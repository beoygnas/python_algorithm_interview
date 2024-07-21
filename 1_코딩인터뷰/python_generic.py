from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def are_equal(a: T, b: U) -> bool :
    return a == b

print(are_equal(10, 10.0))
    

