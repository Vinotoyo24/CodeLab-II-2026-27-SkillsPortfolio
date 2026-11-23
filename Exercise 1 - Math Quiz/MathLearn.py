# Import Tkinter for Gui, Messagebox, and Random Library Module
import tkinter as tk
import random
import os
from tkinter import messagebox
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#------------------------------------------------------------

# Global Variables for scoring and Max Number of Tries 
score = 0
tries = 2

# Function for Determining Tries Allowed Per question
# Starts Quiz and for resetting Points 
#------------------------------------------------------------
def StartQuestion(new):
    global score, tries
    tries = 2
    if new:
        score = 0
        Points_Label.config(text="Points: 0")

# This Line of code ensures that 10 Points is Given on the First Try at the Question
# And 5 points Given on the 2nd, else moves on to the next question
#------------------------------------------------------------
def done(correct):
    global score, tries
    if correct:
        score += 10 if tries == 2 else 5
        Points_Label.config(text=f"Points: {score}")
        return True
    tries -= 1
    return tries == 0

# Utilizing the MessageBox Module GUI this Part Determines and Calculates the Final Score.
# Play again Prompt withthe MessageBox Asking for a input of yes or no.
#------------------------------------------------------------
def displayResults():
    rank = "A+" if score > 90 else "A" if score >= 80 else "B" if score >= 70 else "C" if score >= 60 else "F"
    if not messagebox.askyesno("Quiz Complete", f"Score: {score}/100\nRank: {rank}\n\nPlay again?"):
        root.quit()

#Color Variables
#------------------------------------------------------------
EasyColor = "#73A5CA"
ModerateColor = "#FF933E"
AdvancedColor = "#FFE9A9"

#------------------------------------------------------------
def displayProblem_Easy(new=False):
    global res, count
    #This Function Generates Random Range from 1-9 and Symbol
    # Gets Correct Results for Random Generated Values
    EasyPage.tkraise()

    # This Line Resets on new Quizes and tries count, and count the questions, 
    if new:
        count = 0
    count += 1
    StartQuestion(new)

    v1 = random.randint(1, 9)
    v2 = random.randint(1, 9)
    sym = random.choice(["+", "-"])
    print(f"{v1} {sym} {v2}")

    if str(sym) == "+":
        res = int(v1) + int(v2)
    else:
        res = int(v1) - int(v2)

    print("Correct Answer: ", res)
    El1.config(text=f"Count {count}/10")
    El2.config(text=f"{v1} {sym} {v2} = ?")

# This Handles Answers that are input in and Error handlings.
def isCorrect_Easy():
    try:
        entry = int(Easy_Entry.get())
    except ValueError:
        print("Enter a Whole Number")
        return

    if done(entry == res):
        print("Waiting")
        Easy_Entry.set("")
        if count >= 10:
            print("Quiz Finished")
            displayResults()
            LearnPage.tkraise()
        else:
            displayProblem_Easy()
    else:
        print("Wrong, Try again")

#------------------------------------------------------------
def displayProblem_Moderate(new=False):
    global res, count
    #This Function Generates Random Range from 1-99 and Symbol
    # Gets Correct Results for Random Generated Values
    ModeratePage.tkraise()

    if new:
        count = 0
    count += 1
    StartQuestion(new)

    v1 = random.randint(1, 99)
    v2 = random.randint(1, 99)
    sym = random.choice(["+", "-"])
    print(f"{v1} {sym} {v2}")

    if str(sym) == "+":
        res = int(v1) + int(v2)
    else:
        res = int(v1) - int(v2)

    print("Correct Answer: ", res)
    Ml1.config(text=f"Count {count}/10")
    Ml2.config(text=f"{v1} {sym} {v2} = ?")

def isCorrect_Moderate():
    try:
        entry = int(Moderate_Entry.get())
    except ValueError:
        print("Enter a Whole Number")
        return

    if done(entry == res):
        print("Waiting")
        Moderate_Entry.set("")
        if count >= 10:
            print("Quiz Finished")
            displayResults()
            LearnPage.tkraise()
        else:
            displayProblem_Moderate()
    else:
        print("Wrong, Try again")

#------------------------------------------------------------
def displayProblem_Advanced(new=False):
    global res, count
    #This Function Generates Random Range from 1-9999 and Symbol
    # Gets Correct Results for Random Generated Values
    AdvancedPage.tkraise()

    if new:
        count = 0
    count += 1
    StartQuestion(new)

    v1 = random.randint(1, 9999)
    v2 = random.randint(1, 9999)
    sym = random.choice(["+", "-"])
    print(f"{v1} {sym} {v2}")

    if str(sym) == "+":
        res = int(v1) + int(v2)
    else:
        res = int(v1) - int(v2)

    print("Correct Answer: ", res)
    Al1.config(text=f"Count {count}/10")
    Al2.config(text=f"{v1} {sym} {v2} = ?")

def isCorrect_Advanced():
    try:
        entry = int(Advanced_Entry.get())
    except ValueError:
        print("Enter a Whole Number")
        return

    if done(entry == res):
        print("Waiting")
        Advanced_Entry.set("")
        if count >= 10:
            print("Quiz Finished")
            displayResults()
            LearnPage.tkraise()
        else:
            displayProblem_Advanced()
    else:
        print("Wrong, Try again")


# Create Root Window and Other Window Formatting settings
# ---------------------------------------------------------------
root = tk.Tk()
root.title("MathLearn - Learn Quiz!")
root.geometry("400x600")
root.resizable(0, 0)
root.config(bg="#F17720")

