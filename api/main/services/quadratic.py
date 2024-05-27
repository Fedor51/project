from .mod import *


# quadratic_equation
def generate_quadratic_equation():
    ran = [i for i in range(-10, 0)] + [j for j in range(1, 11)]
    ran1 = [i for i in range(-20, 0)] + [j for j in range(1, 21)]
    while True:
        a = choice(ran)
        b = choice(ran1)
        c = choice(ran1)

        if choice([0, 1]):
            equation = f"{a}x^2 {'+' if b >= 0 else ''} {b}x {'+' if c >= 0 else ''} {c} = 0"
            D = (b**2) - (4*a*c)
            if D < 0:
                continue
            elif D == 0:
                # answer = ref((-b) / (2*a))
                continue
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
            return equation, answer 
        else:
            equation = f"{a}x^2 {'+' if b >= 0 else ''} {b}x = {c}"
            c = -c
            D = (b**2) - (4*a*c)
            if D < 0:
                continue
            elif D == 0:
                # answer = ref((-b) / (2*a))
                continue
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
            return equation, answer 