from lists.linked_list import LinkedList


def test_empty():
    linked_list: LinkedList[int] = LinkedList()
    assert linked_list.is_empty

    linked_list.delete(777)
    assert linked_list.is_empty


def test_add_tail():
    linked_list: LinkedList[int] = LinkedList()
    linked_list.add_tail(5).add_tail(7)

    assert list(linked_list) == [5, 7]


def test_delete_first_only():
    linked_list: LinkedList[int] = LinkedList()
    (linked_list
        .add_tail(1)
        .add_tail(2)
        .add_tail(2)
        .add_tail(3)
        .delete(2, first_only=True))

    assert list(linked_list) == [1, 2, 3]


def test_delete():
    linked_list: LinkedList[int] = LinkedList()
    (linked_list
        .add_tail(1)
        .add_tail(2)
        .add_tail(2)
        .add_tail(3)
        .delete(2))

    assert list(linked_list) == [1, 3]


def test_dedup():
    linked_list = LinkedList[int].from_iterable([1, 2, 2, 3])
    assert list(linked_list.dedup()) == [1, 2, 3]


def test_nth_to_last():
    linked_list: LinkedList[int] = LinkedList[int].from_iterable([1, 2, 3, 4])
    assert linked_list.nth_to_last(1) == 4
    assert linked_list.nth_to_last(2) == 3
    assert linked_list.nth_to_last(3) == 2
    assert linked_list.nth_to_last(4) == 1
    assert linked_list.nth_to_last(5) is None
