from .mod import *
from .generate import *
from .quadratic import *


def get(complexity: int):
    # complexity is 0(easy), 1(middle) or 2(hard). 
    
    # easy
    if not complexity:  
        problem, answer = math_gen_complexity0()
        return problem, answer
    # middle
    elif complexity == 1:
        f = choice([math_gen_complexity1, math_gen_complexity2, math_gen_complexity2_1, math_gen_equation0])
        return f()
    # hard
    else: 
        problem, answer = generate_quadratic_equation()
        return problem, answer
    