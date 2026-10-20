import importlib.util
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / "code" / "36_most_frequent.py"
spec = importlib.util.spec_from_file_location("most_frequent_module", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
most_frequent = module.most_frequent


def test_most_frequent_item():
    assert most_frequent([1, 2, 2, 3, 2, 4]) == 2


def test_tie_uses_first_appearance():
    assert most_frequent(["apple", "banana", "banana", "apple"]) == "apple"


def test_empty_list():
    assert most_frequent([]) is None


def test_single_item():
    assert most_frequent(["python"]) == "python"


def test_all_items_unique():
    assert most_frequent([4, 2, 7]) == 4
