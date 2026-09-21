# tests/test_linked_list.py
import pytest

from linked_list import LinkedList


def test_add_to_empty():
    ll = LinkedList()
    ll.add(1)
    assert ll.head.value == 1


def test_add_multiple_keeps_order():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 3


def test_remove_head():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.remove(1)
    assert ll.head.value == 2


def test_remove_middle():
    ll = LinkedList()
    for v in [1, 2, 3]:
        ll.add(v)
    ll.remove(2)
    assert ll.head.value == 1
    assert ll.head.next.value == 3


def test_remove_tail():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.remove(2)
    assert ll.head.next is None


def test_remove_missing_raises():
    ll = LinkedList()
    ll.add(1)
    with pytest.raises(ValueError):
        ll.remove(99)


def test_print_empty(capsys):
    LinkedList().print()
    assert capsys.readouterr().out.strip() == "(empty)"


def test_print_values(capsys):
    ll = LinkedList()
    for v in [1, 2, 3]:
        ll.add(v)
    ll.print()
    assert capsys.readouterr().out.strip() == "1 -> 2 -> 3"