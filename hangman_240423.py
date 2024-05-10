
'''
BIOBLANKS. This program is an interactive Biology-based 
Hangman game that allows the user to guess a biology-related 
word from a category (molecular biology, physiology, etc.) 
within 6 attempts. 

Requires Python 3 to run. More information about other
dependencies in the requirements.txt file.
'''

#import necessary libraries 

import tkinter as tk
from tkinter import messagebox, BOTH, ROUND
import random
import customtkinter
from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk
import _thread
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from tkinter import Label
from PIL import Image, ImageSequence

#setting the overall appearance + color scheme of interactive elements

customtkinter.set_appearance_mode("dark")


# creating the root window and size of window
root = customtkinter.CTk()
root.geometry("890x800")
root.title("Biology Hangman")
root.config(cursor="heart")

#creating a frame inside the root window
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=0, padx=0, fill="both", expand=False)


# retrieve gif from path and display gif on screen
image_path = "smallkirby.gif"  
img = Image.open(image_path)
img = img.resize((300, 300))  
photo = ImageTk.PhotoImage(img)

image_label = customtkinter.CTkLabel(master=frame, image=photo, text="")  
image_label.image = photo  # reference

#using code snippet of a function to allow gif to play inside ctkinter
# code snippet source: https://gist.github.com/gupta-shantanu/8781f72ff903c2cf3878

class gifplay:

    def __init__(self, label, giffile, delay):
        self.frame = []
        i = 0
        while True:
            try:
                image = PhotoImage(file=giffile, format="gif -index " + str(i))
                self.frame.append(image)
                i += 1
            except:
                break
        print(i)
        self.totalFrames = i - 1
        self.delay = delay
        self.labelspace = label
        self.labelspace.configure(image=self.frame[0])  # Update the label image initially

    def play(self):
        _thread.start_new_thread(self.infinite, ())

    def infinite(self):
        i = 0
        while True:
            self.labelspace.configure(image=self.frame[i])
            i = (i + 1) % self.totalFrames
            time.sleep(self.delay)


    def play(self):
        _thread.start_new_thread(self.infinite,())

    def infinite(self):
        i = 0
        while 1:
            self.labelspace.configure(image=self.frame[i])
            i = (i + 1) % self.totalFrames
            time.sleep(self.delay)

# gif path
gif_path = "smallkirby.gif"

# tkinter main loop for gif
gif_player = gifplay(image_label, gif_path, 0.1)
gif_player.play()

# list of words for the game
words_lower = [
    "glucose",
    "atp",
    "cytoplasm",
    "mitochondria",
    "water",
    "oxygen",
    "dna",
    "transcription",
    "translation",
    "physiology",
    "muscle",
    "myocardium",
    "protein",
    "transcriptase",
    "hemoglobin",
    "signal",
    "substrate",
    "bacteria",
    "antibody",
    "microbiome"
]

# dictionary of words for the game that includes word + category

words_defs = {
    "glucose": "Metabolism",
    "atp": "Energy",
    "cytoplasm": "Cellular Structure",
    "mitochondria": "Cellular Organelles",
    "water": "Biochemistry",
    "oxygen": "Respiration",
    "dna": "Genetics",
    "transcription": "Gene Expression",
    "translation": "Protein Synthesis",
    "physiology": "Human Anatomy",
    "muscle": "Muscular System",
    "myocardium": "Cardiovascular System",
    "protein": "Macromolecules",
    "transcriptase": "Enzymes",
    "hemoglobin": "Blood",
    "signal": "Cell Signaling",
    "substrate": "Biochemical Reactions",
    "bacteria": "Microorganisms",
    "antibody": "Immune System",
    "microbiome": "Microbial Ecology"
}

#words + definitions

words_definitions = {
    "glucose": "primary source of energy",
    "atp": "energy currency of the cell",
    "cytoplasm": "fluid inside cells",
    "mitochondria": "powerhouse of the cell",
    "water": "universal solvent",
    "oxygen": "essential for respiration",
    "dna": "genetic material",
    "transcription": "DNA to RNA synthesis",
    "translation": "RNA to protein synthesis",
    "physiology": "study of body function",
    "muscle": "tissue for movement",
    "myocardium": "heart muscle",
    "protein": "macromolecule made of amino acids",
    "transcriptase": "enzyme that synthesizes RNA",
    "hemoglobin": "protein in red blood cells",
    "signal": "molecule that carries information",
    "substrate": "reactant in an enzyme-catalyzed reaction",
    "bacteria": "microscopic organisms",
    "antibody": "immune system protein",
    "microbiome": "collection of microorganisms in a particular environment"

}


# initialize variables

word_to_guess = random.choice(words_lower)
guessed_letters = []  # keeps track of guessed letters
attempts = 6  # number of allowed guesses before game ends
w = 0
l = 0

