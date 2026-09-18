// Validate.cs
//
// Structural / type validation for podawaa2024.json and HyperClaper.json.
// Reports errors by record INDEX and error type/count only — never prints
// an author name, handle, profile URL, or post content, consistent with the
// de-identification rule used everywhere else in this repo.
//
// Build & run (requires .NET 8 SDK):
//   cd tools/csharp
//   dotnet run -- podawaa /path/to/podawaa2024.json
//   dotnet run -- hyperclapper /path/to/HyperClaper.json
//   dotnet run -- podawaa /path/to/podawaa2024.json --checksums ../../checksums/CHECKSUMS.txt
//
// Note: this uses System.Text.Json's DOM (JsonDocument), which loads the
// whole file into memory. For podawaa2024.json (~220MB) that's fine on a
// normal dev machine but budget a couple GB of RAM. For much larger files,
// switch to the streaming Utf8JsonReader instead.
//
// Exit code: 0 if no errors, 1 if any validation errors were found.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text.Json;

internal static class Validate
{
    private static int Main(string[] args)
    {
        if (args.Length < 2)
        {
            Console.WriteLine("Usage: dotnet run -- <podawaa|hyperclapper|linkboost> <path> [--checksums <path>]");
            return 2;
        }

        string dataset = args[0];
        string path = args[1];
        string? checksumsPath = null;

        for (int i = 2; i < args.Length; i++)
        {
            if (args[i] == "--checksums" && i + 1 < args.Length)
            {
                checksumsPath = args[i + 1];
            }
        }

        Console.WriteLine($"Validating {dataset}: {path}");

        if (checksumsPath != null)
        {
            CheckChecksum(path, checksumsPath);
        }

        bool ok = dataset switch
        {
            "podawaa" => ValidatePodawaa(path),
            "hyperclapper" => ValidateHyperclapper(path),
            "linkboost" => ValidateLinkboost(path),
            _ => Fatal($"unknown dataset '{dataset}', expected 'podawaa', 'hyperclapper', or 'linkboost'")
        };

        return ok ? 0 : 1;
    }

    private static bool Fatal(string message)
    {
        Console.WriteLine($"  [FATAL] {message}");
        return false;
    }

    private static string Sha256Of(string path)
    {
        using var sha = SHA256.Create();
        using var stream = File.OpenRead(path);
        byte[] hash = sha.ComputeHash(stream);
        return Convert.ToHexString(hash).ToLowerInvariant();
    }

    private static void CheckChecksum(string path, string checksumsPath)
    {
        string fileName = Path.GetFileName(path);
        string? expected = null;

        if (!File.Exists(checksumsPath))
        {
            Console.WriteLine($"  [WARN] checksums file not found: {checksumsPath}");
            return;
        }

        foreach (var line in File.ReadLines(checksumsPath))
        {
            var parts = line.Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries);
            if (parts.Length == 2 && parts[1] == fileName)
            {
                expected = parts[0];
                break;
            }
        }

        if (expected == null)
        {
            Console.WriteLine($"  [WARN] no checksum entry found for {fileName} in {checksumsPath}");
            return;
        }

