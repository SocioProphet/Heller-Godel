from itertools import permutations

from heller_godel.emr_complex import (
    f_vector,
    ordered_set_partitions,
    permute_lambda,
    reduced_betti,
    reduced_euler_characteristic,
    sigma_lambda,
    vertex_labels,
)


def test_fubini_count():
    assert len(ordered_set_partitions(3)) == 13
    assert len(ordered_set_partitions(4)) == 75
    assert len(ordered_set_partitions(5)) == 541


def test_emr_figure_1_vertices():
    complex_ = sigma_lambda([5, 1, -2, -3])
    assert vertex_labels(complex_) == (
        "{1}",
        "{2}",
        "{1,2}",
        "{1,3}",
        "{1,4}",
        "{1,2,3}",
        "{1,2,4}",
    )


def test_emr_figure_1_fvector():
    assert f_vector(sigma_lambda([5, 1, -2, -3])) == (7, 12, 6)


def test_all_positive_lambda_is_full_complex():
    n = 4
    complex_ = sigma_lambda([1] * n)
    assert len(complex_.vertices) == 2**n - 2
    assert sum(f_vector(complex_)) == len(ordered_set_partitions(n)) - 1


def test_all_negative_lambda_is_empty():
    complex_ = sigma_lambda([-1, -2, -3, -4])
    assert complex_.faces == frozenset()
    assert f_vector(complex_) == ()


def test_lemma_37_isomorphism():
    lam = (5, 1, -2, -3)
    baseline = f_vector(sigma_lambda(lam))
    for perm in permutations(range(len(lam))):
        assert f_vector(sigma_lambda(permute_lambda(lam, perm))) == baseline


def test_reduced_euler_characteristic():
    complex_ = sigma_lambda([5, 1, -2, -3])
    betti = reduced_betti(complex_)
    homology_euler = sum(((-1) ** dim) * value for dim, value in enumerate(betti))
    assert reduced_euler_characteristic(complex_) == 0
    assert homology_euler == reduced_euler_characteristic(complex_)
