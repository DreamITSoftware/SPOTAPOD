// Deidentify.cs
//
// Produces a de-identified COPY of one of the three source files, for
// your own local use. Run on your machine against your own copy of the
// data — its output is NOT something this repo ever generates, stores,
// or ships, and it should not be committed to git or shared/published
// anywhere. See tools/README.md.
//
// What "de-identified" means here, precisely — read before trusting the
// output for anything sensitive:
//
//   DEFAULT MODE hashes direct identifiers (handles, real names,
//   internal LinkedIn URNs/IDs, profile links, photos) with SHA-256 and
//   leaves post content untouched. This stops casual browsing/grep from
//   exposing an identity, but it does NOT stop re-identification via the
//   post content itself — a distinctive sentence in a post's text can be
//   pasted into a search engine and traced back to its original author
//   regardless of what happened to the identifier fields. This is the
//   same failure mode that de-anonymized the AOL search-log and Netflix
//   Prize datasets: removing the ID column doesn't remove
//   identifiability when the retained content is unique enough to
//   fingerprint.
//
//   --redact-content ALSO removes post/comment content fields entirely
//   (Content / post_title / Title / Comment), closing that gap — at the
//   cost of removing most of what the data is useful for.
//
//   Quasi-identifiers (headline, occupation, location, country, follower
//   counts, etc.) are left untouched in both modes. See docs/privacy.md
//   and docs/demographics.md for why this repo never aggregates those
//   beyond population-level statistics.
//
// Build & run (requires .NET 8 SDK):
//   cd tools/csharp/deidentify
//   dotnet run -- podawaa /path/to/podawaa2024.json /path/to/output.json
//   dotnet run -- hyperclapper /path/to/HyperClaper.json /path/to/output.json
//   dotnet run -- linkboost /path/to/LinkBoost-2025.json /path/to/output.json --redact-content
//
// Options:
//   --redact-content     Also strip post/comment content fields (see above)
//   --salt SALT          Salt the hash (default: unsalted, reproducible
//                        across runs). A salted hash is NOT reproducible
//                        across runs unless you reuse the same salt value.
//
// Note: this uses System.Text.Json's DOM (JsonDocument/JsonNode), which
// loads the whole file into memory — fine for these file sizes on a
// normal dev machine.

using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;

internal static class Deidentify
{
    private static int Main(string[] args)
    {
        if (args.Length < 3)
        {
            Console.WriteLine("Usage: dotnet run -- <podawaa|hyperclapper|linkboost> <input_path> <output_path> [--redact-content] [--salt <salt>]");
            return 2;
        }

        string dataset = args[0];
        string inputPath = args[1];
        string outputPath = args[2];
        bool redactContent = false;
        string? salt = null;

        for (int i = 3; i < args.Length; i++)
        {
            if (args[i] == "--redact-content")
            {
                redactContent = true;
            }
            else if (args[i] == "--salt" && i + 1 < args.Length)
            {
                salt = args[++i];
            }
        }

        string json = File.ReadAllText(inputPath);
        var root = JsonNode.Parse(json);
        if (root == null)
        {
            Console.WriteLine("  [FATAL] could not parse input JSON");
            return 1;
        }

        int identifiersHashed = 0;
        int contentRedacted = 0;

        string Hash(string? value)
        {
            if (string.IsNullOrEmpty(value)) return value ?? "";
            string raw = salt != null ? $"{salt}:{value}" : value;
            byte[] bytes = SHA256.HashData(Encoding.UTF8.GetBytes(raw));
            string hex = Convert.ToHexString(bytes).ToLowerInvariant().Substring(0, 16);
            return "anon_" + hex;
        }

        void HashField(JsonObject obj, string field)
        {
            var v = obj[field]?.GetValue<string>();
            if (!string.IsNullOrEmpty(v))
            {
                obj[field] = Hash(v);
                identifiersHashed++;
            }
        }

        void RedactField(JsonObject obj, string field)
        {
            if (obj[field] != null)
            {
                obj[field] = null;
                contentRedacted++;
            }
        }

        switch (dataset)
        {
            case "podawaa":
                {
                    var posts = root["Posts"]?.AsArray();
                    if (posts != null)
                    {
                        foreach (var node in posts)
                        {
                            if (node is not JsonObject rec) continue;
                            HashField(rec, "AuthorPublicIdentifier");
                            if (redactContent) RedactField(rec, "Content");
                        }
                    }
                    break;
                }
            case "hyperclapper":
                {
                    var posts = root["data"]?["post"]?.AsArray();
                    if (posts != null)
                    {
                        foreach (var node in posts)
                        {
                            if (node is not JsonObject rec) continue;
                            if (rec["profile"] is JsonObject profile)
                            {
                                HashField(profile, "name");
                                HashField(profile, "profile_picture");
                                if (profile["linkedin_data"] is JsonObject ld)
                                {
                                    HashField(ld, "fullName");
                                    HashField(ld, "public_identifier");
                                    HashField(ld, "linkedin_profile_link");
                                    HashField(ld, "linkedin_profile_id");
                                    HashField(ld, "profilePicture");
                                }
                            }
                            if (redactContent) RedactField(rec, "post_title");
                        }
                    }
                    break;
                }
            case "linkboost":
                {
                    var records = root.AsArray();
                    foreach (var node in records)
                    {
                        if (node is not JsonObject rec) continue;
                        foreach (var field in new[] { "FirstName", "LastName", "piFirstName", "piLastName",
                                                        "DashEntityUrn", "ObjectUrn", "liProfileLink",
                                                        "liDigitalMarketer", "UserId" })
                        {
                            HashField(rec, field);
                        }
                        if (redactContent)
                        {
                            RedactField(rec, "Title");
                            RedactField(rec, "Comment");
                        }
                    }
                    break;
                }
            default:
                Console.WriteLine($"  [FATAL] unknown dataset '{dataset}'");
                return 1;
        }

        var options = new JsonSerializerOptions { WriteIndented = false };
        File.WriteAllText(outputPath, root.ToJsonString(options));

        Console.WriteLine($"De-identified copy written to {outputPath}");
        Console.WriteLine($"  Identifiers hashed:  {identifiersHashed:N0}");
        Console.WriteLine($"  Content fields redacted: {contentRedacted:N0}");
        if (!redactContent)
        {
            Console.WriteLine();
            Console.WriteLine("  NOTE: post/comment content was left intact. This output is");
            Console.WriteLine("  NOT re-identification-resistant on its own — see the file header");
            Console.WriteLine("  comment. Re-run with --redact-content if you need that.");
        }
        Console.WriteLine();
        Console.WriteLine("  Do not commit this output to git or share/publish it. See");
        Console.WriteLine("  tools/README.md.");

        return 0;
    }
}
