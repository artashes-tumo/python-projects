import math

def format_equation(a, b, c):
    eq = ""

    # a 
    if a == 1:
        eq += "x^2"
    elif a == -1:
        eq += "-x^2"
    else:
        eq += f"{a}x^2"

    # b 
    if b > 0:
        eq += f" + {b}x"
    elif b < 0:
        eq += f" - {abs(b)}x"

    # c 
    if c > 0:
        eq += f" + {c}"
    elif c < 0:
        eq += f" - {abs(c)}"

    eq += " = 0"
    return eq


def solve_quadratic(a, b, c):
    if a == 0:
        return "Not a quadratic equation"

    print("Equation:", format_equation(a, b, c))

    d = b**2 - 4*a*c

    # d<0
    if d < 0:
        return "No real roots"

    # d=0
    elif d == 0:
        x = -b / (2*a)
        return f"One real root: {x}"
    
    # d>0
    else:
            sqrt_d = math.isqrt(d)
            x1 = (-b + sqrt_d) / (2*a)
            x2 = (-b - sqrt_d) / (2*a)
            return f"Two real roots: {x1} and {x2}"
