
import json
from pathlib import Path
from typing import Dict, Tuple

# ==========================================================
# CONFIG
# ==========================================================

DATA_FILE = Path("myp_grades.json")

GRADE_BOUNDARIES: Dict[int, int] = {
    7: 28,
    6: 24,
    5: 19,
    4: 15,
    3: 10,
    2: 6,
    1: 4
}

DEFAULT_SUBJECTS: Dict[str, Dict[str, int]] = {
    subject: {c: 0 for c in ["A", "B", "C", "D"]}
    for subject in [
        "English", "German", "Geography", "Science",
        "Mathematics", "P.E.", "Multimedia", "Programming"
    ]
}

# ==========================================================
# CORE LOGIC
# ==========================================================

def calculate_total_and_final(grades: Dict[str, int]) -> Tuple[int, int]:
    total = sum(grades.values())

    for final, boundary in sorted(GRADE_BOUNDARIES.items(), reverse=True):
        if total >= boundary:
            return total, final

    return total, 1


# ==========================================================
# DATA HANDLING
# ==========================================================

def load_grades():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except Exception:
            print("⚠️ Error reading file. Using default data.")
    return DEFAULT_SUBJECTS.copy()


def save_grades(subjects):
    try:
        DATA_FILE.write_text(json.dumps(subjects, indent=4))
        print("✅ Data saved.")
    except Exception:
        print("❌ Failed to save.")


# ==========================================================
# COMMAND FUNCTIONS
# ==========================================================

def add(subjects, parts):
    # add Math 7 6 5 8
    if len(parts) != 6:
        print("❌ Usage: add <subject> A B C D")
        return

    subject = parts[1]

    try:
        grades = {
            "A": int(parts[2]),
            "B": int(parts[3]),
            "C": int(parts[4]),
            "D": int(parts[5])
        }

        if not all(1 <= g <= 8 for g in grades.values()):
            raise ValueError

        subjects[subject] = grades

        total, final = calculate_total_and_final(grades)

        print(f"✅ {subject} updated.")
        print(f"Total: {total} | Final: {final}")

    except ValueError:
        print("❌ Grades must be numbers 1–8.")


def update(subjects, parts):
    # update Math A 7
    if len(parts) != 4:
        print("❌ Usage: update <subject> <A/B/C/D> <grade>")
        return

    subject = parts[1]
    crit = parts[2].upper()

    if subject not in subjects or crit not in ["A", "B", "C", "D"]:
        print("❌ Invalid subject or criteria.")
        return

    try:
        grade = int(parts[3])
        if not 1 <= grade <= 8:
            raise ValueError

        subjects[subject][crit] = grade
        total, final = calculate_total_and_final(subjects[subject])

        print(f"✅ Updated {subject} {crit} → {grade}")
        print(f"Total: {total} | Final: {final}")

    except ValueError:
        print("❌ Grade must be 1–8.")


def view(subjects, parts):
    # view OR view Math
    if len(parts) == 1:
        for subject, grades in subjects.items():
            total, final = calculate_total_and_final(grades)
            print(f"{subject}: {grades} | Total: {total} | Final: {final}")
    else:
        subject = parts[1]
        if subject in subjects:
            grades = subjects[subject]
            total, final = calculate_total_and_final(grades)
            print(f"{subject}: {grades}")
            print(f"Total: {total} | Final: {final}")
        else:
            print("❌ Subject not found.")


def reset(subjects, parts):
    # reset Math
    if len(parts) != 2:
        print("❌ Usage: reset <subject>")
        return

    subject = parts[1]

    if subject in subjects:
        subjects[subject] = {c: 0 for c in ["A", "B", "C", "D"]}
        print(f"✅ {subject} reset.")
    else:
        print("❌ Subject not found.")


def advisor(subjects, parts):
    # advisor Math 7
    if len(parts) != 3:
        print("❌ Usage: advisor <subject> <target>")
        return

    subject = parts[1]

    if subject not in subjects:
        print("❌ Subject not found.")
        return

    try:
        target = int(parts[2])
        required_total = GRADE_BOUNDARIES.get(target)

        if required_total is None:
            raise ValueError

        grades = subjects[subject]
        entered = [g for g in grades.values() if g > 0]
        missing = 4 - len(entered)

        if missing == 0:
            _, final = calculate_total_and_final(grades)
            print(f"Final grade already: {final}")
            return

        current = sum(entered)
        needed = max(0, required_total - current)

        print(f"Points needed: {needed}")

        if missing == 1:
            print(f"→ Need at least: {needed}")
        else:
            avg = (needed + missing - 1) // missing
            print(f"→ Suggested average: {avg}")

    except ValueError:
        print("❌ Invalid target grade.")


def help_menu():
    print("\nAvailable commands:")
    print(" add <subject> A B C D")
    print(" update <subject> <A/B/C/D> <grade>")
    print(" view [subject]")
    print(" reset <subject>")
    print(" advisor <subject> <target>")
    print(" save")
    print(" exit")

def detailed_help():
    print("\n" + "="*60)
    print("📘 DETAILED HELP GUIDE")
    print("="*60)

    print("\n🔹 add <subject> A B C D")
    print("  → Adds or replaces ALL 4 criteria grades for a subject")
    print("  Example: add Math 7 6 5 8")
    print("  Meaning: A=7, B=6, C=5, D=8")

    print("\n🔹 update <subject> <A/B/C/D> <grade>")
    print("  → Updates ONE criterion only")
    print("  Example: update Math A 7")

    print("\n🔹 view [subject]")
    print("  → Shows all subjects OR one subject")
    print("  Example: view")
    print("  Example: view Math")

    print("\n🔹 reset <subject>")
    print("  → Resets all criteria to 0")
    print("  Example: reset Math")

    print("\n🔹 advisor <subject> <target>")
    print("  → Shows what you need to reach a target grade")
    print("  Example: advisor Math 7")

    print("\n🔹 save")
    print("  → Saves your data to file")

    print("\n🔹 exit")
    print("  → Closes the program")

    print("\n📊 GRADE SYSTEM")
    print("  Criteria: 1–8")
    print("  Total: out of 32")
    print("  Final grade boundaries:")
    print("    7 → 28+")
    print("    6 → 24+")
    print("    5 → 19+")
    print("    4 → 15+")
    print("    3 → 10+")
    print("    2 → 6+")
    print("    1 → below 6")

    print("\n💡 TIPS")
    print("  • Use 'add' to quickly enter all grades")
    print("  • Use 'update' to fix one mistake")
    print("  • Use 'advisor' before final assessments")

    print("="*60 + "\n")


# ==========================================================
# MAIN LOOP
# ==========================================================

def main():
    subjects = load_grades()

    print("⚡ MYP Grade Advisor (Command Mode)")
    print("Type 'help' for commands and morehelp for detailed information.\n")

    while True:
        command = input(">> ").strip().split()

        if not command:
            continue

        cmd = command[0].lower()

        if cmd == "add":
            add(subjects, command)

        elif cmd == "update":
            update(subjects, command)

        elif cmd == "view":
            view(subjects, command)

        elif cmd == "reset":
            reset(subjects, command)

        elif cmd == "advisor":
            advisor(subjects, command)

        elif cmd == "save":
            save_grades(subjects)

        elif cmd == "help":
            help_menu()
        
        elif cmd == "morehelp":
            detailed_help()

        elif cmd == "exit":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()