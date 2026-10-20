import importlib.util
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / "code" / "35_move_zeros.py"
spec = importlib.util.spec_from_file_location("move_zeros_module", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
move_zeros = module.move_zeros


def test_move_zeros():
    assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_no_zeros():
    assert move_zeros([1, 2, 3]) == [1, 2, 3]


def test_all_zeros():
    assert move_zeros([0, 0, 0]) == [0, 0, 0]


def test_empty_list():
    assert move_zeros([]) == []


def test_preserve_order():
    assert move_zeros([4, 0, 2, 0, 1]) == [4, 2, 1, 0, 0]
