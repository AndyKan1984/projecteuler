from problem2 import problem2


def test_problem2_with10() -> None:
    assert problem2(10) == 10


def test_problem2_with20() -> None:
    assert problem2(20) == 10


def test_problem2_with4M() -> None:
    assert problem2(4000000) == 4613732
