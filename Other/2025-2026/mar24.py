import random

a = random.randint(1, 15)
b = random.randint(1, 15)
def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    return False

def oneline_makes10(a, b):
    return a == 10 or b == 10 or a + b == 10


print(f"The number a is {a}, and the number b is {b}")
print(oneline_makes10(a, b))