import pytest
from typing import Sequence


def safe_mean(xs: Sequence[float]) -> float:
    if not xs:
        raise ValueError("empty")
    return sum(xs) / len(xs)


def test_safe_mean_ok():
    assert safe_mean([1, 2, 3]) == 2

def test_asfe_mean_mixed_types():
    assert safe_mean([1, 2.0, 3]) == 2

def test_safe_mean_empty():
    with pytest.raises(ValueError):
        safe_mean([])