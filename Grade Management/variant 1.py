# Imports
import json
from pathlib import Path
from typing import Dict, Tuple

# Configuration

Grades_File = Path("Grade Management/grades.json")

if not Grades_File.exists():
    subjects = input("What subjects do you study? (Separate with commas) ").split(",")
    subjects = [subject.strip().lower() for subject in subjects]
    with open(Grades_File, "w") as addupp:
        json.dump(
            {subject: {"A": 0, "B": 0, "C": 0, "D": 0} for subject in subjects}, 
            addupp,
            indent=4
        )    
# load
with open(Grades_File, "r") as GradesLoad:
    grades_list = json.load(GradesLoad)

def showGrades():
    for subject, grades_showing in grades_list.items():
        print(f"{subject.capitalize()}:")
        
        for grade, count in grades_showing.items():
            print(f"  {grade}: {count}")

        # Only calculate if all grades entered
        if all(count > 0 for count in grades_showing.values()):
            totalgradesum = sum(grades_showing.values())
            print(f"Total Grade Sum: {totalgradesum}")

            if totalgradesum >= 28:
                print("Final Grade: 7")
            elif totalgradesum >= 24:
                print("Final Grade: 6")
            elif totalgradesum >= 19:
                print("Final Grade: 5")
            elif totalgradesum >= 15:
                print("Final Grade: 4")
            elif totalgradesum >= 10:
                print("Final Grade: 3")
            elif totalgradesum >= 6:
                print("Final Grade: 2")
            else:
                print("Final Grade: 1")
        else:
            print("Not all criteria graded yet.")

        print()

def addGrade():
    subject_choice = input("Enter the subject:   ").strip().lower()

    if subject_choice in grades_list:
        grade_Criteria = input("Enter the Criteria (A, B, C, D): ").strip().upper()

        if grade_Criteria in grades_list[subject_choice]:
            grade_number = int(input("Enter the grade(1-8): "))

            if 1 <= grade_number <= 8:
                grades_list[subject_choice][grade_Criteria] = grade_number
                print("Grade added successfully!")
                with open(Grades_File, "w") as GradesSave:
                    json.dump(grades_list, GradesSave, indent=4)
            else:
                print("Invalid grade number. Please enter a number between 1 and 8.")

        else:
            print("Invalid grade criteria. Please enter A, B, C, or D.")

    else:
        print("Subject not found. Please enter a valid subject.")

def resetGrades():
    subject_choice = input("Enter the subject to reset grades for: ").strip().lower()
    if subject_choice in grades_list:
        print(f"Resetting all 4 criteria grades for {subject_choice.capitalize()}")

        for grade in grades_list[subject_choice]:
            print(f"Resetting {grade} grade to 0.")
            grades_list[subject_choice][grade] = 0
        
        with open(Grades_File, "w") as GradesReset:
            json.dump(grades_list, GradesReset, indent=4)
        print("All grades have been reset to 0.")

    else:
        print("Subject not found. Please enter a valid subject.")

def gradesDistribution():
    distribution = {str(i): 0 for i in range(1, 9)}

    for subject, grades in grades_list.items():
        for criteria, value in grades.items():
            if value != 0: 
                distribution[str(value)] += 1

    print("Grade Distribution:")
    for grade, count in distribution.items():
        print(f"  {grade}: {'█' * count} ({count})")

def SmartAdvisor():
    subject_choice = input("Enter the subject for advice: ").strip().lower()
    if subject_choice in grades_list:
        finalgradechoice = input("Enter the final grade you want to achieve (1-7): ").strip()
        if finalgradechoice in [str(i) for i in range(1, 8)]:
            finalgradechoice = int(finalgradechoice)
            current_total = sum(grades_list[subject_choice].values())
            required_total = 0

            if finalgradechoice == 7:
                required_total = 28
            elif finalgradechoice == 6:
                required_total = 24
            elif finalgradechoice == 5:
                required_total = 19
            elif finalgradechoice == 4:
                required_total = 15
            elif finalgradechoice == 3:
                required_total = 10
            elif finalgradechoice == 2:
                required_total = 6
            else:
                print("Final Grade: 1 requires no points.")

            missing_criteria_grade_count = sum(1 for grade in grades_list[subject_choice].values() if grade == 0)
            points_needed = max(0, required_total - current_total)

            if points_needed == 0:
                print(f"You have already achieved a final grade of {finalgradechoice} or higher.")
            
            if missing_criteria_grade_count >1:
                print(f"To achieve a final grade of {finalgradechoice}, you need a total amount of minimum {points_needed} points with average of {points_needed / missing_criteria_grade_count} points per criterion.")
                print(f"You currently have {current_total} points, so you need at least {points_needed} more points across the remaining criteria.")
            else:
                print(f"To achieve a final grade of {finalgradechoice}, you need a total of minimum {required_total} points.")
                print(f"You currently have {current_total} points, so you need at least {points_needed} more points.")
        else:
            print("Invalid final grade choice. Please enter a number between 1 and 7.")
    else:
        print("Subject not found. Please enter a valid subject.")

while True:
    print("\n      Grade Management System")
    print("1. Show Grades       4. Grade Distribution")
    print("2. Add Grade         5. Smart Advisor")
    print("3. Reset Grades      6. Exit and Save")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        showGrades()
    elif choice == "2":
        addGrade()
    elif choice == "3":
        resetGrades()
    elif choice == "4":
        gradesDistribution()
    elif choice == "5":
        SmartAdvisor()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")