def test_item_in_list():
    assert 1 in [1, 2, 3, 4] 

def test_item_in_list_fail():
    assert 1 in [2, 3, 4] 

def test_item_not_in_list():
    assert not 1 in [2, 3, 5]

def test_item_not_in_list_fail():
    assert not 1 in [1, 2, 3, 5]
