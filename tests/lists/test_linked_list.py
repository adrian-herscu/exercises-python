from lists.linked_list import LinkedList


def test_add_tail():
    linked_list: LinkedList[int] = LinkedList()
    linked_list.add(5).add(7)

    assert list(linked_list) == [5, 7]


def test_delete_first_only():
    linked_list: LinkedList[int] = LinkedList()
    (linked_list
        .add(1)
        .add(2)
        .add(2)
        .add(3)
        .delete(2, first_only=True))

    assert list(linked_list) == [1, 2, 3]


def test_delete():
    linked_list: LinkedList[int] = LinkedList()
    (linked_list
        .add(1)
        .add(2)
        .add(2)
        .add(3)
        .delete(2))

    assert list(linked_list) == [1, 3]
