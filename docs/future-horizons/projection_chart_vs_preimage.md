# Projection Chart vs. Preimage Geometry

Status: future-horizon / methodological note. This document preserves the projection/preimage vocabulary developed in the chat corpus. It is not a theorem and does not imply a holographic duality for proof classes.

## 1. Purpose

The Heller–Gödel program repeatedly encounters projected invariants:

- finite phase fingerprints such as `chi_p` and `chi_13`;
- carry defects such as `zeta_p`;
- shell projections of richer Puiseux singularity data;
- base-relative visibility of flat or torsion data.

Projected invariants are useful, but they are not the whole object. This note records the discipline:

```text
projection is evidence about a chosen view, not automatically evidence about the preimage object.
```

The practical rule is: before upgrading a projected obstruction into theorem-core topology, identify the preimage object, the section, the gauge freedom, and the equivalence relation.

## 2. The model example: Poincare disk and hyperbolic plane

The Poincare disk represents the hyperbolic plane inside a bounded Euclidean disk. The representation has a visual center and a circular boundary.

Those features are partly chart artifacts:

- every point of `H^2` can be moved to the center by an isometry;
- tiles that appear small near the boundary can have equal intrinsic hyperbolic size;
- the boundary circle is a compactification of infinity, not an ordinary finite boundary of `H^2`.

This gives a clean conceptual distinction:

```text
chart feature != intrinsic feature
```

The chart is useful, but the theorem must be about the intrinsic object.

## 3. Heller–Gödel analog: zeta_p as projected defect

The displayed carry term is:

```math
zeta_p(alpha,beta)
= floor(p(alpha+beta)) - floor(p alpha) - floor(p beta) mod p.
```

It is a real finite-resolution multiplicativity defect for the projected phase map.

But with

```math
f_p(alpha) = floor(p alpha) mod p,
```

it satisfies

```math
zeta_p(alpha,beta)=f_p(alpha+beta)-f_p(alpha)-f_p(beta).
```

Thus in ordinary group cohomology with free cochain changes, it is a coboundary. The projected obstruction dissolves in the cochain preimage.

This does not make `zeta_p` trivial as a computational object. It means its current theorem-core interpretation is:

```text
finite-resolution section defect / carry correction
```

not:

```text
nontrivial cohomological obstruction
```

unless extra structure restricts the allowed gauges or supplies a different cohomological setting.

## 4. Section choice and gauge discipline

A projection requires a section or chart choice. Heller–Gödel must keep these choices explicit:

- proof grammar;
- canonical normal-form convention;
- statistic `sigma`;
- singularity channel selection;
- finite prime truncation;
- base manifold or visibility context.

A notation such as `chi_p(phi)` is therefore usually too compressed. A safer conceptual form is:

```text
chi_p(phi; grammar, normal_form, sigma, channel, section)
```

The notation can be abbreviated once the context is fixed, but the proof must know what was fixed.

## 5. Shell projection discipline

The dominant-shell character is a projection of richer analytic data:

```text
full singularity object
-> Puiseux shell support
-> dominant shell
-> finite prime phase fingerprint
```

Information can be lost at each arrow. Therefore a claim about the finite phase fingerprint is not automatically a claim about the full singularity object.

This is why multi-shell support and admissible-statistics tests matter: they check how much of the projection survives changes of channel, statistic, or grammar.

## 6. Base-relative visibility

A base space can make some data visible and hide other data. For example:

- `S^2` has no flat `H^1` data but has integral `H^2` curvature data;
- `T^2` has rich flat holonomy and integral Chern data;
- the Klein bottle has a `Z/2` torsion feature useful for discussing `p=2` visibility.

This remains future-horizon until a proof-family bundle, local system, or proof-moduli map is actually constructed.

## 7. AdS/CFT caution

AdS/CFT is a strong physical duality, not merely a metaphor for projection. It asserts an equivalence between bulk and boundary descriptions with a precise dictionary of observables.

Heller–Gödel currently has projection/preimage discipline, not a holographic duality. The safe lesson from AdS/CFT is:

```text
a real bulk-boundary theory requires a rigorous dictionary, not vocabulary similarity.
```

Unsafe language to avoid:

```text
chi_p is the holographic boundary of a proof class.
```

Safe language:

```text
chi_p is a finite projected phase shadow of selected singularity data, relative to fixed choices.
```

## 8. Promotion conditions

This note becomes theorem-supporting only when the following exist:

1. a defined preimage object, e.g. proof-moduli or multichannel singularity object;
2. a specified projection map;
3. section/gauge choices;
4. an equivalence relation identifying when two projections represent the same preimage data;
5. a theorem showing which features are projection artifacts and which are intrinsic.

Until then, projection/preimage language is methodological guidance and future-horizon vocabulary.

## 9. Repository boundary

This note supports future-horizon routing and claim discipline. It must not be cited as proof of any regulator, Chern-class, holographic, or cognition claim.
