from lists.linked_list import LinkedList


def test_add_tail():
    linked_list: LinkedList[int] = LinkedList()
    linked_list.add_tail(5).add_tail(7)

    assert list(linked_list) == [5, 7]
