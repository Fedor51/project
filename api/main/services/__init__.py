from .mod import *
from .generate import *
from .quadratic import *


def get(complexity: int):
    # complexity is 0(easy), 1(middle) or 2(hard). 
    
    # easy
    if not complexity: 
        f = choice([add, substract, multiplicate, division])
        return f() 
    # middle
    elif complexity == 1:
        f = choice([math_gen_complexity1, exp, math_gen_complexity2_1, math_gen_equation0, linear_equation, root])
        return f()
    # hard 
    else: 
        f = choice([generate_quadratic_equation, math_gen_equation1])
        return f()
    