        string actual = Sha256Of(path);
        if (string.Equals(actual, expected, StringComparison.OrdinalIgnoreCase))
        {
            Console.WriteLine($"  [OK] sha256 matches: {actual}");
        }
        else
        {
            Console.WriteLine($"  [MISMATCH] expected {expected}, got {actual}");
        }
    }

    private sealed class ErrorLog
    {
        public readonly Dictionary<string, int> Counts = new();
        public readonly Dictionary<string, List<int>> Examples = new();

        public void Flag(int index, string errorType)
        {
            Counts[errorType] = Counts.GetValueOrDefault(errorType) + 1;
            if (!Examples.TryGetValue(errorType, out var list))
            {
                list = new List<int>();
                Examples[errorType] = list;
            }
            if (list.Count < 5)
            {
                list.Add(index);
            }
        }
    }

    private static bool Report(int recordCount, ErrorLog log)
    {
        Console.WriteLine($"  Records checked: {recordCount:N0}");
        if (log.Counts.Count == 0)
        {
            Console.WriteLine("  [PASS] no validation errors found");
            return true;
        }

        int total = log.Counts.Values.Sum();
        Console.WriteLine($"  [FAIL] {total:N0} validation errors across {log.Counts.Count} error types:");
        foreach (var kv in log.Counts.OrderByDescending(kv => kv.Value))
        {
            var examples = log.Examples[kv.Key];
            string exampleStr = string.Join(", ", examples);
            Console.WriteLine($"    {kv.Key,-32} {kv.Value:N0} occurrences (e.g. record indices [{exampleStr}])");
        }
        return false;
    }

    private static bool ValidatePodawaa(string path)
    {
        using var stream = File.OpenRead(path);
        using var doc = JsonDocument.Parse(stream);
        var root = doc.RootElement;

        if (root.ValueKind != JsonValueKind.Object || !root.TryGetProperty("Posts", out var posts))
        {
            return Fatal("top-level object missing required key 'Posts'");
        }
        if (posts.ValueKind != JsonValueKind.Array)
        {
            return Fatal("'Posts' is not an array");
        }

        var log = new ErrorLog();
        int i = 0;
        int count = 0;

        foreach (var rec in posts.EnumerateArray())
        {
            count++;
            if (rec.ValueKind != JsonValueKind.Object)
            {
                log.Flag(i, "record_not_object");
                i++;
                continue;
            }

            if (rec.TryGetProperty("linkedinPostId", out var pid) && pid.ValueKind != JsonValueKind.Null)
            {
                if (pid.ValueKind != JsonValueKind.Number || !pid.TryGetInt64(out _))
                {
                    log.Flag(i, "linkedinPostId_wrong_type");
                }
            }

            if (rec.TryGetProperty("Content", out var content) && content.ValueKind != JsonValueKind.Null)
            {
                if (content.ValueKind != JsonValueKind.String)
                {
                    log.Flag(i, "Content_wrong_type");
                }
            }

            if (rec.TryGetProperty("AuthorPublicIdentifier", out var author) && author.ValueKind != JsonValueKind.Null)
            {
                if (author.ValueKind != JsonValueKind.String)
                {
                    log.Flag(i, "AuthorPublicIdentifier_wrong_type");
                }
            }

            if (!rec.TryGetProperty("Likes", out var likes))
            {
                log.Flag(i, "Likes_missing");
            }
            else if (likes.ValueKind != JsonValueKind.Number || !likes.TryGetInt64(out long likesVal))
            {
                log.Flag(i, "Likes_wrong_type");
            }
            else if (likesVal < 0)
            {
                log.Flag(i, "Likes_negative");
            }

            if (!rec.TryGetProperty("Views", out var views))
            {
                log.Flag(i, "Views_missing");
            }
            else if (views.ValueKind != JsonValueKind.Number || !views.TryGetInt64(out long viewsVal))
            {
                log.Flag(i, "Views_wrong_type");
            }
            else if (viewsVal < 0)
            {
                log.Flag(i, "Views_negative");
            }

            i++;
        }

        return Report(count, log);
    }

    private static bool ValidateHyperclapper(string path)
    {
        using var stream = File.OpenRead(path);
        using var doc = JsonDocument.Parse(stream);
        var root = doc.RootElement;

        if (root.ValueKind != JsonValueKind.Object ||
            !root.TryGetProperty("data", out var dataEl) ||
            dataEl.ValueKind != JsonValueKind.Object)
        {
            return Fatal("top-level object missing required key 'data'");
        }
        if (!dataEl.TryGetProperty("post", out var posts) || posts.ValueKind != JsonValueKind.Array)
        {
            return Fatal("'data.post' is not an array");
        }

        var log = new ErrorLog();
        string[] requiredBoolFields = { "comment", "like" };
        string[] requiredStrFields = { "post_url", "created_at" };
        string[] optionalIntFields = { "like_count", "impression_count", "comment_count" };

        int i = 0;
        int count = 0;

        foreach (var rec in posts.EnumerateArray())
        {
            count++;
            if (rec.ValueKind != JsonValueKind.Object)
            {
                log.Flag(i, "record_not_object");
                i++;
                continue;
            }

            foreach (var field in requiredBoolFields)
            {
                if (!rec.TryGetProperty(field, out var v))
                {
                    log.Flag(i, $"{field}_missing");
                }
                else if (v.ValueKind != JsonValueKind.True && v.ValueKind != JsonValueKind.False)
                {
                    log.Flag(i, $"{field}_wrong_type");
                }
            }

            foreach (var field in requiredStrFields)
            {
                if (!rec.TryGetProperty(field, out var v) ||
                    v.ValueKind == JsonValueKind.Null ||
                    (v.ValueKind == JsonValueKind.String && v.GetString() == ""))
                {
                    log.Flag(i, $"{field}_missing");
                }
                else if (v.ValueKind != JsonValueKind.String)
                {
                    log.Flag(i, $"{field}_wrong_type");
                }
            }

            if (rec.TryGetProperty("created_at", out var ca) && ca.ValueKind == JsonValueKind.String)
            {
                var raw = ca.GetString();
                if (raw != null && !DateTimeOffset.TryParse(raw, out _))
                {
                    log.Flag(i, "created_at_unparseable");
                }
            }

            foreach (var field in optionalIntFields)
            {
                if (rec.TryGetProperty(field, out var v) && v.ValueKind != JsonValueKind.Null)
                {
                    // The source data mixes ints and floats here (e.g. 5.0) —
                    // flag anything that isn't a clean non-negative integer.
                    if (v.ValueKind != JsonValueKind.Number)
                    {
                        log.Flag(i, $"{field}_wrong_type");
                    }
                    else if (!v.TryGetInt64(out long iv))
                    {
                        log.Flag(i, $"{field}_wrong_type");
                    }
                    else if (iv < 0)
                    {
                        log.Flag(i, $"{field}_negative");
                    }
                }
            }

            if (rec.TryGetProperty("profile", out var profile) &&
                profile.ValueKind != JsonValueKind.Null &&
                profile.ValueKind != JsonValueKind.Object)
            {
                log.Flag(i, "profile_wrong_type");
            }

            i++;
        }

        return Report(count, log);
    }

    // SuccessfullLikes and SuccessfullComments are "indicators of social
    // media influence" under 16 CFR 465.1(j), governed by 16 CFR 465.8
    // (see docs/regulatory-context.md). This method makes no legal
    // determination about any record — structural/type checks only.
    private static bool ValidateLinkboost(string path)
    {
        using var stream = File.OpenRead(path);
        using var doc = JsonDocument.Parse(stream);
        var root = doc.RootElement;

        if (root.ValueKind != JsonValueKind.Array)
        {
            return Fatal("top-level value is not an array");
        }

        var log = new ErrorLog();
        string[] requiredStrFields = { "Id", "ObjectUrn", "Url", "piFirstName", "piLastName", "UserId" };
        string[] optionalStrFields = { "FirstName", "LastName", "Occupation", "DashEntityUrn",
            "Comment", "liProfileLink", "liUrl", "liDigitalMarketer", "Title", "country" };
        string[] requiredIntFields = { "SuccessfullLikes", "SuccessfullComments", "VolumeId" };

        int i = 0;
        int count = 0;

        foreach (var rec in root.EnumerateArray())
        {
            count++;
            if (rec.ValueKind != JsonValueKind.Object)
            {
                log.Flag(i, "record_not_object");
                i++;
                continue;
            }

            foreach (var field in requiredStrFields)
            {
                if (!rec.TryGetProperty(field, out var v) ||
                    v.ValueKind == JsonValueKind.Null ||
                    (v.ValueKind == JsonValueKind.String && v.GetString() == ""))
                {
                    log.Flag(i, $"{field}_missing");
                }
                else if (v.ValueKind != JsonValueKind.String)
                {
                    log.Flag(i, $"{field}_wrong_type");
                }
            }

            foreach (var field in optionalStrFields)
            {
                if (rec.TryGetProperty(field, out var v) &&
                    v.ValueKind != JsonValueKind.Null &&
                    v.ValueKind != JsonValueKind.String)
                {
                    log.Flag(i, $"{field}_wrong_type");
                }
            }

            foreach (var field in requiredIntFields)
            {
                if (!rec.TryGetProperty(field, out var v))
                {
                    log.Flag(i, $"{field}_missing");
                }
                else if (v.ValueKind != JsonValueKind.Number || !v.TryGetInt64(out long iv))
                {
                    log.Flag(i, $"{field}_wrong_type");
                }
                else if (iv < 0)
                {
                    log.Flag(i, $"{field}_negative");
                }
            }

            i++;
        }

        return Report(count, log);
    }
}
