from dataclasses import dataclass
from typing import Iterator, Self


class LinkedList[T]:
    @dataclass
    class Node:
        data: T
        next: 'LinkedList[T].Node | None' = None

    head: Node | None = None
    tail: Node | None = None

    def add_tail(self, value: T) -> Self:
        tail = self.Node(value)
        if self.tail is None:
            self.head = self.tail = tail
        else:
            self.tail.next = tail
            self.tail = tail
        return self

    # def delete_first[T](self, value: T):

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
