from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(20, 6)
    assert sum(result) == 20


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(9, 1) == [9]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_difference_between_max_and_min_is_not_more_than_one() -> None:
    result = split_integer(100, 9)
    assert max(result) - min(result) <= 1


def test_length_equals_number_of_parts() -> None:
    result = split_integer(50, 7)
    assert len(result) == 7


def test_could_split_on_different_parts() -> None:
    result = split_integer(25, 4)
    assert sum(result) == 25
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_split_on_incorrect_parts_pattern() -> None:
    result = split_integer(7, 3)
    assert result == [2, 2, 3]


def test_split_on_different_parts() -> None:
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]
