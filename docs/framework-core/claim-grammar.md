# Framework-Core Claim Grammar

Status: bootstrap governance rule.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

This document defines how Heller-Godel framework objects are identified and cited by downstream program repositories.

## Stable identifier scheme

Framework objects use identifiers of the form:

```text
HG-{LAYER}-{NNN}
```

where:

- `HG` is the repository namespace for `SocioProphet/Heller-Godel`;
- `LAYER` is one of `FND`, `VOC`, `MTH`, `EX`, `REF`, or `DOC`;
- `NNN` is a zero-padded three-digit number.

Optional version tags may be used in prose when an object has materially changed:

```text
HG-FND-001 v0.2
```

The canonical citation should still include the merged commit SHA.

## Layer codes

| Layer | Meaning |
| --- | --- |
| `FND` | Framework-foundational object |
| `VOC` | Framework-vocabulary object |
| `MTH` | Framework-method or governance method |
| `EX` | Worked example or canonical fixture |
| `REF` | Bibliographic or provenance reference |
| `DOC` | Governance / doctrine object |

## Downstream citation form

Downstream Clay-program repositories should cite framework objects as:

```text
[HG-FND-001 @ <merged-main-commit-sha>]
```

The commit SHA must be a merged commit on `main`, not a floating branch tip and not a generic reference to current `main`.

## Required citation metadata

A downstream citation should record:

1. framework identifier;
2. merged Heller-Godel commit SHA;
3. distance tier;
4. citation grade: `theorem-grade`, `method-grade`, `fixture-grade`, or `provenance-grade`;
5. the exact local claim licensed by the citation.

## Citation grades

| Grade | Meaning | May license |
| --- | --- | --- |
| `theorem-grade` | typed proved or canonically cited object | theorem premises within declared scope |
| `method-grade` | method, governance rule, bridge specification, or classification | procedure, analogy, taxonomy, or review discipline |
| `fixture-grade` | worked example or apparatus validation fixture | apparatus alignment only |
| `provenance-grade` | source capture, historical note, imported Drive artifact, or unpromoted draft | historical origin only |

## Forbidden citation patterns

The following are forbidden:

- citing an `HG-*` object without a merged commit SHA in downstream theorem-grade text;
- citing Drive RTF/PDF material as canonical after it has an imported repo version;
- citing a fixture as proof of progress on a Clay problem;
- citing Universal Bridge material as proof equivalence or proof transfer;
- citing an anti-seed entry as positive mathematical content;
- using downstream Clay-program success to promote an upstream Heller-Godel object without a Heller-Godel promotion PR.

## Anti-seed precedence

Every positive framework object should have an associated anti-seed entry before promotion.

The anti-seed entry does not prove the positive object. It records a failure mode and constrains unsafe uses.

## Bootstrap active identifiers

| Identifier | Object | Grade | Status |
| --- | --- | --- | --- |
| `HG-MTH-001` | Framework-core distance classification | method-grade | active |
| `HG-MTH-002` | Claim grammar and citation rule | method-grade | active |
| `HG-MTH-003` | Dependency graph | method-grade | active |
| `HG-MTH-004` | Anti-seed framework register | method-grade | active |
| `HG-EX-001` | Catalan / mu_2 canonical reference fixture | fixture-grade | active doctrine; implementation pending |
| `HG-DOC-001` | Framework-core declaration for existing Heller-Godel repo | method-grade / governance | active |

## Existing Paper I identifiers

Existing Paper I artifacts may retain their current local names and theorem labels. This bootstrap does not rewrite manuscript numbering.

Future PRs may add an identifier crosswalk mapping manuscript theorem labels and proof artifacts into the `HG-*` registry. Until that crosswalk exists, downstream repos should cite file paths and commit SHAs in addition to any manuscript-local labels.

## Example downstream citation block

```markdown
Framework citations:

- [HG-EX-001 @ <sha>] — Catalan / mu_2 fixture; citation grade: fixture-grade;
  licensed use: apparatus-alignment check only.
- [HG-MTH-002 @ <sha>] — claim grammar; citation grade: method-grade;
  licensed use: downstream citation format.
```

## Review rule

A PR that adds an `HG-*` identifier must update this document or `docs/framework-core/distance-classification.md` in the same PR.
