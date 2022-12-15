from problem2 import sum_evens_in_fibonacci


def test_problem2_with10() -> None:
    assert sum_evens_in_fibonacci(10) == 10


def test_problem2_with20() -> None:
    assert sum_evens_in_fibonacci(20) == 10


def test_problem2_with40() -> None:
    assert sum_evens_in_fibonacci(40) == 44


def test_problem2_with4M() -> None:
    assert sum_evens_in_fibonacci(4_000_000) == 4_613_732
