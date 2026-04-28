import random

question_and_answer = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What is the hardest natural substance?", "answer": "Diamond"},
    {"question": "How many bones are in the human body?", "answer": "206"},
    {"question": "What is the largest mammal?", "answer": "Blue Whale"},
    {"question": "What is the smallest prime number?", "answer": "2"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the speed of light in vacuum ( in km/s)?", "answer": "300000"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "Who is known as the 'Father of Computers'?", "answer": "Charles Babbage"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "What is the longest river in the world?", "answer": "Nile River"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the largest desert in the world?", "answer": "Sahara Desert"},
    {"question": "What is the chemical symbol for iron?", "answer": "Fe"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "What is the largest island in the world?", "answer": "Greenland"},
    {"question": "Who is the author of 'Harry Potter' series?", "answer": "J.K. Rowling"},
    {"question": "What is the chemical symbol for sodium?", "answer": "Na"},
    {"question": "What is the largest continent on Earth?", "answer": "Asia"}
]

points = 0
num_of_questions_choose = int(input("How many questions would you like to answer? (1-25): "))
if num_of_questions_choose < 1 or num_of_questions_choose > len(question_and_answer):
    print(f"Invalid number of questions. Please choose a number between 1 and {len(question_and_answer)}.")
    num_of_questions_choose = len(question_and_answer)


print("Welcome to the quiz! Please answer the following questions:")
print(f"There are {len(question_and_answer)} questions in total.\n")
print("You will earn 1 point for each correct answer. Let's see how many you can get right!\n")
print("Note: Try to answer without looking up the answers. Good luck!\n")
print("Let's get started!\n")

random.shuffle(question_and_answer)  

for i, qa in enumerate(question_and_answer):
    if i >= num_of_questions_choose:
        break
    user_answer = input(qa["question"] + " ")
    if user_answer.strip().lower() == qa["answer"].strip().lower():
        print("Correct!")
        points += 1
    else:
        print(f"Wrong! The correct answer is {qa['answer']}.")

print(f"You scored {points} out of {num_of_questions_choose}.")
print("Thank you for playing the quiz! Hope you had fun and learned something new!")



