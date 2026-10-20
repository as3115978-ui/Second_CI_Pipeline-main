import importlib.util
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / "code" / "40_gcd.py"
spec = importlib.util.spec_from_file_location("gcd_module", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
gcd = module.gcd


def test_gcd_of_two_positive_numbers():
    assert gcd(48, 18) == 6


def test_gcd_with_coprime_numbers():
    assert gcd(7, 5) == 1


def test_gcd_with_zero():
    assert gcd(12, 0) == 12


def test_gcd_with_negative_numbers():
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6


def test_gcd_of_two_zeros():
    assert gcd(0, 0) == 0


def test_gcd_with_equal_numbers():
    assert gcd(9, 9) == 9
