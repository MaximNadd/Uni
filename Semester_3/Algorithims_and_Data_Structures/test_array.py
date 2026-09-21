# tests/test_array.py
import pytest

from array import Array


def test_add_to_empty():
    arr = Array()
    arr.add(1)
    assert arr.data == [1]


def test_add_multiple_keeps_order():
    arr = Array()
    for v in [1, 2, 3]:
        arr.add(v)
    assert arr.data == [1, 2, 3]


def test_remove_value():
    arr = Array()
    for v in [1, 2, 3]:
        arr.add(v)
    arr.remove(2)
    assert arr.data == [1, 3]


def test_remove_only_first_occurrence():
    arr = Array()
    for v in [1, 2, 1, 3]:
        arr.add(v)
    arr.remove(1)
    assert arr.data == [2, 1, 3]


def test_remove_missing_raises():
    arr = Array()
    arr.add(1)
    with pytest.raises(ValueError):
        arr.remove(99)


def test_print_empty(capsys):
    Array().print()
    assert capsys.readouterr().out.strip() == "[]"


def test_print_values(capsys):
    arr = Array()
    for v in [1, 2, 3]:
        arr.add(v)
    arr.print()
    assert capsys.readouterr().out.strip() == "[1, 2, 3]"