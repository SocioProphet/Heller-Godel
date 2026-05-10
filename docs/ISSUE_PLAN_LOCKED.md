# Locked Issue Plan

## HG-M0 — Repository Bootstrap

Status: started upstream.

Acceptance:

- README states the current claim boundary.
- AGENTS.md gives operating rules.
- Source classification ledger exists.
- Claim boundary register exists.
- Gödel/provability note exists.
- Source manifest exists.

## HG-M1 — Source Import and Manifest Lock

Goal: import the uploaded primary sources and context sources into the repository with exact hashes.

Acceptance:

- Binary sources are present under `sources/primary/` or `sources/context/`, or explicitly marked as pending binary import.
- `SOURCE_MANIFEST.json` and `SOURCE_MANIFEST.sha256` match repository contents.
- BSD files are classified context-only.
- Temporal Mechanics is classified context/future-horizon.
- Primary Heller-Godel files are classified load-bearing.

## HG-M2 — Corrected Proof-Character Manuscript v2.1.3

Goal: produce the corrected manuscript after the v2.1.2 review.

Required corrections:

- Treat `zeta_p` as a coboundary/section defect in ordinary cohomology.
- Remove nontrivial/nonabelian central-extension claims unless extra structure is added.
- Define singular exponents as Puiseux exponent channels.
- Demote regulator/Chern-class material to candidate/future work.
- Correct the chain-product example.
- Require canonicalization before calculus-invariance claims.
- Add prime-indexed family `(chi_p)_p` before finite `P_13` truncation.

## HG-M3 — Verification Harness

Goal: implement reproducible tests for all current computational claims.

Acceptance:

- `chi_13` and `k_13` examples pass.
- `zeta_p` examples pass.
- `zeta_p` coboundary identity passes.
- `zeta_p` symmetry passes.
- Chain-product correction has a regression test.
- Catalan Puiseux channel has a regression test or documented symbolic check.
- Statistic falsifier has a reproducible script/test.

## HG-M4 — Future-Horizon Archive

Goal: preserve material removed from current theorem focus without losing it.

Buckets:

- continued fractions / irrational return scales,
- spectral shell hypothesis,
- operator spectra and Lyapunov/decay cycles,
- nonassociative and Moufang holonomy,
- Temporal Mechanics crosslink.

Acceptance:

- Each future-horizon note states missing prerequisites.
- No future-horizon material is cited as theorem support in the main manuscript.

## HG-M5 — Artifact Rendering and Hash Freeze

Goal: render canonical manuscripts from source and freeze generated hashes.

Acceptance:

- Manuscript PDFs are generated from source.
- Render command is recorded.
- Artifact hashes are recorded.
- Source artifacts and generated artifacts are separated.
