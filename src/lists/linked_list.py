from dataclasses import dataclass
from typing import Iterator, Self


class LinkedList[T]:
    @dataclass
    class Node:
        value: T
        next: 'LinkedList[T].Node | None' = None

    head: Node | None = None
    tail: Node | None = None

    @property
    def is_empty(self) -> bool:
        return self.tail is None and self.head is None

    def add(self, value: T) -> Self:
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

    @property
    def _nodes(self) -> Iterator[tuple[Node | None, Node]]:
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
