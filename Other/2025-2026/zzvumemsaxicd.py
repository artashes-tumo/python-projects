questions_with_answers = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "What is the hardest natural substance?": "Diamond",
    "How many bones are in the human body?": "206",
    "What is the largest mammal?": "Blue Whale",
    "What is the smallest prime number?": "2",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the speed of light in vacuum (in km/s)?": "299792",
    "What is the tallest mountain in the world?": "Mount Everest",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Who is known as the 'Father of Computers'?": "Charles Babbage",
    "What is the chemical symbol for gold?": "Au",
    "What is the longest river in the world?": "Nile River",
    "What is the smallest country in the world?": "Vatican City",
    "Who discovered penicillin?": "Alexander Fleming",
    "What is the largest desert in the world?": "Sahara Desert",
    "What is the chemical symbol for iron?": "Fe",
    "What is the capital of Japan?": "Tokyo",
    "What is the largest island in the world?": "Greenland",
    "Who is the author of 'Harry Potter' series?": "J.K. Rowling",
    "What is the chemical symbol for sodium?": "Na",
    "What is the largest continent on Earth?": "Asia"
}

score = 0

import random
questions = list(questions_with_answers.keys())
random.shuffle(questions)
print(questions)

for question in questions:
    answer = questions_with_answers[question]
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")


print(f"You scored {score} out of {len(questions_with_answers)}.")