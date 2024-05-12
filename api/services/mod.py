from random import randint, choice 

# refactoring answer
def ref(x: float|int):
    if type(x) == float() and x.is_integer():
        return int(x)
    return str(round(x, 2))