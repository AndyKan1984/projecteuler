from problem1 import find_divisible
from problem1 import sumList


def test_problem1_with1000() -> None:
    assert sumList(find_divisible(1000, [3, 5])) == 233168


def test_problem1_with10() -> None:
    assert sumList(find_divisible(10, [3, 5])) == 23
