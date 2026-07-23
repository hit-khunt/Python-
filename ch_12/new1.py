from typing import List, Tuple, Dict, Union

number: List[int] = [1,2,3,4,5]

person: Tuple[str, int] = ("Hit", 19)

scores: Dict[str, int] = {"Hit":19, "Het":19}

username: Union[str, int] = "ID1234"
username = 432345

n : int = 5

name: str = "Hit"

def sum(a: int, b: int) -> int:
    return a+b

print(sum(3,5))