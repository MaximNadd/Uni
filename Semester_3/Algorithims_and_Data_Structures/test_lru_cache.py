import random
from collections import OrderedDict

import pytest

from lru_cache import LRUCache, lru_cache


# ------------------------------------------------------------------ creation
@pytest.mark.parametrize("capacity", [0, -1, -50])
def test_invalid_capacity_raises(capacity):
    with pytest.raises(ValueError):
        LRUCache(capacity)


def test_empty_cache():
    c = LRUCache(3)
    assert len(c) == 0
    assert c.get("missing") is None
    assert c.get("missing", "dflt") == "dflt"
    assert "missing" not in c


# ---------------------------------------------------------------- basic usage
def test_put_get():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1
    assert c.get("b") == 2
    assert len(c) == 2


def test_update_existing_key():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("a", 99)
    assert c.get("a") == 99
    assert len(c) == 1


def test_eviction_order():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("c", 3)              # evicts "a" (least recently used)
    assert "a" not in c
    assert c.get("b") == 2
    assert c.get("c") == 3


def test_get_refreshes_recency():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1     # "a" becomes MRU, "b" becomes LRU
    c.put("c", 3)              # evicts "b"
    assert "b" not in c
    assert "a" in c and "c" in c


def test_put_existing_refreshes_recency_and_does_not_evict():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("a", 10)             # refresh "a"; nothing evicted
    assert len(c) == 2
    c.put("c", 3)              # evicts "b"
    assert "b" not in c
    assert c.get("a") == 10


def test_peek_and_contains_do_not_change_order():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)

    assert c.peek("a") == 1
    assert "a" in c            # neither call should promote "a"

    c.put("c", 3)              # so "a" is still the LRU one
    assert "a" not in c
    assert c.get("b") == 2


def test_keys_are_mru_to_lru():
    c = LRUCache(3)
    c.put("a", 1)
    c.put("b", 2)
    c.put("c", 3)
    assert list(c.keys()) == ["c", "b", "a"]
    c.get("a")
    assert list(c.keys()) == ["a", "c", "b"]
    assert list(c.items()) == [("a", 1), ("c", 3), ("b", 2)]


def test_clear():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.clear()
    assert len(c) == 0
    assert list(c.items()) == []
    c.put("x", 9)              # still usable after clear
    assert c.get("x") == 9


def test_capacity_one():
    c = LRUCache(1)
    c.put("a", 1)
    c.put("b", 2)
    assert "a" not in c
    assert c.get("b") == 2
    assert len(c) == 1


# ------------------------------------------------- randomized model-based test
def _model_put(model: OrderedDict, key, value, capacity: int) -> None:
    if key in model:
        model.move_to_end(key)
        model[key] = value
        return
    if len(model) >= capacity:
        model.popitem(last=False)   # drop LRU
    model[key] = value


def test_matches_reference_model():
    rng = random.Random(1234)
    capacity = 7
    cache = LRUCache(capacity)
    model: OrderedDict = OrderedDict()

    for _ in range(3000):
        key = rng.randrange(25)
        if rng.random() < 0.5:
            value = rng.randrange(10_000)
            cache.put(key, value)
            _model_put(model, key, value, capacity)
        else:
            assert cache.get(key) == model.get(key)
            if key in model:                       # get() promotes in both
                model.move_to_end(key)
            assert cache.peek(key) == model.get(key)

        assert len(cache) == len(model)
        assert list(cache.keys()) == list(reversed(model.keys()))
        assert dict(cache.items()) == dict(model)


# ------------------------------------------------------------------ decorator
def test_decorator_caches_results():
    calls = []

    @lru_cache(maxsize=2)
    def square(x: int) -> int:
        calls.append(x)
        return x * x

    assert square(3) == 9
    assert square(3) == 9
    assert calls == [3]


def test_decorator_evicts_and_supports_kwargs():
    calls = []

    @lru_cache(maxsize=2)
    def add(a: int, b: int = 0) -> int:
        calls.append((a, b))
        return a + b

    assert add(1, b=2) == 3
    assert add(1, b=2) == 3          # cache hit, kwargs order-independent
    assert add(3) == 3
    assert add(4) == 4               # evicts the oldest entry (1, b=2)
    assert add(1, b=2) == 3          # recomputed
    assert calls == [(1, 2), (3, 0), (4, 0), (1, 2)]