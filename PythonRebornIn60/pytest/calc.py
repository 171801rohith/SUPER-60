def add(a: int, b:int):
    return a + b

def sub(a: int, b:int):
    return a - b

def mul(a: int, b:int):
    return a * b

def div(a: int, b:int):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b
    
def to_uppercase(s: str) -> str:
    return s.upper()