def test_max_profit():
    from max_profit import max_profit
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2]) == 1
    assert max_profit([2, 1]) == 0
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4
    assert max_profit([]) == 0
    assert max_profit([10]) == 0
