from dataclasses import dataclass
from typing import Iterator, Self


class LinkedList[T]:
    @dataclass
    class Node:
        value: T
        next: 'LinkedList[T].Node | None' = None

    head: Node | None = None
    tail: Node | None = None

    def add_tail(self, value: T) -> Self:
        new_tail = self.Node(value)
        if self.tail is None:  # and self.head is None breaks type checking for self.tail.next below
            self.head = self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        return self

    # def delete_first[T](self, value: T):

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
