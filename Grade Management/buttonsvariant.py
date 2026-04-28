import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter.font import Font

# =========================
# DATA SETUP
# =========================

DATA_DIR = Path("Grade Management")
DATA_DIR.mkdir(exist_ok=True)
GRADES_FILE = DATA_DIR / "grades.json"

DEFAULT_SUBJECTS = ["English", "German", "Maths", "History", "Science", "P.E."]

def load_grades():
    if not GRADES_FILE.exists():
        data = {s: {"A": 0, "B": 0, "C": 0, "D": 0} for s in DEFAULT_SUBJECTS}
        with open(GRADES_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return data
    with open(GRADES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_grades(data):
    with open(GRADES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

grades_data = load_grades()

# =========================
# HELPER FUNCTIONS
# =========================

def get_final_grade(total: int):
    if total >= 28: return 7, "#22ff88"   # vibrant green
    if total >= 24: return 6, "#44ffaa"
    if total >= 19: return 5, "#ffee33"   # bright yellow
    if total >= 15: return 4, "#ffaa33"
    if total >= 10: return 3, "#ff7733"
    if total >= 6:  return 2, "#ff4444"
    return 1, "#ff2266"                   # hot pink/red

# =========================
# MAIN APP
# =========================

class GradeForgeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GradeForge")
        self.root.geometry("860x680")
        self.root.configure(bg="#0f0f1a")

        # Custom fonts
        self.title_font = Font(family="Segoe UI", size=18, weight="bold")
        self.header_font = Font(family="Segoe UI", size=13, weight="bold")
        self.mono_font = Font(family="Consolas", size=11)

        self.create_styles()
        self.create_ui()

        self.refresh_all()

    def create_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        # Vibrant color palette
        style.configure("TFrame", background="#0f0f1a")
        style.configure("Card.TFrame", background="#1a1a2e", relief="flat")

        style.configure("TLabel", background="#0f0f1a", foreground="#e0e0ff", font=("Segoe UI", 10))
        style.configure("Header.TLabel", background="#0f0f1a", foreground="#a5b4fc", font=self.header_font)
        style.configure("Title.TLabel", background="#0f0f1a", foreground="#c4d0ff", font=self.title_font)

        # Beautiful buttons
        style.configure("Accent.TButton", 
                       font=("Segoe UI", 10, "bold"),
                       padding=10,
                       background="#6366f1")
        style.map("Accent.TButton",
                 background=[("active", "#818cf8"), ("pressed", "#4f46e5")])

        style.configure("Danger.TButton", 
                       font=("Segoe UI", 10, "bold"),
                       padding=10,
                       background="#f43f5e")
        style.map("Danger.TButton",
                 background=[("active", "#fb7185")])

        style.configure("Success.TButton", background="#22d3ee", foreground="#0f172a")

    def create_ui(self):
        # Main padding frame
        main = ttk.Frame(self.root, padding=25, style="TFrame")
        main.pack(fill=tk.BOTH, expand=True)

        # Header with gradient feel
        header = ttk.Frame(main, style="TFrame")
        header.pack(fill=tk.X, pady=(0, 30))

        title = ttk.Label(header, text="GradeForge", style="Title.TLabel")
        title.pack(side=tk.LEFT)

        subtitle = ttk.Label(header, text="  •  Advanced Grade Tracker", 
                           foreground="#64748b", font=("Segoe UI", 11))
        subtitle.pack(side=tk.LEFT, pady=6)

        # Input Card
        input_card = ttk.Frame(main, style="Card.TFrame")
        input_card.pack(fill=tk.X, pady=12, ipadx=20, ipady=20)

        ttk.Label(input_card, text="Manage Grades", style="Header.TLabel").pack(anchor="w", padx=20, pady=(10,15))

        # Input fields in a nice grid
        grid = ttk.Frame(input_card, style="Card.TFrame")
        grid.pack(padx=20, fill=tk.X)

        # Row 1
        ttk.Label(grid, text="Subject").grid(row=0, column=0, sticky="w", pady=8, padx=(0,10))
        self.subject_var = tk.StringVar()
        self.subject_combo = ttk.Combobox(grid, textvariable=self.subject_var, 
                                        values=list(grades_data.keys()), state="readonly", width=22, font=("Segoe UI", 10))
        self.subject_combo.grid(row=0, column=1, sticky="ew", padx=5, pady=8)

        ttk.Button(grid, text="+ New", command=self.add_new_subject, 
                  style="Accent.TButton", width=10).grid(row=0, column=2, padx=8)

        # Row 2
        ttk.Label(grid, text="Criteria").grid(row=1, column=0, sticky="w", pady=8, padx=(0,10))
        self.criteria_var = tk.StringVar(value="A")
        ttk.Combobox(grid, textvariable=self.criteria_var, values=["A","B","C","D"], 
                    state="readonly", width=8, font=("Segoe UI", 10)).grid(row=1, column=1, sticky="w", padx=5, pady=8)

        # Row 3
        ttk.Label(grid, text="Grade (1-8)").grid(row=2, column=0, sticky="w", pady=8, padx=(0,10))
        self.grade_var = tk.StringVar()
        ttk.Entry(grid, textvariable=self.grade_var, width=12, font=("Segoe UI", 10)).grid(row=2, column=1, sticky="w", padx=5, pady=8)

        # Action buttons
        btn_frame = ttk.Frame(input_card, style="Card.TFrame")
        btn_frame.pack(pady=18)

        ttk.Button(btn_frame, text="Add Grade", command=self.add_grade, 
                  style="Accent.TButton").pack(side=tk.LEFT, padx=6)
        ttk.Button(btn_frame, text="Reset", command=self.reset_subject, 
                  style="Danger.TButton").pack(side=tk.LEFT, padx=6)
        ttk.Button(btn_frame, text="Delete Subject", command=self.delete_subject, 
                  style="Danger.TButton").pack(side=tk.LEFT, padx=6)

        # Advisor Section
        advisor_card = ttk.Frame(main, style="Card.TFrame")
        advisor_card.pack(fill=tk.X, pady=12, ipadx=20, ipady=15)

        advisor_top = ttk.Frame(advisor_card, style="Card.TFrame")
        advisor_top.pack(fill=tk.X, padx=20, pady=10)

        ttk.Label(advisor_top, text="Smart Advisor", style="Header.TLabel").pack(side=tk.LEFT)
        
        ttk.Label(advisor_top, text="Target:").pack(side=tk.LEFT, padx=(30,5))
        self.target_var = tk.StringVar(value="7")
        ttk.Combobox(advisor_top, textvariable=self.target_var, values=["7","6","5","4","3","2","1"], 
                    width=5, state="readonly").pack(side=tk.LEFT)

        ttk.Button(advisor_top, text="Get Advice", command=self.show_advisor, 
                  style="Accent.TButton").pack(side=tk.RIGHT)

        # Output Area - Beautiful Text Widget
        output_card = ttk.Frame(main, style="Card.TFrame")
        output_card.pack(fill=tk.BOTH, expand=True, pady=12, ipadx=15, ipady=15)

        self.output = tk.Text(output_card, bg="#16162a", fg="#e0e0ff", 
                             font=self.mono_font, relief="flat", padx=18, pady=18,
                             wrap=tk.WORD, height=18, borderwidth=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(output_card, orient="vertical", command=self.output.yview)
        self.output.configure(yscrollcommand=scrollbar.set)

        self.output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Bottom bar
        bottom = ttk.Frame(main, style="TFrame")
        bottom.pack(fill=tk.X, pady=(15,0))

        ttk.Button(bottom, text="Refresh", command=self.refresh_all, 
                  style="Accent.TButton").pack(side=tk.LEFT)
        ttk.Button(bottom, text="Distribution", command=self.show_distribution, 
                  style="Accent.TButton").pack(side=tk.LEFT, padx=12)
        ttk.Button(bottom, text="Exit", command=self.on_close, 
                  style="Danger.TButton").pack(side=tk.RIGHT)

        # Initial combo update
        self.subject_combo['values'] = list(grades_data.keys())

    def add_new_subject(self):
        name = simpledialog.askstring("New Subject", "Subject name:", parent=self.root)
        if name and (name := name.strip().lower()):
            if name not in grades_data:
                grades_data[name] = {"A": 0, "B": 0, "C": 0, "D": 0}
                save_grades(grades_data)
                self.subject_combo['values'] = list(grades_data.keys())
                self.subject_var.set(name)
                messagebox.showinfo("Added", f"New subject '{name.capitalize()}' created!")
                self.refresh_all()

    def add_grade(self):
        subject = self.subject_var.get().strip().lower()
        criteria = self.criteria_var.get()
        try:
            grade = int(self.grade_var.get().strip())
        except:
            messagebox.showerror("Error", "Please enter a valid grade (1-8)")
            return

        if not subject or subject not in grades_data:
            messagebox.showerror("Error", "Please select a subject")
            return
        if criteria not in ["A", "B", "C", "D"]:
            messagebox.showerror("Error", "Invalid criteria")
            return
        if not 1 <= grade <= 8:
            messagebox.showerror("Error", "Grade must be between 1 and 8")
            return

        grades_data[subject][criteria] = grade
        save_grades(grades_data)
        messagebox.showinfo("Success", f"Added {grade} to {subject.capitalize()} - {criteria}")
        self.refresh_all()

    def reset_subject(self):
        subject = self.subject_var.get().strip().lower()
        if subject and subject in grades_data:
            if messagebox.askyesno("Reset", f"Reset all grades for {subject.capitalize()}?"):
                grades_data[subject] = {"A": 0, "B": 0, "C": 0, "D": 0}
                save_grades(grades_data)
                self.refresh_all()

    def delete_subject(self):
        subject = self.subject_var.get().strip().lower()
        if subject and subject in grades_data:
            if messagebox.askyesno("Delete", f"Delete subject '{subject.capitalize()}' permanently?", icon="warning"):
                del grades_data[subject]
                save_grades(grades_data)
                self.subject_combo['values'] = list(grades_data.keys())
                if grades_data:
                    self.subject_var.set(list(grades_data.keys())[0])
                self.refresh_all()

    def show_advisor(self):
        subject = self.subject_var.get().strip().lower()
        if not subject or subject not in grades_data:
            messagebox.showerror("Error", "Select a subject first")
            return

        try:
            target = int(self.target_var.get())
        except:
            return

        boundaries = {7:28, 6:24, 5:19, 4:15, 3:10, 2:6, 1:4}
        grades = grades_data[subject]
        current = sum(v for v in grades.values() if v > 0)
        missing = sum(1 for v in grades.values() if v == 0)
        needed = max(0, boundaries.get(target, 28) - current)

        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, f"SMART ADVISOR — {subject.upper()}\n\n", "title")
        self.output.insert(tk.END, f"Target Grade: {target}\n")
        self.output.insert(tk.END, f"Current Points: {current}\n")
        self.output.insert(tk.END, f"Needed Points: {needed}\n")
        self.output.insert(tk.END, f"Remaining Tests: {missing}\n\n")

        if needed == 0:
            self.output.insert(tk.END, "EXCELLENT! Target already achieved ✨\n", "success")
        elif missing == 0:
            self.output.insert(tk.END, "Not enough tests left to reach target.\n", "danger")
        else:
            avg = (needed + missing - 1) // missing
            self.output.insert(tk.END, f"Average required per remaining test: {avg}\n", "accent")

        self.apply_output_tags()

    def show_distribution(self):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "OVERALL GRADE DISTRIBUTION\n", "title")
        self.output.insert(tk.END, "═"*48 + "\n\n")

        dist = {str(i): 0 for i in range(1, 9)}
        for subj in grades_data.values():
            for v in subj.values():
                if v != 0:
                    dist[str(v)] += 1

        colors = ["#22ff88", "#44ffaa", "#ffee33", "#ffaa33", "#ff7733", "#ff4444", "#ff2266", "#cc11aa"]
        for i, (g, count) in enumerate(dist.items(), 1):
            bar = "█" * min(count * 2, 25)
            self.output.insert(tk.END, f"Grade {g}  ", "label")
            self.output.insert(tk.END, f"{bar}  ({count})\n", "bar")

        self.apply_output_tags()

    def refresh_all(self):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "YOUR GRADES\n", "title")
        self.output.insert(tk.END, "═"*45 + "\n\n")

        for subject, crits in grades_data.items():
            self.output.insert(tk.END, f"◆ {subject.upper()}\n", "subject")

            total = sum(v for v in crits.values() if v > 0)
            graded = sum(1 for v in crits.values() if v > 0)

            for c, v in crits.items():
                emoji = "✅" if v > 0 else "⭕"
                self.output.insert(tk.END, f"   {c}: {v:2d}   {emoji}\n")

            if graded == 4:
                final, color = get_final_grade(total)
                self.output.insert(tk.END, f"\n   → Final Grade: {final}  ", "final")
                self.output.insert(tk.END, "★ Excellent!\n\n" if final >= 6 else "\n\n", "final")
            else:
                self.output.insert(tk.END, f"\n   {graded}/4 criteria graded\n\n", "info")

        self.apply_output_tags()

    def apply_output_tags(self):
        self.output.tag_config("title", font=("Segoe UI", 14, "bold"), foreground="#c4d0ff")
        self.output.tag_config("subject", font=("Segoe UI", 12, "bold"), foreground="#a5b4fc")
        self.output.tag_config("final", font=("Segoe UI", 12, "bold"), foreground="#67e8f9")
        self.output.tag_config("success", foreground="#67e8f9")
        self.output.tag_config("accent", foreground="#818cf8")
        self.output.tag_config("danger", foreground="#fb7185")
        self.output.tag_config("info", foreground="#94a3b8")
        self.output.tag_config("bar", foreground="#67e8f9")

    def on_close(self):
        if messagebox.askokcancel("Exit GradeForge", "Save all changes before exiting?"):
            save_grades(grades_data)
            self.root.destroy()

    def run(self):
        self.root.mainloop()


# =========================
# LAUNCH
# =========================

if __name__ == "__main__":
    app = GradeForgeApp()
    app.run()