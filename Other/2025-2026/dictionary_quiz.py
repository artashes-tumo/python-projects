# personal_info = {
#     "first name": "John",
#     "last name": "Doe",
#     "age": 30,
#     "city": "New York",
#     "interests": ["programming", "traveling", "cooking"]
# }

# print(f"First Name: {personal_info['first name']}")
# print(f"Last Name: {personal_info['last name']}")
# print(f"Age: {personal_info['age']}")
# print(f"City: {personal_info['city']}")
# print("Interests:")
# for interest in personal_info["interests"]:
#     print(f"- {interest}")


# five_python_commands_i_know = {
#     "print()": "Used to output text or variables to the console.",
#     "input()": "Used to take user input from the console.",
#     "len()": "Returns the length of an object, such as a string or list.",
#     "type()": "Returns the type of an object.",
#     "range()": "Generates a sequence of numbers, often used in loops."
# }

# print("Here are five Python commands I know:")
# for command, description in five_python_commands_i_know.items():
#     print(f"{command}: {description}")

# questions_and_answers_for_quiz = {
#     "What is the capital of France?": "Paris",
#     "What is the largest planet in our solar system?": "Jupiter",
#     "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
#     "What is the chemical symbol for water?": "H2O",
#     "What is the square root of 64?": "8",
#     "Who painted the Mona Lisa?": "Leonardo da Vinci",
#     "What is the smallest prime number?": "2",
#     "What is the currency of Japan?": "Yen",
#     "Who is the author of '1984'?": "George Orwell",
#     "What is the largest mammal?": "Blue Whale"
# }

# import random
# # shuffle the questions
# questions = list(questions_and_answers_for_quiz.keys())
# random.shuffle(questions)
# score = 0

# print("Welcome to the quiz!")
# print("You will be asked 10 questions. Try to answer them correctly!")
# print("For each correct answer, you will earn 1 point. Let's see how many points you can get!\n")
# print("Let's get started!\n")
# for question in questions:
#     answer = input(question + " ")
#     if answer.strip().lower() == questions_and_answers_for_quiz[question].strip().lower():
#         print("Correct!\n")
#         score += 1
#     else:
#         print(f"Wrong! The correct answer is: {questions_and_answers_for_quiz[question]}\n")
      
# print(f"Quiz completed! Your score is: {score}/10")


# dictionary inside a dictionary, inside a dictionary

# family = {
#     "parents": {
#         "father": {
#             "name": "John",
#             "age": 50,
#             "occupation": "Engineer"
#         },
#         "mother": {
#             "name": "Jane",
#             "age": 48,
#             "occupation": "Teacher"
#         }
#     },
#     "children": {
#         "son": {
#             "name": "Jack",
#             "age": 20,
#             "occupation": "Student"
#         },
#         "daughter": {
#             "name": "Jill",
#             "age": 18,
#             "occupation": "Student"
#         }
#     }
# }

import random

number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
print("You have 10 attempts to guess the number. Good luck!\n")
attempts = 10
while attempts > 0:
    guess = input("Enter your guess(exit to quit): ")
    if guess.lower() == "exit":
        print("Thanks for playing! Goodbye!")
        break 
    guess = int(guess)
    if guess < number:
        print("Too low! Try again.\n")
    elif guess > number:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You've guessed the number {number} correctly!")
        break
    attempts -= 1
    print(f"You have {attempts} attempts left.\n")
if attempts == 0:
    print(f"Game over! The number was {number}. Better luck next time!")


print("Thanks for playing!")