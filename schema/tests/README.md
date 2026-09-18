# Tests

Run all tests:

```bash
python3 -m unittest discover -s tests -v
```

`fixtures/` contains small, entirely fabricated JSON files — fictional
names, fake URNs, invented occupations — matching the shape of the three
real datasets. No test in this repo touches, downloads, or requires any
real dataset file.

Each test module checks two things per script: that it runs and reports
the right aggregate counts, and — just as important — that its output
never contains any identifier from the fixture (name, handle, URN, email-
shaped string, etc.). That second check is the actual point: it's an
automated tripwire for the "no script may print an identifier" rule in
`CONTRIBUTING.md`. If a future change accidentally starts leaking a field
that should stay hashed, these tests are what catch it.
