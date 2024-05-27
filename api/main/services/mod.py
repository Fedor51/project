from random import randint, choice 

# refactoring answer
def ref(x: float|int|str):
    if type(x) == float and x.is_integer():
        return str(int(x))
    if type(x) == str:
        return x
    return str(round(x, 2))
