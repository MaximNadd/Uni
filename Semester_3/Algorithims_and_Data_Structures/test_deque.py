# test_deque.py
import pytest
from deque import Deque


def test_append_right_and_pop_right():
    dq = Deque(3)
    dq.append_right(1)
    dq.append_right(2)
    assert dq.pop_right() == 2
    assert dq.pop_right() == 1


def test_append_left_and_pop_left():
    dq = Deque(3)
    dq.append_left(1)
    dq.append_left(2)
    assert dq.pop_left() == 2
    assert dq.pop_left() == 1


def test_both_ends_and_repr():
    dq = Deque(3)
    dq.append_left(10)
    dq.append_left(20)
    dq.append_right(5)
    assert repr(dq) == "Deque([20, 10, 5])"

    dq.pop_right()   # removes 5
    dq.pop_left()    # removes 20
    assert repr(dq) == "Deque([10])"


def test_print_ele(capsys):
    dq = Deque(3)
    dq.append_right(1)
    dq.append_right(2)
    assert dq.print_ele(1) == "2"

    dq.print_ele(5)  # out of range
    captured = capsys.readouterr()
    assert "INDEX OUT OF RANGE" in captured.out


def test_overflow(capsys):
    dq = Deque(1)
    dq.append_right(1)
    dq.append_right(2)   # should overflow
    captured = capsys.readouterr()
    assert "ERROR OVERFLOW" in captured.out


def test_empty_pop(capsys):
    dq = Deque(2)
    assert dq.pop_left() is None
    captured = capsys.readouterr()
    assert "DEQUE EMPTY" in captured.out