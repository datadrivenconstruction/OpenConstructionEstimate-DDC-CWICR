# Contributing to OpenConstructionEstimate DDC CWICR

Thank you for your interest in improving the DDC CWICR
dataset and its adapter scripts. Before opening a pull
request, please read this short guide.

## Scope of contributions

**In scope (Apache-2.0 Code):**

- n8n workflow JSON and pipeline definitions under
  `0_Workflow and Pipelines CWICR/`
- AI agent instruction files under `1_AI_INSTRUCTIONS/`
- Python, JavaScript, R, Rust, and shell adapter scripts
- Dockerfiles and build automation

**In scope (CC BY-NC 4.0 Data and Documentation):**

- Schema clarifications and data-dictionary improvements
- New regional cost-reference entries for existing language
  tracks (must cite public sources)
- New language-track additions (open discussion first)
- Documentation and README improvements in any language

**Out of scope:**

- The copyrighted PDF book is not open to community edits.
- Large dataset rewrites without prior agreement.

See [LICENSE](./LICENSE), [LICENSE-DATA.txt](./LICENSE-DATA.txt),
[LICENSE-CODE.txt](./LICENSE-CODE.txt), and
[NOTICE](./NOTICE) for the full dual-licensing scheme.

## How to contribute

1. Fork the repository.
2. Create a feature branch from `main`:
   `git checkout -b feat/<short-description>`.
3. Make your changes. Keep the change focused and atomic.
4. For data changes, include a source citation in the PR
   description.
5. **Sign every commit** (Developer Certificate of Origin):
   `git commit -s -m "..."`. The `dco.yml` workflow fails any
   PR with unsigned commits.
6. Open a pull request against `main` with a clear description
   of what changed and why.
7. Address review feedback and rebase as needed.

## Developer Certificate of Origin (DCO)

By signing off on a commit you attest to the
**Developer Certificate of Origin** at
<https://developercertificate.org/>. In short: you confirm that
you have the right to submit the contribution under the
project's open-source licence (Apache-2.0 for code; CC BY-NC 4.0
for data and documentation).

Sign with `git commit -s`. To fix already-unsigned commits:

```bash
git rebase --signoff main
```

## Data-quality standards

When contributing cost data:

- cite at least one public, verifiable source per row or batch;
- harmonise units to SI where possible;
- maintain currency consistency within each language track
  (see [DATA_DICTIONARY.md](./DATA_DICTIONARY.md) for the
  currency column and the per-track reference region);
- provide a short rationale for prices that deviate by more
  than 30% from the existing median.

## Code of Conduct

Contributors agree to follow the [Code of Conduct](./CODE_OF_CONDUCT.md)
(Contributor Covenant 2.1) in all project spaces.

## Reporting bugs and feature requests

- **Bug or feature:** open a GitHub issue using the appropriate
  template.
- **Security vulnerability:** do not open a public issue. See
  [SECURITY.md](./SECURITY.md) for the private reporting
  channel.
- **Data-quality concern:** open a GitHub issue with the
  "data quality" label; include the affected row identifier(s)
  and the discrepancy with a public source.

## Citation

If you publish research or a product built on DDC CWICR,
please cite the dataset. See [CITATION.cff](./CITATION.cff) for
the machine-readable citation and the attribution format in
[LICENSE](./LICENSE) Section 1.

Contact: `info@datadrivenconstruction.io`
