# 8-9
# def great_magicians(magicians):
#     for magician in magicians:
#         print(f"The Great {magician}")

# # 8-10
# def make_great(magicians):
#     for i in range(len(magicians)):
#         magicians[i] = "The Great " + magicians[i]
#     return magicians

# # 8-11
# def make_great(magicians):
#     great_magicians = []
#     for magician in magicians:
#         great_magicians.append("The Great " + magician)
#     return great_magicians

# # 8-12
# def sandwich(*ingredients):
#     while True: 
#         print("Your sandwich includes the following ingredients:")
#         for ingredient in ingredients:
#             print(f"- {ingredient}")
#         more = input("Would you like to add more ingredients? (y/n): ").strip().lower()
#         if more == 'y':
#             new_ingredient = input("Enter the next ingredient: ")
#             ingredients += (new_ingredient,)
#         else:
#             break

# 8-13



# build_profile("first_name", "last_name", "age", "city", "country")

# 8-14
# def make_car(manufacturer, model, color, tow_package=False):
#     car = {
#         'manufacturer': manufacturer,
#         'model': model,
#         'color': color,
#         'tow_package': tow_package
#     }
#     for key, value in car.items():
#         car[key] = value
#     return car

# car1 = make_car("Toyota", "Camry", "Blue")
# print(car1)

# 8-15
# import print_models
# print_models.make_pizza(16, "pepperoni", " mushrooms")

# 8-16
# import print_models
# print_models.make_pizza(16, "pepperoni", " mushrooms")

# from print_models import make_pizza
# make_pizza(16, "pepperoni", " mushrooms")

# from print_models import make_pizza as mp
# mp(16, "pepperoni", " mushrooms")

# import print_models as pm
# pm.make_pizza(16, "pepperoni", " mushrooms")

# from print_models import *
# make_pizza(16, "pepperoni", " mushrooms")

# from print_models import make_pizza, show_magicians, build_profile
# make_pizza(16, "pepperoni", " mushrooms")
# show_magicians()
# build_profile("first_name", "last_name", "age", "city", "country")

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

def sum_double(a, b):
    if a == b:
        print (2 * (a + b))
    else:
        print(a + b)

sum_double(a, b)

