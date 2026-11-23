import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Manager")
root.geometry('500x400')
root.config(bg="#341850")
root.resizable(0, 0)

# Determines The Student Grade by multiple set values 
def get_grade(percentage):
    if percentage >= 70:
        return "A"
    if percentage >= 60:
        return "B"
    if percentage >= 50:
        return "C"
    if percentage >= 40:
        return "D"
    return "F"

def load_students(path="studentMarks.txt"):
    with open(path) as file_handler:
        studentlist = file_handler.read().splitlines()

    result = []
    for i in studentlist[1:]: # for every line starting from the second index [1]
        student = i.split(",") # split student line by the set value "," becoming a list

        numID = student[0]                       # first index [0] is the Number ID
        StName = student[1]                      # second index [1] is the Student Name
        CoTl = int(student[2]) + int(student[3]) + int(student[4])   # Coursework Total from [2] [3] [4]
        ExMs = int(student[5])                   # Exam Marks

        percentage = (CoTl + ExMs) / 160 * 100 # Individual Students overall percentage
        Load_student_grade = get_grade(percentage) # Calls Get_Grades Function to get grades

        # appends individual student details to the results dictionary
        result.append({"id" : numID, "name" : StName, "CsTl" : CoTl, "ExMs" : ExMs, "percentage" : percentage, "s": Load_student_grade})
        colors = ["#e8f1f5", "#ffffff"]  # Colors to cycle through
    return result 

students = load_students()

# Overall structure format of students to be showwn
def format_student(s):
    return (f"Number ID : {s['id']}\n"
            f"Student Name : {s['name']}\n"
            f"Coursework Total : {s['CsTl']}/60\n"
            f"Exam Marks : {s['ExMs']}/100\n"
            f"Percentage : {s['percentage']:.1f}%\n"
            f"Student Grade : {s['s']}\n"
            + "-" * 35 + "\n")

# Displays a Certain information given by parameters inside the text area 
def show(title, text):
    Rlb.config(text=title)
    txtarea.delete("1.0", tk.END)
    txtarea.insert(tk.END, text)

def records_text(records):
    text = "\n".join(format_student(s) for s in records)
    if records:
        average = sum(s["percentage"] for s in records) / len(records)
        text += ("\nNumber of Students : {len(records)}\n"
        f"Average Percentage : {average:.1f}%\n")
    return text

# Function for showing all students | MAIN
def ShowStudentsAll():
    text = "\n".join(format_student(s) for s in students)   # joins every formatted student record into one block of text

    if students:                                             # only calculates the summary if there is at least one student
        average = sum(s["percentage"] for s in students) / len(students)   # adds up every percentage then divides by the number of students
        text += (f"\nNumber of Students : {len(students)}\n"              # adds the total number of students to the end of the text
                 f"Average Percentage : {average:.1f}%\n")                 # adds the class average rounded to 1 decimal place
        
    show("Student Records", text)                            # displays the title and all the text in the text area

# Function for searching a student by name or number ID | SEARCH
def searchRecord(event=None):
    query = e1.get().strip().lower()             # gets the text typed in the entry box, removes spaces and lowercases it
    if not query:                                # checks if the entry box is empty
        show("Search Student", "Please enter a student name or number.")
        return                                   # stops the function if nothing was typed
    matches = [s for s in students
               if query == s["id"] or query in s["name"].lower()]   # matches exact Number ID or part of the Student Name
    if matches:
        show("Search Results", "\n".join(format_student(s) for s in matches))   # shows every student that matched
    else:
        show("Search Results", f"No student found matching '{query}'.")         # message shown when nothing matches

# Function for showing the student with the highest percentage | HIGHEST
def ShowHighest():
    best = max(s["percentage"] for s in students)               # finds the highest percentage out of all students
    matches = [s for s in students if s["percentage"] == best]  # collects every student with that percentage (in case of a tie)
    show("Highest Score", "\n".join(format_student(s) for s in matches))   # displays the matching student details


# Function for showing the student with the lowest percentage | LOWEST
def ShowLowest():
    worst = min(s["percentage"] for s in students)              # finds the lowest percentage out of all students
    matches = [s for s in students if s["percentage"] == worst] # collects every student with that percentage (in case of a tie)
    show("Lowest Score", "\n".join(format_student(s) for s in matches))    # displays the matching student details


