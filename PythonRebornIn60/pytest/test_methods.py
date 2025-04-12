import methods
import pytest

# Testing a Simple Functions
def test_add():
    assert 5 + 9 == methods.add(5, 9)

def test_sub():
    assert 5 - 9 == methods.sub(5, 9)

def test_mul():
    assert 5 * 9 == methods.mul(5, 9)

# Testing String Manipulation
def test_upper1():
    assert "ROHITH" != methods.to_uppercase("rohith")

def test_upper2():
    assert "ROHITH" == methods.to_uppercase("rohith")

def test_upper3():
    assert "ROHITH 171801" == methods.to_uppercase("rohith 171801")

def test_special_char():
    assert "@#$!()$#^"  == methods.to_uppercase("@#$!()$#^")

# Testing List Membership
def test_item_in_list():
    assert 1 in [1, 2, 3, 4] 

def test_item_in_list_fail():
    assert 1 in [2, 3, 4] 

# Deliberate Failure
def test_will_fail():
    assert 1 == 2

# Testing for Expected Exceptions
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        methods.div(10, 0)

def test_divide():
    assert 5 == methods.div(10, 2)