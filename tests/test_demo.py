import pytest

from crawler_zsxq.lib import InvalidSomethingError, demo_function


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 6),
        (10, 3628800),
    ],
)
def test_demo_function(n: int, expected: int) -> None:
    assert demo_function(n) == expected


@pytest.mark.parametrize(
    "n",
    [
        -1,
        -100,
    ],
)
def test_invalid_demo_function(n: int) -> None:
    with pytest.raises(InvalidSomethingError):
        demo_function(n)
