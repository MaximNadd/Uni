"""LRU cache: dict for O(1) lookup + doubly linked list for O(1) recency updates.
"""

from __future__ import annotations

from functools import wraps
from typing import Any, Callable, Iterator


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key: Any = None, value: Any = None):
        self.key = key
        self.value = value
        self.prev: "_Node | None" = None
        self.next: "_Node | None" = None


class LRUCache:
    def __init__(self, capacity: int):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self._capacity = capacity
        self._map: dict[Any, _Node] = {}
        self._head = _Node()  # sentinel, MRU side
        self._tail = _Node()  # sentinel, LRU side
        self._head.next = self._tail
        self._tail.prev = self._head

    # ------------------------------------------------------------- internals
    def _link_front(self, node: _Node) -> None:
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node

    def _unlink(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def _bump(self, node: _Node) -> None:
        self._unlink(node)
        self._link_front(node)

    # ------------------------------------------------------------ public API
    def get(self, key: Any, default: Any = None) -> Any:
        node = self._map.get(key)
        if node is None:
            return default
        self._bump(node)
        return node.value

    def peek(self, key: Any, default: Any = None) -> Any:
        """Read without changing recency."""
        node = self._map.get(key)
        return default if node is None else node.value

    def put(self, key: Any, value: Any) -> None:
        node = self._map.get(key)
        if node is not None:
            node.value = value
            self._bump(node)
            return
        if len(self._map) == self._capacity:  # evict LRU
            lru = self._tail.prev
            self._unlink(lru)
            del self._map[lru.key]
        node = _Node(key, value)
        self._link_front(node)
        self._map[key] = node

    def clear(self) -> None:
        self._map.clear()
        self._head.next = self._tail
        self._tail.prev = self._head

    def keys(self) -> Iterator[Any]:
        """Keys from most recently used to least recently used."""
        node = self._head.next
        while node is not self._tail:
            yield node.key
            node = node.next

    def items(self) -> Iterator[tuple[Any, Any]]:
        node = self._head.next
        while node is not self._tail:
            yield node.key, node.value
            node = node.next

    def __contains__(self, key: Any) -> bool:  # does NOT change recency
        return key in self._map

    def __len__(self) -> int:
        return len(self._map)

    def __repr__(self) -> str:
        return f"LRUCache(capacity={self._capacity}, items={list(self.items())})"


def lru_cache(maxsize: int = 128) -> Callable:
    """Decorator flavour: memoize a function with an LRU cache."""

    def decorator(func: Callable) -> Callable:
        cache: LRUCache = LRUCache(maxsize)

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            sentinel = object()
            hit = cache.get(key, sentinel)
            if hit is not sentinel:
                return hit
            result = func(*args, **kwargs)
            cache.put(key, result)
            return result

        wrapper.cache = cache          # type: ignore[attr-defined]
        wrapper.cache_clear = cache.clear  # type: ignore[attr-defined]
        return wrapper

    return decorator