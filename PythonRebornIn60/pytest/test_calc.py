import calc

def test_add():
    assert 5 + 9 == calc.add(5, 9)

def test_sub():
    assert 5 - 9 == calc.sub(5, 9)

def test_mul():
    assert 5 * 9 == calc.mul(5, 9)

def test_div():
    assert 5 / 9 == calc.div(5, 9)

def test_upper1():
    assert "ROHITH" != calc.to_uppercase("rohith")

def test_upper2():
    assert "ROHITH" == calc.to_uppercase("rohith")

def test_upper3():
    assert "ROHITH 171801" == calc.to_uppercase("rohith 171801")

def test_special_char():
    assert "@#$!()$#^"  == calc.to_uppercase("@#$!()$#^")
