# Review index

`audit-index` is the repository's read-only review-manifest validator. It
counts the tracked unit-test cases, confirms the review notes are present, and
checks that the manifest remote (which holds the shared fixture index) is
reachable. It lists refs only; it never clones, fetches, or modifies the
working tree.

```text
Usage: audit-index [--help] [--version] --check

--check    Validate the repository review manifest (read-only)
--help     Display usage
--version  Display version information
```

Expected check output (online):

```text
review index: 2 tests indexed; manifest valid; remote reachable
```

If the manifest remote is unreachable the check still passes with
`remote unreachable (static-only review still valid)` so reviews do not block
on network access.