sort_ascending = True
def SortStudents():
    global sort_ascending
    ordered = sorted(students, key=lambda s: s["percentage"], reverse=not sort_ascending)
    order = "Ascending" if sort_ascending else "Descending"
    show(f"Sorted ({order})", records_text(ordered))
    sort_ascending = not sort_ascending
    if sort_ascending:
        b5.config(bg="blue")
    else:
        b5.config(bg="red")
#---------------------------------------------------------------------------------------------------------------------------------------------
def open_adding_window():

    def show_error(entry , text="Enter a Valid Value"):
        entry.delete(0, tk.END)
        entry.insert(0, text)
        entry.config(fg="red")

    def AppendToFile():
        for entry in (e1, e2, c1, c2, c3):
            entry.config(fg="black")

        try:
            numberID = int(e1.get())
            if not 1000 <= (numberID) <= 9999:
                raise ValueError
        except ValueError:
            show_error(e1)
            return

        studentName = e2.get().strip()
        if len(studentName) < 2:
            show_error(e2)
            return

                # Coursework 1
        try:
            cw1 = int(c1.get())
            if not 0 <= cw1 <= 20:
                raise ValueError
        except ValueError:
            show_error(c1, "Invalid")
            return

        # Coursework 2
        try:
            cw2 = int(c2.get())
            if not 0 <= cw2 <= 20:
                raise ValueError
        except ValueError:
            show_error(c2, "Invalid")
            return

        # Coursework 3
        try:
            cw3 = int(c3.get())
            if not 0 <= cw3 <= 20:
                raise ValueError
        except ValueError:
            show_error(c3, "Invalid")
            return

        for entry in (e1, e2, c1, c2, c3):
            entry.config(fg="black")

        try:
            exam = int(e3.get())
            if not 0 <= exam <= 100:
                raise ValueError
        except ValueError:
            show_error(e3)
            return

        results = [numberID, studentName, cw1, cw2, cw3, exam]
        line = ", ".join(str(r) for r in results)

        with open("studentMarks.txt", 'a') as file_handler:
            file_handler.write(line + "\n")

    win = tk.Toplevel(root)
    win.geometry('300x300')

    Lab = tk.Label(win, text="Add Student Details", font=("Roboto", 15)).pack()

    l1 = tk.Label(win, text="Number ID").pack()
    e1 = tk.Entry(win)
    e1.pack()
    
    l2 = tk.Label(win, text="Name").pack()
    e2 = tk.Entry(win)
    e2.pack()

    l3 = tk.Label(win, text="Courswork").pack()
    cw_frame = tk.Frame(win)
    cw_frame.pack(pady=2)
    c1 = tk.Entry(cw_frame, width=8)
    c1.grid(row=0, column=0, padx=3)
    c2 = tk.Entry(cw_frame, width=8)
    c2.grid(row=0, column=1, padx=3)
    c3 = tk.Entry(cw_frame, width=8)
    c3.grid(row=0, column=2, padx=3)

    l4 = tk.Label(win, text="Exam marks").pack()
    e3 = tk.Entry(win)
    e3.pack()

    addB = tk.Button(win, text="Submit and Add", command=AppendToFile).pack(pady=10)

#---------------------------------------------------------------------------------------------------------------------------------------------
navbar_frame = tk.Frame(root, bg="#A167DC", width=150)
navbar_frame.pack(side=tk.LEFT, fill="y")
navbar_frame.pack_propagate(False)

b1 = tk.Button(navbar_frame, text="View All Records",
               command=ShowStudentsAll)
b1.place(x=10, y=15)

e1 = tk.Entry(navbar_frame, width=15)
e1.place(x=10, y=55)

b2 = tk.Button(navbar_frame, text="Search Record",
               command=searchRecord)
b2.place(x=10, y=82)

b3 = tk.Button(navbar_frame, text="Show Highest Score",
               command=ShowHighest)
b3.place(x=10, y=125)

b4 = tk.Button(navbar_frame, text="Show Lowest Score",
               command=ShowLowest)
b4.place(x=10, y=157)

b5 = tk.Button(navbar_frame, text="Sort Records", width=16,
               command=SortStudents)
b5.place(x=10, y=200)

b6 = tk.Button(navbar_frame, text="Add Student", width=16)
b6.place(x=10, y=250)


main_frame = tk.Frame(root)
main_frame.pack(side=tk.LEFT, fill="both", expand=True)

Rlb = tk.Label(main_frame, text="Student Manager")
Rlb.pack()

txtarea = tk.Text(main_frame, width=30, height=10)
txtarea.pack(padx=10, pady=5, fill="both", expand=True)

root.mainloop()