import pytest

from hash_table import HashTable


class FixedHashKey:
    """Key whose hash is constant -> forces all keys into the same bucket."""

    __slots__ = ("name",)

    def __init__(self, name: str):
        self.name = name

    def __hash__(self) -> int:
        return 42

    def __eq__(self, other) -> bool:
        return isinstance(other, FixedHashKey) and other.name == self.name

    def __repr__(self) -> str:
        return f"FixedHashKey({self.name!r})"


# ------------------------------------------------------------------ creation
def test_new_table_is_empty():
    t = HashTable()
    assert len(t) == 0
    assert list(t) == []
    assert t.capacity >= HashTable.MIN_CAPACITY
    assert t.load_factor == 0.0


@pytest.mark.parametrize("capacity", [0, -1, -100])
def test_invalid_capacity_raises(capacity):
    with pytest.raises(ValueError):
        HashTable(capacity)


@pytest.mark.parametrize("requested, expected", [(1, 8), (8, 8), (9, 16), (17, 32)])
def test_capacity_rounded_to_power_of_two(requested, expected):
    assert HashTable(requested).capacity == expected


# ------------------------------------------------------------- basic mapping
def test_set_get_roundtrip():
    t = HashTable()
    t["a"] = 1
    t["b"] = 2
    assert t["a"] == 1
    assert t["b"] == 2
    assert len(t) == 2


def test_missing_key_raises_keyerror():
    t = HashTable()
    with pytest.raises(KeyError):
        _ = t["nope"]


def test_overwrite_does_not_grow():
    t = HashTable()
    t["k"] = 1
    t["k"] = 2
    assert t["k"] == 2
    assert len(t) == 1


def test_get_with_default():
    t = HashTable()
    t["x"] = None
    assert t.get("x", "fallback") is None
    assert t.get("y", "fallback") == "fallback"
    assert t.get("y") is None


def test_contains():
    t = HashTable()
    t["present"] = 1
    assert "present" in t
    assert "absent" not in t


def test_delete():
    t = HashTable()
    t["a"] = 1
    del t["a"]
    assert len(t) == 0
    assert "a" not in t
    with pytest.raises(KeyError):
        del t["a"]


def test_keys_values_items_and_iteration():
    t = HashTable()
    data = {"one": 1, "two": 2, "three": 3}
    for k, v in data.items():
        t[k] = v
    assert sorted(t.keys()) == sorted(data)
    assert sorted(t.values()) == sorted(data.values())
    assert dict(t.items()) == data
    assert sorted(t) == sorted(data)


def test_unhashable_key_raises_typeerror():
    t = HashTable()
    with pytest.raises(TypeError):
        t[[1, 2]] = "list"  # noqa: F601


def test_clear():
    t = HashTable()
    for i in range(5):
        t[i] = i
    t.clear()
    assert len(t) == 0
    assert list(t.items()) == []


# ------------------------------------------------------------------ collisions
def test_colliding_keys_are_all_stored():
    t = HashTable(capacity=32)  # big enough to avoid a resize
    keys = [FixedHashKey(name) for name in "abcde"]
    for i, k in enumerate(keys):
        t[k] = i

    assert len(t) == 5
    assert t.collisions == 4  # first insert is free, the other four collided
    for i, k in enumerate(keys):
        assert t[k] == i
        assert k in t


def test_delete_from_collision_bucket_keeps_others():
    t = HashTable(capacity=32)
    a, b, c = FixedHashKey("a"), FixedHashKey("b"), FixedHashKey("c")
    t[a], t[b], t[c] = 1, 2, 3
    del t[b]
    assert a in t and c in t and b not in t
    assert (t[a], t[c]) == (1, 3)


# --------------------------------------------------------------------- resizing
def test_resize_preserves_everything():
    t = HashTable(capacity=8)
    n = 1000
    for i in range(n):
        t[i] = i * 2
    assert len(t) == n
    assert t.capacity > 8
    assert t.load_factor <= HashTable.LOAD_FACTOR
    for i in range(n):
        assert t[i] == i * 2
    assert sorted(t) == list(range(n))


def test_resize_with_colliding_keys():
    t = HashTable(capacity=8)
    keys = [FixedHashKey(str(i)) for i in range(50)]  # forces resizes
    for i, k in enumerate(keys):
        t[k] = i
    for i, k in enumerate(keys):
        assert t[k] == i
    assert len(t) == 50