stats = {
    'wins':0, 
    'losses':0, 
    'streak':0, 
    }

# function to check if the game is over
def is_game_over():
    return check_win() or check_lost()

# check if the player has won
def check_win():
    return all(letter in guessed_letters for letter in word_to_guess)

# check if the player has lost
def check_lost():
    return attempts == 0

# create a label to display guessed letters

guessed_letters_label = tk.Label(root, text="Guessed Letters: ", font=("Cambria", 16),bg="#252424",fg="#ffffff")
guessed_letters_display = tk.Label(root, text="", font=("Cambria", 16))

guessed_letters_label = tk.Label(root, text="Guessed Letters: ", font=("ComicSansMS", 16), bg="#252424", fg="#ffffff")
guessed_letters_display = tk.Label(root, text="", font=("ComicSansMS", 16))


# win popup

def win_popup():
    # new toplevel window for the custom popup
    win_popup_window = tk.Toplevel(root)
    win_popup_window.title("You win!")
    win_popup_window.geometry("300x300")
    win_popup_window.resizable(False, False)

    # custom message
    win_message = "You win! The word was: " + previous_word_to_guess

    #creating a frame inside the pop up window
    win_frame = customtkinter.CTkFrame(master=win_popup_window)
    win_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # retrieve gif from path and display gif on screen
    win_gif_path = "win_kirby.gif"
    win_img = Image.open(win_gif_path)
    win_img = win_img.resize((140, 140))  
    win_photo = ImageTk.PhotoImage(win_img)

    win_image_label = customtkinter.CTkLabel(master=win_frame, image=win_photo, text="")  
    win_image_label.image = win_photo  # reference
    win_image_label.pack()

    # tkinter loop for you win gif
    win_gif_player = gifplay(win_image_label, win_gif_path, 0.1)
    win_gif_player.play()

    #  label to display the message
    win_message_label = tk.Label(win_popup_window, text=win_message, font=("Cambria", 14))
    win_message_label.pack()
    # close button
    close_button = customtkinter.CTkButton(win_popup_window, text="Close", fg_color="#d74894", command=win_popup_window.destroy)
    close_button.pack(pady=10)

    # display pop up
    win_popup_window.mainloop()


#loss popup 

def loss_popup():
    # new toplevel window for the custom popup
    print("Loss popup called")
    loss_popup_window = tk.Toplevel(root)
    loss_popup_window.title("You lose!")
    loss_popup_window.geometry("300x300")
    loss_popup_window.resizable(False, False)

    # custom message
    lose_message = ("You lose! The word was: " + previous_word_to_guess)

    #creating a frame inside the pop up window
    lose_frame = customtkinter.CTkFrame(master=loss_popup_window)
    lose_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # retrieve gif from path and display gif on screen
    lose_gif_path = "lost_kirby.gif"
    lose_img = Image.open(lose_gif_path)
    lose_img = lose_img.resize((140, 140))  
    lose_photo = ImageTk.PhotoImage(lose_img)

    lose_image_label = customtkinter.CTkLabel(master=lose_frame, image=lose_photo, text="")  
    lose_image_label.image = lose_photo  # Reference
    lose_image_label.pack()

    # tkinter loop for you win gif
    lose_gif_player = gifplay(lose_image_label, lose_gif_path, 0.1)
    lose_gif_player.play()

    #  label to display the message
    lose_message_label = tk.Label(loss_popup_window, text=lose_message, font=("Cambria", 14))
    lose_message_label.pack()
    # close button
    lose_close_button = customtkinter.CTkButton(loss_popup_window, text="Close", fg_color="#d74894", command=loss_popup_window.destroy)
    lose_close_button.pack(pady=10)

 
    # display pop up
    loss_popup_window.mainloop()

# invalid error pop up

