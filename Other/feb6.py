# countries_with_capitals = {
#     "India": "New Delhi",
#     "USA": "Washington, D.C.",
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "Australia": "Canberra"
# }

# for country, capital in countries_with_capitals.items():
#     print(f"The capital of {country} is {capital}.")


# def calculate_area_of_circle(radius):
#     import math
#     area = math.pi * (radius ** 2)
#     return area
# radius = 5
# area = calculate_area_of_circle(radius)
# print(f"The area of a circle with radius {radius} is {area:.2f}.")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:   print(f"{number} is not a prime number.")