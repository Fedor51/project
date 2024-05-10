from random import randint, choice
## Generating 
operators = ['+', '-', '*', '/'] 

def math_gen_complexity0(operators=operators):
    a = randint(1, 10)
    b = randint(1, 10)
    operator = choice(operators)
    problem = f"{a} {operator} {b}"
    answer = round(eval(problem), 2)
    return problem, answer

def math_gen_complexity1(limit: int = 10, operators=operators):
    while True:
        numbers_count = randint(4, limit)
        problem = [str(randint(1, 10)) for num in range(numbers_count)]

        for i in range(1, len(problem)*2 - 1, 2):
            problem.insert(i, choice(operators))
        problem = " ".join(problem)

        try: answer = round(eval(problem), 2)
        except ZeroDivisionError: continue
        if answer > 200 or answer < -200:
            continue
        return problem, answer
    
def math_gen_complexity2():
    operator = "**"
    a = randint(1, 5)
    b = randint(1, 5)
    problem = f'{a}{operator}{b}'
    answer = eval(problem)
    return problem, answer

def math_gen_complexity2_1(operators=['+', '-', '*', '/', '**']): 
    
    # problem1, _ = math_gen_complexity2()
    # problem2, _ = math_gen_complexity1(5)
    # problem = f"{problem1} {choice(operators)} {problem2}"
    # try: answer = round(eval(problem), 2)
    # except ZeroDivisionError: continue
    # if answer > 200 or answer < -200:
    #     continue
    # return problem, answer
    problem, answer = math_gen_complexity1(5, operators)
    return problem, answer
    
# Equation
def math_gen_equation0():
    operator = choice(['+', '-', '*', '/'])
    if operator == '+':
        a = randint(1, 10)
        b = randint(10, 30)
        equation = choice(["a + x = b","x + a = b"])
        if equation == "a + x = b":
            return f'{a} {operator} x = {b}', b - a
        else:
            return f'x {operator} {a} = {b}', b - a
        
    if operator == '-':
        a = randint(20, 40)
        b = randint(0, 20)
        equation = choice(["a - x = b","x - a = b"])
        if equation == "a - x = b":
            return f'{a} {operator} x = {b}', a - b
        else:
            return f'x {operator} {a} = {b}', a + b
        
    if operator == '*':
        a = randint(1, 10)
        b = randint(10, 30)
        return f'{a}x = {b}', round(b/a, 2)
    
    if operator == '/':
        a = randint(20, 50)
        b = randint(1, 12)
        equation = choice(["a / x = b","x / a = b"])
        if equation == "a / x = b":
            return f'{a} / x = {b}', round(a/b, 2)
        else:
            return  f'x / {a} = {b}', round(a * b, 2)

# quadratic_equation
def generate_quadratic_equation():
    while True:
        a = randint(1, 10)
        b = randint(-20, 20)
        c = randint(-20, 20)
        s1, s2, s3 = choice(["", "-"]), choice(["+", "-"]), choice(["+", "-"])
        equation = f"{s1}{abs(a) if a != 1 else ''}x^2 {s2} {abs(b)}x {s3} {abs(c)} = 0"
        D = (b**2) - (4*a*c)
        if D < 0:
            continue
        elif D == 0:
            answer = round((-b) / (2*a), 2)
        else:
            x1: float = (-b + (D**0.5)) / (2*a)
            x2: float = (-b - (D**0.5)) / (2*a)
            i = x1.as_integer_ratio()[0]
            j = x2.as_integer_ratio()[0]
            if i > 1e3 or i < 1e-3:
                continue
            if j > 1e3 or j < 1e-3:
                continue
            answer = [x1, x2]
        if a == 1:
            # equation = equation[]
            pass
        return equation, answer 



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
    