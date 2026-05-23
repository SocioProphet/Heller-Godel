from heller_godel.phase_characters import carry, carry_cocycle_identity_holds, carry_table, tame_symbol_standard


def test_carry_1_1_level_2():
    assert carry(1, 1, 2) == 1


def test_carry_0_0_level_2():
    assert carry(0, 0, 2) == 0


def test_carry_identity_level_2_all_residues():
    for a in range(2):
        for b in range(2):
            for c in range(2):
                assert carry_cocycle_identity_holds(a, b, c, 2)


def test_tame_symbol_value_is_distinct_from_integer_carry():
    carry_value = carry(1, 1, 2)
    tame_value = tame_symbol_standard(1, 1)
    assert tame_value != carry_value
    assert isinstance(carry_value, int)
    assert isinstance(tame_value, (complex, int))


def test_carry_table_level_3():
    assert carry_table(3) == ((0, 0, 0), (0, 0, 1), (0, 1, 1))
