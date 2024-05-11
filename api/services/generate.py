from random import randint, choice

# refactoring answer
def ref(x: float|int):
    if x.is_integer():
        return int(x)
    return round(x, 2)

## Generating 
operators = ['+', '-', '*', '/'] 

def math_gen_complexity0(operators=operators):
    a = randint(1, 10)
    b = randint(1, 10)
    operator = choice(operators)
    problem = f"{a} {operator} {b}"
    answer = ref(eval(problem))
    return problem, answer

def math_gen_complexity1(limit: int = 10, operators=operators):
    while True:
        numbers_count = randint(4, limit)
        problem = [str(randint(1, 10)) for num in range(numbers_count)]

        for i in range(1, len(problem)*2 - 1, 2):
            problem.insert(i, choice(operators))
        problem = " ".join(problem)

        try: answer = ref(eval(problem))
        except ZeroDivisionError: continue
        if answer > 200 or answer < -200:
            continue
        return problem, answer
    
def math_gen_complexity2():
    operator = "**"
    a = randint(1, 5)
    b = randint(1, 5)
    problem = f'{a}{operator}{b}'
    answer = ref(eval(problem))
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
        return f'{a}x = {b}', ref(b/a)
    
    if operator == '/':
        a = randint(20, 50)
        b = randint(1, 12)
        equation = choice(["a / x = b","x / a = b"])
        if equation == "a / x = b":
            return f'{a} / x = {b}', ref(a/b)
        else:
            return  f'x / {a} = {b}', ref(a*b)

# quadratic_equation
def generate_quadratic_equation():
    ran = [i for i in range(-10, 0)] + [j for j in range(1, 11)]
    ran1 = [i for i in range(-20, 0)] + [j for j in range(1, 21)]
    while True:
        a = choice(ran)
        b = choice(ran1)
        c = choice(ran1)
        equation = f"{a}x^2 {'+' if b >= 0 else ''} {b}x {'+' if c >= 0 else ''} {c} = 0"
        D = (b**2) - (4*a*c)
        if D < 0:
            continue
        elif D == 0:
            answer = ref((-b) / (2*a))
        else:
            x1: float = (-b + (D**0.5)) / (2*a)
            x2: float = (-b - (D**0.5)) / (2*a)
            i = x1.as_integer_ratio()[0]
            j = x2.as_integer_ratio()[0]
            if i > 1e3 or i < 1e-3:
                continue
            if j > 1e3 or j < 1e-3:
                continue
            answer = [ref(x1), ref(x2)]
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
    