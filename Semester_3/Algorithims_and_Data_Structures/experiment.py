# experiment.py
"""Time-complexity experiment: Deque vs Array vs LinkedList.

Sizes:   10_000, 100_000, 1_000_000
Measures: build, append, remove-from-front, remove-from-middle, iterate.

Look for these patterns:
  * O(1)   -> time roughly constant across n
  * O(n)   -> time roughly doubles when n doubles  (×10 when n ×10)
  * O(n²)  -> time roughly quadruples when n doubles (we avoid these)
"""

import time

from deque import Deque               # your Deque class
from linked_list import LinkedList, Node
from aarray import Array


SIZES = [10_000, 100_000, 1_000_000]
TRIALS = 5


# ----------------------------------------------------------------- helpers
def build_linked_list(values):
    """Build a LinkedList in O(n) time (instead of O(n²) via .add)."""
    ll = LinkedList()
    if not values:
        return ll
    ll.head = Node(values[0])
    cur = ll.head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return ll


def traverse_linked_list(ll):
    """Walk every node once (like .print, but without the output)."""
    out = []
    cur = ll.head
    while cur is not None:
        out.append(cur.value)
        cur = cur.next
    return out


def time_once(fn):
    start = time.perf_counter()
    fn()
    return time.perf_counter() - start


def fmt(seconds):
    if seconds < 1e-3:
        return f"{seconds * 1e6:10.2f} µs"
    if seconds < 1:
        return f"{seconds * 1e3:10.2f} ms"
    return f"{seconds:10.4f} s "


def header(title):
    print(f"\n{title}")
    print("-" * 72)


# ------------------------------------------------------------- benchmark
def benchmark(n):
    print()
    print("=" * 72)
    print(f"  n = {n:,}")
    print("=" * 72)
    values = list(range(n))

    # -- [1] Build the whole structure (n operations) -----------------
    header("[1] Build structure with n elements")

    d = Deque(n)
    start = time.perf_counter()
    for v in values:
        d.append_right(v)
    print(f"    Deque.append_right    x {n:>9,} : {fmt(time.perf_counter() - start)}")

    a = Array()
    start = time.perf_counter()
    for v in values:
        a.add(v)
    print(f"    Array.add             x {n:>9,} : {fmt(time.perf_counter() - start)}")

    start = time.perf_counter()
    build_linked_list(values)
    print(f"    LinkedList O(n) build x {n:>9,} : {fmt(time.perf_counter() - start)}")
    print("      (LinkedList.add is O(n) each — building via .add would be O(n²))")

    # -- [2] Append one element ---------------------------------------
    header(f"[2] Append one element (avg of {TRIALS})")

    d = Deque(n + TRIALS + 1)
    for v in values:
        d.append_right(v)
    times = [time_once(lambda: d.append_right(0)) for _ in range(TRIALS)]
    print(f"    Deque.append_right       : {fmt(sum(times) / TRIALS)}")

    a = Array()
    for v in values:
        a.add(v)
    times = [time_once(lambda: a.add(0)) for _ in range(TRIALS)]
    print(f"    Array.add                : {fmt(sum(times) / TRIALS)}")

    ll = build_linked_list(values)
    times = [time_once(lambda: ll.add(0)) for _ in range(TRIALS)]
    print(f"    LinkedList.add           : {fmt(sum(times) / TRIALS)}")

    # -- [3] Remove from the FRONT ------------------------------------
    header(f"[3] Remove first element (avg of {TRIALS})")

    d = Deque(n)
    for v in values:
        d.append_right(v)
    times = [time_once(lambda: d.pop_left()) for _ in range(TRIALS)]
    print(f"    Deque.pop_left           : {fmt(sum(times) / TRIALS)}")

    a = Array()
    for v in values:
        a.add(v)
    times = [time_once(lambda i=i: a.remove(i)) for i in range(TRIALS)]
    print(f"    Array.remove(0..)        : {fmt(sum(times) / TRIALS)}")

    ll = build_linked_list(values)
    times = [time_once(lambda i=i: ll.remove(i)) for i in range(TRIALS)]
    print(f"    LinkedList.remove(0..)   : {fmt(sum(times) / TRIALS)}")

    # -- [4] Remove from the MIDDLE -----------------------------------
    header(f"[4] Remove middle element (avg of {TRIALS})")

    mid = n // 2

    a = Array()
    for v in values:
        a.add(v)
    times = [time_once(lambda i=i: a.remove(mid + i)) for i in range(TRIALS)]
    print(f"    Array.remove(n/2..)      : {fmt(sum(times) / TRIALS)}")

    ll = build_linked_list(values)
    times = [time_once(lambda i=i: ll.remove(mid + i)) for i in range(TRIALS)]
    print(f"    LinkedList.remove(n/2..) : {fmt(sum(times) / TRIALS)}")

    # -- [5] Iterate / print the whole structure ----------------------
    header("[5] Print / iterate whole structure (1 trial)")

    d = Deque(n)
    for v in values:
        d.append_right(v)
    print(f"    Deque repr               : {fmt(time_once(lambda: repr(d)))}")

    a = Array()
    for v in values:
        a.add(v)
    print(f"    Array str(data)          : {fmt(time_once(lambda: str(a.data)))}")

    ll = build_linked_list(values)
    print(f"    LinkedList traverse      : {fmt(time_once(lambda: traverse_linked_list(ll)))}")


def main():
    print("Time-complexity experiment: Deque vs Array vs LinkedList")
    print(f"Sizes : {', '.join(f'{n:,}' for n in SIZES)}")
    print(f"Trials: {TRIALS}")

    for n in SIZES:
        benchmark(n)


if __name__ == "__main__":
    main()