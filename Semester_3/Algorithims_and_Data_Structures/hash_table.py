"""A hash table implemented with separate chaining (buckets of key/value pairs).

Operations are O(1) average / O(n) worst case (all keys colliding).
"""

from __future__ import annotations

from typing import Any, Iterator


class HashTable:
    """Hash table with separate chaining and automatic resizing."""

    DEFAULT_CAPACITY = 8
    MIN_CAPACITY = 8
    LOAD_FACTOR = 0.75  # resize when size / capacity exceeds this

    def __init__(self, capacity: int = DEFAULT_CAPACITY):
        if not isinstance(capacity, int) or capacity < 1:
            raise ValueError("capacity must be a positive integer")
        self._capacity = self._next_power_of_two(max(capacity, self.MIN_CAPACITY))
        self._buckets: list[list[tuple[Any, Any]]] = [[] for _ in range(self._capacity)]
        self._size = 0
        # number of inserts that landed in an already-occupied bucket
        # (recomputed from scratch on every resize)
        self._collisions = 0

    # ------------------------------------------------------------------ utils
    @staticmethod
    def _next_power_of_two(n: int) -> int:
        return 1 << (n - 1).bit_length()

    def _bucket(self, key: Any) -> list[tuple[Any, Any]]:
        # `hash` raises TypeError for unhashable keys — that is the desired behaviour
        return self._buckets[hash(key) % self._capacity]

    def _resize(self, new_capacity: int) -> None:
        old_buckets = self._buckets
        self._capacity = new_capacity
        self._buckets = [[] for _ in range(new_capacity)]
        self._size = 0
        self._collisions = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self[key] = value

    # ------------------------------------------------------------- properties
    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def collisions(self) -> int:
        """How many inserts hit an occupied bucket (approximate, reset on resize)."""
        return self._collisions

    @property
    def load_factor(self) -> float:
        return self._size / self._capacity

    # ------------------------------------------------------- mapping protocol
    def __setitem__(self, key: Any, value: Any) -> None:
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # overwrite, no collision
                return
        if bucket:
            self._collisions += 1
        bucket.append((key, value))
        self._size += 1
        if self.load_factor > self.LOAD_FACTOR:
            self._resize(self._capacity * 2)

    def __getitem__(self, key: Any) -> Any:
        for k, v in self._bucket(key):
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key: Any) -> None:
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(key)

    def __contains__(self, key: Any) -> bool:
        return any(k == key for k, _ in self._bucket(key))

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        return self.keys()

    # ------------------------------------------------------------ dict-likes
    def get(self, key: Any, default: Any = None) -> Any:
        for k, v in self._bucket(key):
            if k == key:
                return v
        return default

    def keys(self) -> Iterator[Any]:
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k

    def values(self) -> Iterator[Any]:
        for bucket in self._buckets:
            for _, v in bucket:
                yield v

    def items(self) -> Iterator[tuple[Any, Any]]:
        for bucket in self._buckets:
            yield from bucket

    def clear(self) -> None:
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        self._collisions = 0

    def __repr__(self) -> str:
        return f"HashTable(capacity={self._capacity}, size={self._size}, collisions={self._collisions})"