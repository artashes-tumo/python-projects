import random

students = [0, 0, 0, 0, "Louis", "Christos", "Alexander", "Lukas", "Addis", "Antoine", "Jason", "Jonathan", "Kian", "Andrii", "Jakob", "Zubair", "Artashes", "Niranjan"]
seat_num = 18
print("Seating Arrangement:")
for seat in range(1, seat_num + 1):
    student_name = random.choice(students)
    print(f"Seat {seat}: {student_name}")
    students.remove(student_name)
