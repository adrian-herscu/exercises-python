from dataclasses import dataclass
from typing import Iterable, Iterator, Self, Set, Type


class LinkedList[T]:
    @dataclass
    class Node:
        value: T
        next: 'LinkedList.Node | None' = None

    head: 'Node | None'
    tail: 'Node | None'

    def __init__(self) -> None:
        self.tail = self.head = None

    @classmethod
    def from_iterable(
            cls: Type['LinkedList[T]'],
            values: Iterable[T]) -> 'LinkedList[T]':
        linked_list: LinkedList[T] = cls()
        for v in values:
            linked_list.add_tail(v)
        return linked_list

    @property
    def is_empty(self) -> bool:
        return self.tail is None and self.head is None

    def add_tail(self, value: T) -> Self:
        new_tail = self.Node(value)
        if self.is_empty:
            self.head = self.tail = new_tail
        else:
            self.tail.next = new_tail  # type: ignore
            self.tail = new_tail
        return self

    def delete(self, value: T, first_only: bool = False) -> Self:
        previous = None
        current = self.head

        while current:
            if current.value == value:
                next_node = current.next  # Save before unlinking

                if previous is None:
                    self.head = next_node
                else:
                    previous.next = next_node

                if current is self.tail:
                    self.tail = previous

                current = next_node  # Move forward after deletion

                if first_only:
                    break
            else:
                previous, current = current, current.next

        return self

    def nth_to_last(self, n: int) -> T | None:
        fast = slow = self.head

        for _ in range(n):
            if fast is None:
                return None  # List is shorter than n
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next  # type: ignore

        return slow.value if slow else None

    def dedup(self) -> Self:
        seen: Set[T] = set()
        previous = None
        current = self.head

        while current:
            if current.value in seen:
                if previous:
                    previous.next = current.next
                    if current is self.tail:
                        self.tail = previous
                current = current.next
            else:
                seen.add(current.value)
                previous = current
                current = current.next

        return self

    @property
    def nodes(self) -> Iterator[tuple['Node | None', 'Node']]:
        previous = None
        current = self.head
        while current:
            yield (previous, current)
            previous, current = current, current.next

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current:
            yield current.value
            current = current.next
