# Import Necessary Libraries
#--------------------------------------------------------------
import tkinter as tk
import random

# Global Variable for background
BG = "#171843"

# Start Function
#--------------------------------------------------------------
def Start():

    # Sets the Reveal button to Hidden and Reset other Values
    revealB.forget()
    revealB.config(text="Reveal")

    # File Handling 
    with open ('randomJokes.txt') as file_handler:
        listofjokes = file_handler.read().splitlines() # Splits Each line of the File

    ran = random.randrange(len(listofjokes)) # Gets a random number based on the max lines
    spt = listofjokes[ran] # Gets the Line based on the randomly generated value
    line = spt.split("?") # Splits the Joke and Punchline by a set value "?"

    joke = line[0] # joke is the first/0 index 
    print(f"{joke}?")
    l1.config(text=f"{joke}?") # sets the main Label to the Joke text

    global punchline
    punchline = line[1] # puncline is the second/1 index
    print(punchline)

    root.after(1500, RevealPunchlineButton) # 1.5s delay for suspense..
    

def RevealPunchlineButton():
    revealB.pack()
    # Reveals revealbutton

def RevealPunchline():
    # when the button is pressed:
    # gets the punchline value and set it to the text value of the reveal button
    revealB.configure(text=punchline)

# Create Root Windows and Other Window Formats Settings
#--------------------------------------------------------------
root = tk.Tk()
root.title("Salexa")
root.geometry('600x300')
root.resizable(0, 0)
root.config(bg=BG)

# Main Alexa Button for Initiating processes
#--------------------------------------------------------------
salexaB = tk.Button(root, text="Smamazon \nSalexa",
                 command=Start,
                 width=18,
                 height=9,
                 bg="#123456",
                 fg="white",
                 activebackground="#131256",
                 font=("Roboto", 10, "bold")
                 )
salexaB.pack(padx=15, pady=15)

# Main Label for displaying first a set example and displaying jokes to be generated
#--------------------------------------------------------------
l1 = tk.Label(root, text='"Salexa Tell me a Joke"',
              bg=BG,
              fg="white",
              font=("Roboto", 15, "bold"))
l1.pack()

# Reveal Button for delivering the punchline. it is hidden at first.
#--------------------------------------------------------------
revealB = tk.Button(root, text="Reveal",
                    font=("Roboto", 15, "bold"),
                    fg="white",
                    bg=BG,
                    command=RevealPunchline)

# Exit Button for exiting the program entirely
#--------------------------------------------------------------
exitB = tk.Button(root, text="Exit",
                  bg="#431717",
                  fg="#BF8B8B",
                  font=("Roboto", 15, "bold"),
                  command=root.destroy)
exitB.place(x=5, y=5, width=100, height=30)

# Runs the whole Tkinter Application Loop window
#--------------------------------------------------------------
root.mainloop()