# def convert(minutes):
#     seconds = minutes*60
#     print(f'{minutes} minutes is {seconds} seconds.')

# convert(3)


# def addition(a, b):
#     num_sum = a+b
#     print(f'The Sum of {a} and {b} is {a+b}')

# addition(3, 5)


# def calc_age(age):
#     ageindays = age * 0.75 * 365 + age * 0.25 * 366
#     print(f'{age} years is {ageindays} days')

# calc_age(20)

    
# def get_first_value():
#     num_list = []
#     while True:
#         print("type s to stop")
#         num_list_nums = input("Enter a number: ")
#         if num_list_nums == "s":
#             break
#         num_list.append(num_list_nums)
#     if len(num_list) > 0:
#         print(f'The first value of numbers {num_list} is {num_list[0]} ')
#     else:
#         print("No numbers were entered.")

# get_first_value()


# def football_points(wins, draws, losses):

#     if wins < 0 or draws < 0 or losses < 0:
#         print("Wins, draws, and losses cannot be negative.")
#         return

#     points = wins * 3 + draws * 1 + losses * 0
#     print(f"The total points are {points} points.")

# football_points(3, 2, 1)


# def animals_to_legs(chickens, cows, pigs):
#     total_legs = chickens * 2 + cows * 4 + pigs * 4
#     print(f"The total number of legs is {total_legs} legs.")

# animals_to_legs(2, 3, 5)


# def less_than_or_equal_to_zero(num):
#     if num <= 0:
#         print(f"{num} is less than or equal to zero.")
#     else:
#         print(f"{num} is greater than zero.")

# less_than_or_equal_to_zero(-5)


# def convert(hours, minutes):
#     total_seconds = hours * 3600 + minutes * 60
#     print(f"{hours} hours and {minutes} minutes is equal to {total_seconds} seconds.")

# convert(1, 3)


# def greeting(name):
#     print(f"Hello, {name}!")

# greeting("Alice")


# def circuit_power(voltage, current):
#     power = voltage * current
#     print(f"The power is {power} watts.")

# circuit_power(120, 10)


# def are_equal(num1, num2):
#     if num1 == num2:
#         print(f"{num1} and {num2} are equal.")
#     else:
#         print(f"{num1} and {num2} are not equal.")


# def calculator(num1, operation, num2):
#     if operation == "+":
#         result = num1 + num2
#         print(f"The result of {num1} + {num2} is {result}.")
#     elif operation == "-":
#         result = num1 - num2
#         print(f"The result of {num1} - {num2} is {result}.")
#     elif operation == "*":
#         result = num1 * num2
#         print(f"The result of {num1} * {num2} is {result}.")
#     elif operation == "/":
#         if num2 != 0:
#             result = num1 / num2
#             print(f"The result of {num1} / {num2} is {result}.")
#         else:
#             print("Error: Division by zero is not allowed.")
#     else:
#         print("Invalid operation. Please use +, -, *, or /.")

# calculator(10, "+", 5)
# calculator(10, "-", 5)
# calculator(10, "*", 5)
# calculator(10, "/", 5)
# calculator(10, "/", 0)


