# Source Classification Ledger

This ledger classifies the uploaded corpus for the Heller-Godel repository. It distinguishes load-bearing primary sources from context and future-horizon material.

## Primary / load-bearing for Heller-Godel

| File | Role | SHA-256 |
|---|---|---|
| `heller godel motivation.pdf` | Motivation document for the Heller-Godel program: incompleteness, observer projection, proof-character ambition, falsifiability. | `9171961d38479db65b50d17faa73e9ec3dd3c866c65f79f8fa820de4b6ae733c` |
| `calculus invariant characters v2(2).pdf` | Revised technical paper: proof-class generating functions, phase maps, carry defect, regulator sketch, base pairings. | `21738175a878d4903066f12e16a28de2e041e3759ea843ef9ccf165baad8c19c` |
| `calculus invariant characters(2).pdf` | Earlier technical draft used for comparison and regression of claim boundaries. | `17e7821319a95796f58e5622f7ed0f75ea80071f5cbd46ef6521234be2af01d9` |

## Context / future-horizon sources

| File | Role | SHA-256 |
|---|---|---|
| `time_theory_draft_v23_layout_exec(1).pdf` | Context and future-horizon host for shell, operator, projection, and time-dynamics ideas. Not a current theorem dependency. | `5b8538bde2433837f061f791cd4443a023e3bd57395b7e5805c7427797c60436` |

## BSD reference/context only

BSD materials are retained as methodological precedent and source context only. They do not enter the Heller-Godel reproducibility harness unless a future manuscript explicitly cites a BSD artifact as evidence for a Heller-Godel claim.

| File | Role | SHA-256 |
|---|---|---|
| `BSD_Program_Lane_v0.1.pdf` | BSD lane v0.1 program specification and evidence-gate precedent. | `ca8de0c4817b34f3ece0435c91e262116723da955549f9744bf63454e4d14473` |
| `BSD_Program_Lane_v0.2.pdf` | BSD lane v0.2 launch specification; executed Tunnell milestone and workstream discipline. | `599b4d5a5021adc3d42a717cb598f95dfdca51e0b984045f3c82754fbfa58c95` |
| `BSD_Program_Log_M3_snapshot.pdf` | Example of validation failure handling and rollback discipline. | `3893a1de09de16e2cf53cff1e8781138653c1e67d829f1fb49c7ab5464696660` |
| `BSD_53_Rows_Resolution.pdf` | Explicit witness and milestone-report precedent. | `7ca397f04cb05272b36a47ed3ab67452bd7d47af594c9ac24e84f6739d3e9dca` |
| `bsd_milestone_4(1).zip` | BSD Milestone 4 bundle; retained for reference, not imported into tests. | `9a0c54929c655961585960132772d9ad2738711cb53110ed508562e9228ec7ed` |

## Rule

A file classified as context or future-horizon may be cited in explanatory notes, but it may not support a theorem claim in `docs/manuscripts/` unless a promotion note changes its classification and states the exact dependency.
