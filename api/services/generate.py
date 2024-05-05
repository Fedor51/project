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
        problem = [str(randint(0, 10)) for num in range(numbers_count)]

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

## Solving 

def solve_eq(equasion: str):
    x = None
    return x

def solve_problem(problem: str):
    answer = eval(problem)
    return answer 

