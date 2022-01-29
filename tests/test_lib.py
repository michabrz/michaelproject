from michaelproject.lib import is_even_num


def test_enum():
    num_list = is_even_num([2, 4])
    assert [num % 2 == 0 for num in num_list]
