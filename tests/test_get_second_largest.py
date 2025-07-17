def test_get_second_largest():
    from get_second_largest import get_second_largest
    assert get_second_largest([12, 35, 1, 10, 34, 1]) == 34
    assert get_second_largest([1, 1, 1]) == -1
