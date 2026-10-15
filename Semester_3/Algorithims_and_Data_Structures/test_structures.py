import pytest
from structures import AVLTree, bubble_sort, quick_sort


def test_avl_insert_and_inorder():
    tree = AVLTree()
    for x in [10, 20, 30, 40, 50, 25]:
        tree.insert(x)

    assert tree.inorder() == [10, 20, 25, 30, 40, 50]


def test_avl_contains():
    tree = AVLTree()
    for x in [5, 3, 8, 1, 4]:
        tree.insert(x)

    assert tree.contains(4) is True
    assert tree.contains(99) is False


def test_avl_balances():
    tree = AVLTree()
    for x in [10, 20, 30]:
        tree.insert(x)

    assert tree.root.key == 20
    assert tree.root.left.key == 10
    assert tree.root.right.key == 30
    assert tree.height() == 2


@pytest.mark.parametrize("sort_fn", [bubble_sort, quick_sort])
def test_sort_empty(sort_fn):
    assert sort_fn([]) == []


@pytest.mark.parametrize("sort_fn", [bubble_sort, quick_sort])
def test_sort_basic(sort_fn):
    assert sort_fn([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]


@pytest.mark.parametrize("sort_fn", [bubble_sort, quick_sort])
def test_sort_duplicates(sort_fn):
    assert sort_fn([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


@pytest.mark.parametrize("sort_fn", [bubble_sort, quick_sort])
def test_sort_does_not_modify_input(sort_fn):
    data = [3, 1, 2]
    sort_fn(data)
    assert data == [3, 1, 2]