Easy_Entry = tk.StringVar()
Moderate_Entry = tk.StringVar()
Advanced_Entry = tk.StringVar()

# Create Navbar and other Formatting Settings
# ---------------------------------------------------------------
options_frame = tk.Frame(root, bg="#EDF8FF", height=100)
options_frame.pack(side=tk.TOP, fill=tk.X)
options_frame.pack_propagate(False)
options_frame.grid_columnconfigure(1, weight=1)
options_frame.grid_columnconfigure(2, weight=1)
options_frame.grid_rowconfigure(0, weight=1)

logo_img = Image.open(os.path.join(BASE_DIR, "MathLearnLogo.png")).convert("RGBA").resize((64, 64))
logo_photo = ImageTk.PhotoImage(logo_img)
logo = tk.Label(options_frame, image=logo_photo, bg="#EDF8FF")
logo.image = logo_photo  # keep a reference
logo.grid(row=0, column=0, padx=(15, 10))

nb1 = tk.Button(options_frame, text="Learn", font=("Roboto", 12, "bold"),
                bg="#EDF8FF", relief=tk.FLAT, command=lambda: LearnPage.tkraise())
nb1.grid(row=0, column=1)

Points_Label = tk.Label(options_frame, text="Points: 0", font=("Roboto", 12, "bold"),
                        bg="#EDF8FF")
Points_Label.grid(row=0, column=2, padx=(0, 15))

# ------------------------------------------------------------- page container
main_frame = tk.Frame(root, bg="#DDE7ED")
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# Creat Learn Page/Frame
LearnPage = tk.Frame(main_frame, bg="#DDE7ED")
LearnPage.grid(row=0, column=0, sticky="NSEW")

# Easy Button
ll1 = tk.Button(LearnPage, text="Easy", width=35, height=5,
                font=("Roboto", 10, "bold"), command=lambda: displayProblem_Easy(True))
ll1.pack(pady=35)

# Moderate Button
ll2 = tk.Button(LearnPage, text="Moderate", width=35, height=5,
                font=("Roboto", 10, "bold"), command=lambda: displayProblem_Moderate(True))
ll2.pack(pady=35)

#Advanced Button
ll3 = tk.Button(LearnPage, text="Advanced", width=35, height=5,
                font=("Roboto", 10, "bold"), command=lambda: displayProblem_Advanced(True))
ll3.pack(pady=35)


# EASY PAGE
# ----------------------------------------------------------------- 
EasyPage = tk.Frame(main_frame, bg=EasyColor)
EasyPage.grid(row=0, column=0, sticky="nsew")

El1 = tk.Label(EasyPage, text="Question 1/10", font=("Roboto", 12, "bold"),
                          bg=EasyColor)
El1.pack(pady=(15, 0))

El2 = tk.Label(EasyPage, text="question here", font=("Roboto", 34, "bold"),
                          bg=EasyColor, width=12, height=3)
El2.pack(pady=15)

Ee1 = tk.Entry(EasyPage, textvariable=Easy_Entry, font=("Roboto", 22),
                      width=10, justify="center")
Ee1.pack(pady=5)

Eb1 = tk.Button(EasyPage, text="Continue", width=20, height=2,
                font=("Roboto", 12, "bold"), bg="#2493DF", fg="white",
                command=isCorrect_Easy)
Eb1.pack(pady=15)

# Moderate PAGE
# ----------------------------------------------------------------- 
ModeratePage = tk.Frame(main_frame, bg=ModerateColor)
ModeratePage.grid(row=0, column=0, sticky="nsew")

Ml1 = tk.Label(ModeratePage, text="Question 1/10", font=("Roboto", 12, "bold"),
                          bg="#EDF8FF")
Ml1.pack(pady=(15, 0))

Ml2 = tk.Label(ModeratePage, text="question here", font=("Roboto", 34, "bold"),
               bg=ModerateColor, width=12, height=3)
Ml2.pack(pady=(15))

Me1 = tk.Entry(ModeratePage, textvariable=Moderate_Entry, font=("Roboto", 22),
               width=10, justify="center")
Me1.pack(pady=5)

Mb1 = tk.Button(ModeratePage, text="Continue", width=20, height=2,
                font=("Roboto", 12, "bold"), bg="#2493DF", fg="white",
                  command=isCorrect_Moderate)
Mb1.pack(pady=15)


# Advanced PAGE
# ----------------------------------------------------------------- 
AdvancedPage = tk.Frame(main_frame, bg=AdvancedColor)
AdvancedPage.grid(row=0, column=0, sticky="nsew")

Al1 = tk.Label(AdvancedPage, text="Question 1/10", font=("Roboto", 12, "bold"),
                          bg="#EDF8FF")
Al1.pack(pady=(15, 0))

Al2 = tk.Label(AdvancedPage, text="question here", font=("Roboto", 34, "bold"),
               bg=AdvancedColor, width=12, height=3)
Al2.pack(pady=15)

Ae1 = tk.Entry(AdvancedPage, textvariable=Advanced_Entry, font=("Roboto", 22),
               width=10, justify="center")
Ae1.pack(pady=5)

Ab1 = tk.Button(AdvancedPage, text="Continue", width=20, height=2,
                font=("Roboto", 12, "bold"), bg="#2493DF", fg="white",
                command=isCorrect_Advanced)
Ab1.pack(pady=15)

LearnPage.tkraise()
# Main Application Tkinter application Loop
root.mainloop()

