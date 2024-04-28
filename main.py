import random

while True:
    numbers_count = random.randint(2, 10)
    problem = [str(random.randint(0, 20)) for num in range(numbers_count)]
    operators = ['+', '-', '*', "/"]

    for i in range(1, len(problem)*2 - 1, 2):
        problem.insert(i, random.choice(operators))
    problem = "".join(problem)


    print(problem)
