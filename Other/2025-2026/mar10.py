# 7-4

# toppings_list = []
# toppings = ""
# while toppings.lower() != "quit":
#     toppings = input("What toppings would you like on your pizza? (Type 'quit' to finish) ")
#     if toppings.lower() != "quit":
#         print(f"Adding {toppings} to your pizza.")
#         toppings_list.append(toppings)
#     else:
#         print("No more toppings will be added.")
#         break

# print("Finished making your pizza!")
# print("Your pizza has the following toppings:")
# for topping in toppings_list:
#     print(f"- {topping}")


# 7-5

# age = int(input("Please enter your age: "))

# if age <= 0:
#     print("Invalid age. Please enter a positive number.")
#     age = int(input("Please enter your age: "))
# while age >0:
#     if age <3:
#         print("The ticket is free.")
#     elif age < 12:
#         print("The ticket costs $10.")
#     else:
#         print("The ticket costs $15.")
#     break


# 7-6(same as 7-5 but with quit option)

# age = input("Please enter your age (or type 'quit' to exit): ")
# while age.lower() != "quit":
#     if age.isdigit():
#         age = int(age)
#         if age <= 0:
#             print("Invalid age. Please enter a positive number.")
#         elif age < 3:
#             print("The ticket is free.")
#         elif age < 12:
#             print("The ticket costs $10.")
#         else:
#             print("The ticket costs $15.")
#     else:
#         print("Invalid input. Please enter a valid age or type 'quit' to exit.")
#     age = input("Please enter your age (or type 'quit' to exit): ")

# infinite loop(7-7)

# while True:
#     print("This is an infinite loop. Type 'quit' to exit.")
#     user_input = input("Enter something: ")
#     if user_input.lower() == "quit":
#         print("Exiting the loop. Goodbye!")
#         break


# 7-8

# sandwich_orders = ["pastrami", "turkey", "ham", "pastrami", "veggie", "pastrami"]
# finished_sandwiches = []

# while sandwich_orders:
#     sandwich = sandwich_orders.pop(0)
#     print(f"Made a {sandwich} sandwich.")
#     finished_sandwiches.append(sandwich)

# 7-9

# sandwich_orders = ["pastrami", "turkey", "ham", "pastrami", "veggie", "pastrami"]
# finished_sandwiches = []

# print("Sorry, we are out of pastrami sandwiches.")
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")

# 7-10

# favorite_vacations = input("Enter your favorite vacation destinations: ")

# while True:
#     print("If you could visit one place in the world, where would you go?")
#     destination = input("Enter a destination (or type 'quit' to exit): ")
#     if destination.lower() == "quit":
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print(f"Great choice! {destination} sounds like an amazing place to visit.")


# random functions

# import random

# # random number(feature 1)
# random_number = random.randint(1, 100)
# print(f"Random number between 1 and 100: {random_number}")

# # random choice(feature 2)
# options = ["rock", "paper", "scissors"]
# random_choice = random.choice(options)
# print(f"Random choice from options {options}: {random_choice}")


# rock paper scissors game

import random
options = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Enter your choice (rock, paper, scissors) or type 'quit' to exit: ")
    if user_choice.lower() == "quit":
        print("Exiting the game. Goodbye!")
        break
    elif user_choice.lower() not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice.lower() == computer_choice:
        print("It's a tie!")
    elif (user_choice.lower() == "rock" and computer_choice == "scissors") or \
         (user_choice.lower() == "paper" and computer_choice == "rock") or \
         (user_choice.lower() == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")