def show_invalid_input_popup():
    # new toplevel window for the custom popup
    popup_window = tk.Toplevel(root)
    popup_window.title("Invalid Input")
    popup_window.geometry("300x300")
    popup_window.resizable(False, False)

    error_frame = customtkinter.CTkFrame(master=popup_window)  # use popup_window as master
    error_frame.pack(pady=10, padx=10, fill="both", expand=True)

    error_image_path = "madkirby.png.png"  
    error_img = Image.open(error_image_path)
    error_img = error_img.resize((140, 140))  
    error_photo = ImageTk.PhotoImage(error_img)

    error_image_label = customtkinter.CTkLabel(master=error_frame, image=error_photo, text="")  
    error_image_label.image = error_photo  # reference
    error_image_label.pack()

    # custom message
    message = "Please enter a single letter!"

    #  label to display the message
    message_label = tk.Label(popup_window, text=message, font=("Cambria", 24))
    message_label.pack()
    # close button
    close_button = customtkinter.CTkButton(popup_window, text="Close", fg_color="#d74894", command=popup_window.destroy)
    close_button.pack(pady=10)

    # centering the pop up
    popup_window.update_idletasks()
    width = popup_window.winfo_width()
    height = popup_window.info_height()
    x = (popup_window.winfo_screenwidth() // 2) - (width // 2)
    y = (popup_window.winfo_screenheight() // 2) - (height // 2)
    popup_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # display pop up
    popup_window.mainloop()
    
# you already guessed this letter error popup

def guessed_popup():
    # new toplevel window for the custom popup
    popup_window = tk.Toplevel(root)
    popup_window.title("Invalid Input")
    popup_window.geometry("300x300")
    popup_window.resizable(False, False)

    error_frame = customtkinter.CTkFrame(master=popup_window)  # use popup_window as master
    error_frame.pack(pady=10, padx=10, fill="both", expand=True)

    error_image_path = "madkirby.png.png"  
    error_img = Image.open(error_image_path)
    error_img = error_img.resize((140, 140))  
    error_photo = ImageTk.PhotoImage(error_img)

    error_image_label = customtkinter.CTkLabel(master=error_frame, image=error_photo, text="")  
    error_image_label.image = error_photo  # reference
    error_image_label.pack()

    # custom message
    message = "You already guessed this letter!"

    #  label to display the message
    message_label = tk.Label(popup_window, text=message, font=("Cambria", 20))
    message_label.pack()
    # close button
    close_button = customtkinter.CTkButton(popup_window, text="Close", fg_color="#d74894", command=popup_window.destroy)
    close_button.pack(pady=10)

    # centering the pop up
    popup_window.update_idletasks()
    width = popup_window.winfo_width()
    height = popup_window.info_height()
    x = (popup_window.winfo_screenwidth() // 2) - (width // 2)
    y = (popup_window.winfo_screenheight() // 2) - (height // 2)
    popup_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # display pop up
    popup_window.mainloop()
    

#binding 'return' to event object, and passing event through guess_letter function

root.bind('<Return>', lambda event: guess_letter())

# checks if letters match word
def guess_letter(event=None):
    global attempts  # access and modify variable
    letter = letter_entry.get().lower()  # convert to lowercase and store in variable
    if letter.isalpha() and len(letter) == 1:  # check if valid single character
        if letter in guessed_letters:  # if already guessed
            guessed_popup()
        else:
            guessed_letters.append(letter)
            update_guessed_letters_display()  # update guessed letters display
            if letter in word_to_guess: #compare letter to word
                update_word_display()
                if check_win():
                    stats['wins'] += 1
                    stats['streak'] += 1
                    #messagebox.showinfo("Hangman", "Congratulations! You win!")
                    #win_popup()   #call win popup after updating stats
                    reset_game()
                    win_popup()  
            else:
                attempts -= 1
                update_attempts_display()
                draw_hangman()
                if check_lost():
                    stats['losses'] += 1
                    stats['streak'] = 0
                    #messagebox.showinfo("Hangman", "You lose! The word was: " + word_to_guess)
                    reset_game()
                    loss_popup()  
                    reset_game()
                    #stats['losses'] += 1
                    #stats['streak'] = 0
        letter_entry.delete(0, tk.END)  # clears the input field
    else:
        show_invalid_input_popup()

# reset game

def reset_game():
    global word_to_guess, guessed_letters, attempts, previous_word_to_guess #word_current  # modifies global variables
    previous_word_to_guess = word_to_guess
    word_to_guess = random.choice(words_lower)  # randomly selects from list and assigns to global variable
    guessed_letters = []  # initializes empty list, clearing previous guesses
    attempts = 6
    update_word_display()  # updates game interface
    update_attempts_display()  # updates game interface
    draw_hangman()
    guessed_letters_label.config(text="Guessed Letters: ")  # update guessed letters label
    guessed_letters_display.config(text="")  # clear guessed letters display


def show_definition():
    word_current = word_to_guess.lower()
    if word_current in words_defs:
        hint_display.config(text=words_definitions[word_current])
    else:
        hint_display.config(text="No definition available")

# function to update word display

def update_word_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "__"
        display_word += " "
    word_label.config(text=display_word,bg="#252424",fg="#ffffff")
    if word_to_guess.lower() in words_defs:
        hint_display.config(text=words_defs[word_to_guess.lower()])
    else:
        hint_display.config(text = "No category available")


#make df for wins and losses

df = pd.DataFrame(list(stats.items()), columns=['labels', 'value'])
sdf = df[["value"]]
tdf = df[["labels"]]

#make dictionary of wins and losses into a string

for key in stats.keys():
    numbers = stats[key]
    print(numbers)

#show stats screen

def show_stats():
    popup = tk.Tk()
    popup.wm_title("Game Summary")
    popup.geometry("520x520+300+200")

    label = tk.Label(popup, text="Game Summary", font='Cambria')
    label.pack(side="top", fill="x", pady=10)

    wins_loss = tk.Label(popup, text='', font='Cambria')
    wins_loss['text'] = '\n'.join('{} {}'.format(k, d) for k, d in stats.items())
    wins_loss.pack(side="top", fill="x", pady=10)

    B1 = tk.Button(popup, text="Okay", font="Cambria", command = popup.destroy)
    B1.pack()

    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.pie([stats['wins'], stats['losses']], labels=['Wins', 'Losses'], autopct='%1.1f%%', startangle=140)
    ax.axis('equal')

    chart1 = FigureCanvasTkAgg(fig, master=popup)
    chart1.draw()
    chart1.get_tk_widget().pack()

    #chart1 = FigureCanvasTkAgg(fig,popup)
    #chart1.get_tk_widget().pack()

    popup.mainloop()

# function to update attempts display
def update_attempts_display():

    attempts_label.config(text=f"Attempts left: {attempts}", font=("Cambria", 16),bg="#252424")

    attempts_label.config(text=f"Attempts left: {attempts}", font=("ComicSansMS", 16),bg="#252424",fg="#ffffff")


# function to update guessed letters display
def update_guessed_letters_display():
    guessed_letters_display.config(text=" ".join(guessed_letters))
# function to draw the hangman figure
def draw_hangman():
    canvas.delete("hangman")
    if attempts < 6:
        canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman")  # Head
    if attempts < 5:
        canvas.create_line(150, 175, 150, 225, width=4, tags="hangman")  # Body
    if attempts < 4:
        canvas.create_line(150, 175, 125, 200, width=4, tags="hangman")  # Left arm
    if attempts < 3:
        canvas.create_line(150, 175, 175, 200, width=4, tags="hangman")  # Right arm
    if attempts < 2:
        canvas.create_line(150, 225, 125, 250, width=4, tags="hangman")  # Left leg
    if attempts < 1:
        canvas.create_line(150, 225, 175, 250, width=4, tags="hangman")  # Right leg

# create GUI elements

#labels
word_label = tk.Label(root, text="", font=("Cambria", 24))
attempts_label = tk.Label(root, text="", font=("Cambria", 16))
hint_display = tk.Label(root, text = "", font = ("Cambria", 24), wraplength=700,bg="#252424",fg="#ffffff")
hint_display = tk.Label(root, text = "", font = ("Comic Sans", 24), wraplength=700,bg="#252424",fg="#ffffff")

#entry
letter_entry = tk.Entry(root, width=5, font=("Cambria", 16),highlightbackground="pink", highlightcolor="pink")

#permanent canvas elements (hangman post and beam)
canvas = customtkinter.CTkCanvas(root, width=250, height=260)
canvas.create_line(50, 250, 250, 250, width=4)# Base line
canvas.create_line(200, 250, 200, 100, width=4)# Post
canvas.create_line(100, 100, 200, 100, width=4)# Beam
canvas. create_line(150, 100, 150, 120, width=4)# Beam
canvas.config(bg="pink") 

#buttons

guess_button = customtkinter.CTkButton(root, text="GUESS", command=guess_letter, font=("Cambria", 16),fg_color="#d74894")
reset_button = customtkinter.CTkButton(root, text="RESET", command=reset_game, font=("Cambria", 16),fg_color="#d74894")
stats_button = customtkinter.CTkButton(root, text="Game stats", command=show_stats,fg_color="#5e1147")
definition_button = customtkinter.CTkButton(root, text="Reveal definition", command=show_definition, font=("Cambria", 16), fg_color="#d74894")

#frame for title plus image paths and labels
title_frame = customtkinter.CTkFrame(master=root)  # use popup_window as master
title_frame.pack(pady=10, padx=10, fill="both", expand=True)
#title_frame.resizable(False, False)
title_image_path = "bioblanks.png"  
title_img = Image.open(title_image_path)
title_img = title_img.resize((200, 70))  
title_photo = ImageTk.PhotoImage(title_img)

# error image labels
error_image_label = customtkinter.CTkLabel(master=title_frame, image=title_photo, text="",width=200, height=70)  
error_image_label.image = title_photo  # reference
error_image_label.pack()

# pack GUI elements


hint_display.pack()
definition_button.pack()
canvas.pack()
word_label.pack()
attempts_label.pack()
letter_entry.pack()
guessed_letters_label.pack()
guessed_letters_display.pack()
guess_button.pack()
reset_button.pack(pady=12, padx=10)
stats_button.pack()
image_label.pack()


# initial display
update_word_display()
update_attempts_display()
draw_hangman()

#run the window
root.mainloop()
