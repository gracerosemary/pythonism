import pytest
from linked_list_iterator import LinkedList

def test_for_in():
    boba = LinkedList(('Black Milk Tea', 'Honey Milk Tea', 'Green Milk Tea'))
    boba_list = []

    for tea in boba:
        boba_list.append(tea)

    assert boba_list == ['Black Milk Tea', 'Honey Milk Tea', 'Green Milk Tea']

def test_list_comp():
    boba = LinkedList(('bmt', 'hmt', 'gmt'))
    upper_boba = [tea.upper() for tea in boba]
    assert upper_boba == ['BMT', 'HMT', 'GMT']

def test_str():
    foods = LinkedList(['fries', 'waffles', 'cereal'])
    assert str(foods) == '[fries] -> [waffles] -> [cereal] -> None'

def test_reversed_list():
    boba = LinkedList(('bmt', 'hmt', 'gmt'))
    reversed_boba = reversed(boba)
    assert reversed_boba == ['gmt', 'hmt', 'bmt']

def test_list_cast():
    boba_list = ['bmt', 'hmt', 'gmt']
    boba = LinkedList(boba_list)
    assert list(boba) == boba_list

def test_equals():
    lla = LinkedList(['bmt', 'hmt', 'gmt'])
    llb = LinkedList(['bmt', 'hmt', 'gmt'])
    assert lla == llb

def test_comparative_operator():
    lla = LinkedList(['bmt', 'hmt', 'gmt', 'tmt'])
    llb = LinkedList(['bmt', 'hmt', 'gmt'])
    assert lla > llb

def test_range():
    num_range = range(1, 20+1)
    nums = LinkedList(num_range)
    assert len(nums) == 20

def test_filter():
    nums = LinkedList(range(1, 10))
    odds = [num for num in nums if num % 2]
    assert odds == [1, 3, 5, 7, 9]

def test_next():
    boba_list = ['bmt', 'hmt', 'gmt']
    iterator = iter(boba_list)
    assert next(iterator) == 'bmt'
    assert next(iterator) == 'hmt'
    assert next(iterator) == 'gmt'

def test_get_item():
    boba = LinkedList(('bmt', 'hmt', 'gmt'))
    assert boba[0] == 'bmt'

def test_get_item_out_of_range():
    boba = LinkedList(('bmt', 'hmt', 'gmt'))
    with pytest.raises(IndexError):
        boba[100]