import pytest

from my_arithmetic_llamoity import gcd


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (12, 18, 6),
        (18, 12, 6),
        (17, 5, 1),
        (7, 7, 7),
        (0, 5, 5),
        (5, 0, 5),
        (0, 0, 0),
        (-4, 6, 2),
        (4, -6, 2),
        (-4, -6, 2),
    ],
)
def test_gcd(a, b, expected):
    assert gcd(a, b) == expected
