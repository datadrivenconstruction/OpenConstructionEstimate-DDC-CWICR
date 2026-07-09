# Security Policy

This repository is primarily a **data and workflow distribution**
(cost datasets and orchestration scripts) rather than a
long-running service. Security considerations centre on:

- integrity of the distributed datasets and snapshots,
- safety of the adapter scripts (workflows, AI pipelines) that
  consume the data,
- confidentiality of any user-supplied API keys that the
  scripts are configured with.

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**
Public disclosure before a fix is available puts users at risk.

Report vulnerabilities privately to:

- **GitHub Security Advisories** (preferred):
  [Create a new advisory](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR/security/advisories/new)
- **Email:** `info@datadrivenconstruction.io`

### What to Include

- Affected artefact (dataset file, workflow, script, snapshot)
  and release tag / commit hash
- Description of the issue (e.g. malicious script pattern,
  data-integrity defect, credential-leak path in a pipeline)
- Steps to reproduce
- Potential impact
- Your preferred credit attribution (or request for anonymity)

## Response Timeline

| Stage               | Target time                                               |
|---------------------|-----------------------------------------------------------|
| Acknowledgement     | 3 business days                                           |
| Initial assessment  | 14 calendar days                                          |
| Fix or mitigation   | 90 calendar days where technically feasible               |
| Public disclosure   | After a fix is available; at the latest 120 days from report |

## Scope

**In scope:**

- n8n workflow JSON and adapter scripts under
  "0_Workflow and Pipelines CWICR/" (Python, JavaScript, R,
  Rust, shell).
- AI agent instructions under "1_AI_INSTRUCTIONS/".
- The distributed datasets (CSV, XLSX, Parquet) - specifically
  integrity issues such as tampered snapshots, malformed rows
  that crash documented consumers, or embedded payloads.
- Qdrant snapshot files - integrity and safe-restore
  considerations.

**Out of scope:**

- Third-party services consumed by the adapter scripts
  (OpenAI / Anthropic / Google / Mistral / Groq / DeepSeek
  APIs, Qdrant server, n8n runtime) - report directly to the
  upstream vendor.
- Accuracy of the cost data itself - see the "Data accuracy
  disclaimer" in [NOTICE](./NOTICE); data-quality feedback is
  welcomed via standard GitHub issues, not Security Advisories.
- Social engineering of Licensor or downstream users.
- Issues restricted to configurations that expose user-supplied
  API keys in logs or source control through documented-wrong
  setups.

## Supply-chain Integrity

Releases are tagged in git. Large binary assets (XLSX / Parquet /
Qdrant snapshots) are managed via Git LFS; their object hashes
are pinned in the LFS pointer files, which means any tampering
with a release asset is detectable by comparing the stored hash
with the downloaded file's SHA-256.

If you suspect a distributed artefact has been modified in
transit, report it as a security issue - we will publish a
corrected artefact and a signed advisory.

## Regulatory Reporting

Where required by EU Regulation 2024/2847 (Cyber Resilience Act,
vulnerability-reporting obligations effective 11 September 2026),
actively exploited vulnerabilities in the adapter scripts are
reported through the ENISA Single Reporting Platform with
cooperation from the German Federal Office for Information
Security (BSI) / CERT-Bund.

## No Bug Bounty

DataDrivenConstruction currently does not operate a paid
bug-bounty programme. We gratefully acknowledge responsible
researchers in the associated GitHub Security Advisories unless
anonymity is requested.

## Contact

All security communication: `info@datadrivenconstruction.io`.
Where GitHub Security Advisories are available, please use that
channel for reports that include sensitive proof-of-concept
material.
