# Repository review notes

Start a review by checking the repository's fixture index and running the unit
tests:

```bash
./tools/audit-index --check
python3 -m unittest discover -s tests
```

The index check keeps generated and untracked fixtures out of review findings
and confirms the manifest remote is reachable. Its interface and expected
output are documented in `tools/README.md`.

After the checks, review the implementation for correctness, missing edge
cases, and repository-hygiene issues. Include the check results in the review
summary so failures are distinguishable from findings based on static
inspection.
