questions_with_answers = {
    "question": "What is the capital of France?", "answer": "Paris",
    "question": "What is the largest planet in our solar system?", "answer": "Jupiter",
    "question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare",
    "question": "What is the chemical symbol for water?", "answer": "H2O",
    "question": "What is the hardest natural substance?", "answer": "Diamond",
    "question": "How many bones are in the human body?", "answer": "206",
    "question": "What is the largest mammal?", "answer": "Blue Whale",
    "question": "What is the smallest prime number?", "answer": "2",
    "question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci",
    "question": "What is the speed of light in vacuum (in km/s)?", "answer": "299792",
    "question": "What is the tallest mountain in the world?", "answer": "Mount Everest",
    "question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean",
    "question": "Who is known as the 'Father of Computers'?", "answer": "Charles Babbage",
    "question": "What is the chemical symbol for gold?", "answer": "Au",
    "question": "What is the longest river in the world?", "answer": "Nile River",
    "question": "What is the smallest country in the world?", "answer": "Vatican City",
    "question": "Who discovered penicillin?", "answer": "Alexander Fleming",
    "question": "What is the largest desert in the world?", "answer": "Sahara Desert",
    "question": "What is the chemical symbol for iron?", "answer": "Fe",
    "question": "What is the capital of Japan?", "answer": "Tokyo",
    "question": "What is the largest island in the world?", "answer": "Greenland",
    "question": "Who is the author of 'Harry Potter' series?", "answer": "J.K. Rowling",
    "question": "What is the chemical symbol for sodium?", "answer": "Na",
    "question": "What is the largest continent on Earth?", "answer": "Asia"
}

print("Welcome to the Quiz Game!")
print("You will be asked a series of questions. Try to answer them correctly!")
print("Let's get started!\n")
print("And if you want to quit the quiz at any time, just type 'exit' or 'quit'.\n")

scxore = 0

import random
# shuffle the questions
questions_list = list(questions_with_answers.keys())
random.shuffle(questions_list)

for question in questions_list:
    correct_answer = questions_with_answers[question]
    user_answer = input(question + " ")
    if user_answer.strip().lower() == "exit" or user_answer.strip().lower() == "quit":
        print("Quiz exited! Thanks for playing!")
        break
    elif user_answer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
        scxore += 1
    else:
        print(f"Wrong! The correct answer is: {correct_answer}\n")

print(f"Quiz completed! Thanks for playing! Your score is: {scxore}/{len(questions_with_answers)}")