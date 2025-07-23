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
        new_node = self.Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        return self

    # def delete_first[T](self, value: T):

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
