import random


## Generating 

def math_gen_complexity_easy():
    for _ in range(1):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(['+', '-', '*', '/'])
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        else:
            result = a // b
        return f'{a}{operator}{b} = {result}'

def math_gen_complexity_middle(eq:bool):
    if not eq:
        operator = "^"
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        result = a
        for _ in range(b-1):
            result = result * a
        return f'{a}{operator}{b} = {result}'
    # Equation
    else:
        operator = random.choice(['+', '-', '*', '/'])
        if operator == '+':
            a = random.randint(1, 10)
            b = random.randint(10, 30)
            equation = random.choice(["a + x = b","x + a = b"])
            if equation == "a + x = b":
                return f'{a} {operator} x = {b}'
            else:
                return f'x {operator} {a} = {b}'
        if operator == '-':
            a = random.randint(20, 40)
            b = random.randint(0, 20)
            equation = random.choice(["a - x = b","x - a = b"])
            if equation == "a - x = b":
                return f'{a} {operator} x = {b}'
            else:
                return f'x {operator} {a} = {b}'
        if operator == '*':
            a = random.randint(1, 10)
            b = random.randint(10, 30)
            return f'{a}x = {b}'
        if operator == '/':
            a = random.randint(20, 50)
            b = random.randint(1, 12)
            return f'{a} / x = {b}'

## Solving 

def solve_eq(equation: str):
    x = None
    return x

def solve_problem(problem: str):
    answer = eval(problem)
    return answer 

