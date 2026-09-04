# # import random

# # computer_guess = random.randint(1, 100)

# # user_guess = None

# # attempts = 0


# # while user_guess != computer_guess:
# #     user_guess = int(input("Guess a number between 1 and 100: "))
# #     if user_guess < 1 or user_guess > 100 or user_guess != int(user_guess):
# #         print("Please guess a number within the range of 1 to 100.")
# #         continue
# #     if user_guess < computer_guess:
# #         print("Too low! Try again.")
# #         attempts += 1
# #         if attempts >= 10:
# #             print("Sorry, you've reached the maximum number of attempts. The correct number was:", computer_guess)
# #             break
# #         if user_guess - computer_guess <= 5:
# #             print("You're very close! Try again.")
# #     elif user_guess > computer_guess:
# #         print("Too high! Try again.")
# #         attempts += 1
# #         if attempts >= 10:
# #             print("Sorry, you've reached the maximum number of attempts. The correct number was:", computer_guess)
# #             break
# #         if user_guess - computer_guess <= 5:
# #             print("You're very close! Try again.")
# #     else:
# #         print("Congratulations! You've guessed the correct number:", computer_guess)
# #         print("It took you", attempts, "attempts.")

# import random
# import json
# from pathlib import Path

# script_dir = Path(__file__).parent
# Score = script_dir / "score.json"

# Score.parent.mkeadir(parents=True, exist_ok=True)

# if not Score.exists() or Score.stat().st_size == 0:
#     with open(Score, "w") as f:
#         json.dump({"score": 0}, f)

# with open(Score, "r") as f:
#     score_data = json.load(f)

# computer_guess = random.randint(1, 100)
# user_guess = None
# attempts = 0

# difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
# if difficulty == "easy":
#     max_attempts = 15
# elif difficulty == "medium":
#     max_attempts = 10
# elif difficulty == "hard":
#     max_attempts = 5
# else:
#     print("Invalid difficulty. Defaulting to medium.")
#     max_attempts = 10

# while user_guess != computer_guess:
#     user_guess = input("Guess a number between 1 and 100: ")
#     if not user_guess.isdigit():
#         print("Please enter a valid number.")
#         continue
#     user_guess = int(user_guess)
#     if int(user_guess) < 1 or int(user_guess) > 100:
#         print("Please guess a number within the range of 1 to 100.")
#         continue
#     if user_guess < computer_guess:
#         print("Too low! Try again.")
#         attempts += 1
#         if attempts >= max_attempts:
#             print("Sorry, you've reached the maximum number of attempts. The correct number was:", computer_guess)
#             break
#         if computer_guess - user_guess <= 5:
#             print("You're very close! Try again.")
#     elif user_guess > computer_guess:
#         print("Too high! Try again.")
#         attempts += 1
#         if attempts >= max_attempts:
#             print("Sorry, you've reached the maximum number of attempts. The correct number was:", computer_guess)
#             break
#         if user_guess - computer_guess <= 5:
#             print("You're very close! Try again.")
#     else:
#         print("Congratulations! You've guessed the correct number:", computer_guess)
#         print("It took you", attempts, "attempts.")

# score_data["score"] += attempts

# with open(Score, "w") as f:
#     json.dump(score_data, f)

# calculator
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = float(num1) + float(num2)
elif operation == "-":
    result = float(num1) - float(num2)
elif operation == "*":
    result = float(num1) * float(num2)
elif operation == "/":
    if float(num2) == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = float(num1) / float(num2)
else:
    if not operation in ["+", "-", "*", "/"]:
        result = "Error: Invalid operation. Please use +, -, *, or /."
    if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
        result = "Error: Invalid input. Please enter valid numbers."

print("Result:", result)