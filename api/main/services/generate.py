from .mod import *
import mathgenerator as mt

## Generating 
operators = ['+', '-', '*', '/'] 

def math_gen_complexity1(limit: int = 10, operators=operators):
    while True:
        numbers_count = randint(4, limit)
        problem = [str(randint(1, 10)) for num in range(numbers_count)]

        for i in range(1, len(problem)*2 - 1, 2):
            problem.insert(i, choice(operators))
        problem = " ".join(problem)

        try: answer = eval(problem)
        except ZeroDivisionError: continue
        if answer > 200 or answer < -200:
            continue
        return problem, ref(answer)
    

def math_gen_complexity2_1(operators=['+', '-', '*', '/', '**']): 
    problem, answer = math_gen_complexity1(5, operators)
    return problem, ref(answer)
    
# Equation
def math_gen_equation0():
    operator = choice(['+', '-', '*', '/'])
    if operator == '+':
        a = randint(1, 10)
        b = randint(10, 30)
        equation = choice(["a + x = b","x + a = b"])
        if equation == "a + x = b":
            return f'{a} {operator} x = {b}', ref(b - a)
        else:
            return f'x {operator} {a} = {b}', ref(b - a)
        
    if operator == '-':
        a = randint(20, 40)
        b = randint(0, 20)
        equation = choice(["a - x = b","x - a = b"])
        if equation == "a - x = b":
            return f'{a} {operator} x = {b}', ref(a - b)
        else:
            return f'x {operator} {a} = {b}', ref(a + b)
        
    if operator == '*':
        a = randint(1, 10)
        b = randint(10, 30)
        return f'{a}x = {b}', ref(b/a)
    
    if operator == '/':
        a = randint(20, 50)
        b = randint(1, 12)
        equation = choice(["a / x = b","x / a = b"])
        if equation == "a / x = b":
            return f'{a} / x = {b}', ref(a/b)
        else:
            return  f'x / {a} = {b}', ref(a*b)
    
def math_gen_equation1():
    a = choice([i for i in range(-20, 0)] + [j for j in range(1, 21)])
    b = choice([i for i in range(-20, 0)] + [j for j in range(1, 21)])
    
    equation = f"(x {'+' if a > 0 else ''}{a})(x {'+' if b > 0 else ''}{b}) = 0"
    answer = [ref(-a), ref(-b)]
    return equation, answer
    


# using mathgenerator

def linear_equation():
    problem, answer = mt.algebra.basic_algebra(50)
    problem = problem.replace("$", '')
    answer = answer.replace("$", '')
    return problem, ref(eval(answer))

def add():
    problem, answer = mt.basic_math.addition(99, 50)
    problem = problem.replace("$", '')
    problem = problem.replace("=", '')
    answer = answer.replace("$", '')
    return problem, ref(answer)

def substract():
    problem, answer = mt.basic_math.subtraction(200, 170)
    problem = problem.replace("$", '')
    problem = problem.replace("=", '')
    answer = answer.replace("$", '')
    return problem, ref(answer)

def multiplicate():
    problem, answer = mt.basic_math.multiplication(30)
    problem = problem.replace("$", '')
    problem = problem.replace("\cdot", '*')
    answer = answer.replace("$", '')
    return problem, ref(answer)
    
def division():
    if choice([0, 1]):
        problem, answer = mt.basic_math.division(50, 50)
        problem = problem.replace("$", '')
        problem = problem.replace("\div", '/')
        problem = problem.replace("=", '')
        answer = answer.replace("$", '')
        return problem, ref(answer)
    else: 
        problem, answer = mt.basic_math.fraction_to_decimal(99, 99)
        problem = problem.replace("$", '')
        problem = problem.replace("\div", '/')
        problem = problem.replace("=", '')
        answer = answer.replace("$", '')
        return problem, ref(answer)
    
def root():
    problem, answer = mt.basic_math.square_root(1, 16)
    problem = problem.replace("$", '')
    problem = problem.replace("\sqrt{", 'sqrt(')
    problem = problem.replace("}", ')')
    problem = problem.replace("=", '')
    answer = answer.replace("$", '')
    return problem, ref(answer)

def exp():
    problem, answer = mt.basic_math.exponentiation(7, 5)
    problem = problem.replace("$", '')
    problem = problem.replace("=", '')
    problem = problem.replace("^", '**')
    answer = answer.replace("$", '')
    return problem, ref(answer)