# Proof Dynamics Status

This directory records the fixture-level proof-dynamics bridge for the Heller-Godel program.

## Proved for the Catalan `mu_2` fixture

- Catalan full binary tree species have generating function `C(z) = (1 - sqrt(1 - 4z)) / (2z)`.
- The local branch coordinate `tau^2 = 1 - 4z` has `mu_2` branch fiber.
- A branch flip contributes analytic signature `-1`.
- The declared `SO(3)` gate sends a branch flip to a `2pi` rotation loop.
- The `SU(2) -> SO(3)` spin lift of that loop terminates at `-I`, giving spin sign `-1`.
- For declared neutral transport paths in `Assoc_n x mu_2`, branch parity recomputes both analytic and gate signatures.

## Not proved

- This is not a proof of `P != NP`.
- This is not a universal proof-system theorem.
- This is not a closed Lyapunov-cycle existence theorem.
- This is not empirical validation of Lawful Learning.
- This is not an odd-prime generalization.

## Protocol boundary

The protocol is phase-separated:

1. descent/selective machinery may select or freeze an active constraint complex;
2. neutral transport probes monodromy on the frozen complex;
3. the verifier recomputes signatures from the transport path;
4. any overclaim outside fixture-level monodromy agreement is invalid.
