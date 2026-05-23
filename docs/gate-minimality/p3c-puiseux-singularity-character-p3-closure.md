# HG-MTH-018 — P3.c Puiseux Singularity and Character at p=3 Closure

Identifier: `HG-MTH-018`  
Status: closure document for P3.c; scoped by `HG-MTH-017`.  
Owner: `SocioProphet/Heller-Godel`.  
Track: P3.c under `HG-MTH-012`, after P3.a closure `HG-MTH-014` and P3.b closure `HG-MTH-016`.  
Claim level: method-grade modulo candidate-`HG-FND-003` and candidate-`HG-VOC-006`.

## 1. Statement of closure

P3.c closure verifies the Puiseux singular datum of the algebraic function:

```text
C_3(x)=1+x C_3(x)^3
```

The closure establishes:

```text
rho_3 = 4/27
C_3(rho_3)=3/2
alpha_3 = 1/2
```

and derives the principal-branch expansion:

```text
C_3(x)=3/2 - (sqrt(3)/2)(1 - x/rho_3)^(1/2) + (2/3)(1 - x/rho_3) + O((1 - x/rho_3)^(3/2)).
```

For Q4, this closure selects option (b) at the source-identification level: the non-local `mu_3` source is the cyclic `A_3 ~= Z/3` sheet-rotation subgroup inside the global cubic algebraic-function monodromy structure. The specific primitive element is fixed by an explicit positive-generator convention and the manuscript finite phase-map convention.

This file is intentionally expanded in a follow-up patch if connector payload limits require it.
