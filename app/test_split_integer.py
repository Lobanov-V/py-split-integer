from app.split_integer import split_integer


def test_split_integer_even_parts():
    assert split_integer(8, 4) == [2, 2, 2, 2]


def test_split_integer_length():
    assert len(split_integer(9, 3)) == 3


def test_split_integer_sum_preserved():
    assert sum(split_integer(20, 6)) == 20


def test_split_integer_single_part():
    assert split_integer(7, 1) == [7]


def test_split_integer_more_parts_than_value():
    result = split_integer(3, 5)
    assert len(result) == 5
    assert sum(result) == 3
