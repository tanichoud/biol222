import tkinter as tk
from tkinter import messagebox
from tkinter import BOTH, ROUND
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
from matplotlib.backend_bases import key_press_handler


#pygame.mixer.init()

#def play():
    #pygame.mixer.music.load("background_music.mp3")
    #pygame.mixer.music.play(loops=-1)

#def stop():
    #pygame.mixer.music.stop()

#setting the overall appearance + color scheme of interactive elements
customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("green")

# creating the root window and size of window
root = customtkinter.CTk()
root.geometry("1200x500")
root.title("Biology Hangman")
#root.iconbitmap('c:/guis/exe/codemy.ico')
root.config(cursor="heart")



#creating a frame inside the root window
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#play and pause button frames
#button_frame = tk.Frame(root)
#button_frame.pack(pady=10) 

# retrieve gif from path and display gif on screen
image_path = "smallkirby.gif"  
img = Image.open(image_path)
img = img.resize((140, 140))  
photo = ImageTk.PhotoImage(img)

image_label = customtkinter.CTkLabel(master=frame, image=photo, text="")  # Set the text color
image_label.image = photo  # Reference
image_label.pack(pady=12, padx=10)

#using code snippet of a function to allow gif to play inside ctkinter

class gifplay:
    """
    Usage: mygif=gifplay(<<tkinter.label Objec>>,<<GIF path>>,<<frame_rate(in ms)>>)
    example:
    gif=GIF.gifplay(self.model2,'./res/neural.gif',0.1)
    gif.play()
    This will play gif infinitely
    """
    def __init__(self, label, giffile, delay):
        self.frame = []
        i = 0
        while 1:
            try:
                image = PhotoImage(file=giffile, format="gif -index "+str(i))
                self.frame.append(image)
                i = i + 1
            except:
                break
        print(i)
        self.totalFrames = i - 1
        self.delay = delay
        self.labelspace = label
        self.labelspace.image = self.frame[0]
        desired_width = 100
        desired_height = 100


    def play(self):
        """
        plays the gif
        """
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
    "carbondioxide",
    "water",
    "electrons",
    "oxygen"
]

words_defs = {
    "glucose": "sugar produced during photosynthesis",
    "atp": "energy",
    "cytoplasm": "extracellular and intracelluar",
    "mitochondria": "powerhouse of the cell",
    "carbondioxide": "gas we breathe out",
    "water":"wada",
    "electrons": "negatively charged particles",
    "oxygen": "gas we breathe in"
}


# initialize variables
word_to_guess = random.choice(words_lower)
guessed_letters = []  # Keeps track of guessed letters
attempts = 6  # Number of allowed guesses before game ends
w = 0
l = 0

stats = {
    'wins':5, 
    'losess':5, 
    'streak':2, 
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
guessed_letters_label = tk.Label(root, text="Guessed Letters: ", font=("ComicSansMS", 12))
guessed_letters_display = tk.Label(root, text="", font=("ComicSansMS", 12))

# checks if letters match word
def guess_letter():
    global attempts  # access and modify variable
    letter = letter_entry.get().lower()  # convert to lowercase and store in variable
    if letter.isalpha() and len(letter) == 1:  # check if valid single character
        if letter in guessed_letters:  # if already guessed
            messagebox.showinfo("Hangman", "You already guessed this letter.")
        else:
            guessed_letters.append(letter)
            update_guessed_letters_display()  # update guessed letters display
            if letter in word_to_guess: #compare letter w word
                update_word_display()
                if check_win():
                    messagebox.showinfo("Hangman", "Congratulations! You win!")
                    stats['wins'] += 1
                    stats['streak'] += 1
                    reset_game()
            else:
                attempts -= 1
                update_attempts_display()
                draw_hangman()
                if check_lost():
                    messagebox.showinfo("Hangman", "You lose! The word was: " + word_to_guess)
                    #tats['losses'] += 1
                    #stats['streak'] = 0
                    reset_game()
        letter_entry.delete(0, tk.END)  # clears the input field
    else:
        messagebox.showinfo("Hangman", "Please enter a single letter.")  # if not a valid letter

# Reset game
def reset_game():
    global word_to_guess, guessed_letters, attempts, word_current  # modifies global variables
    word_to_guess = random.choice(words_lower)  # randomly selects from list and assigns to global variable
    guessed_letters = []  # initializes empty list, clearing previous guesses
    attempts = 6
    update_word_display()  # updates game interface
    update_attempts_display()  # updates game interface
    draw_hangman()
    guessed_letters_label.config(text="Guessed Letters: ")  # update guessed letters label
    guessed_letters_display.config(text="")  # clear guessed letters display

# function to update word display
def update_word_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "__"
        display_word += " "
    word_label.config(text=display_word)
    if word_to_guess.lower() in words_defs:
        hint_display.config(text=words_defs[word_to_guess.lower()])
    else:
        hint_display.config(text = "test")

def show_definition():
    word_current = word_to_guess.lower()
    if word_current in words_defs:
        hint_display.config(text=words_defs[word_current])
    else:
        hint_display.config(text="test")

#make df for wins and losses
df = pd.DataFrame(list(stats.items()), columns=['label', 'value'])
sdf = df[["value"]]

def show_stats():
    popup = tk.Tk()
    popup.wm_title("Game Summary")
    popup.geometry("520x520+300+200")

    label = tk.Label(popup, text="Game Summary", font='Arial')
    label.pack(side="top", fill="x", pady=10)

    wins_loss = tk.Label(popup, text='')
    wins_loss['text'] = '\n'.join('{} {}'.format(k, d) for k, d in stats.items()) 
    wins_loss.pack(side="top", fill="x", pady=10)

    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()

    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, popup)
    chart_type.get_tk_widget().pack()
    plot = sdf.plot.pie( subplots=True, figsize=(11, 6))
    
    popup.mainloop()

# function to update attempts display
def update_attempts_display():
    attempts_label.config(text=f"Attempts left: {attempts}", font=("ComicSansMS", 12))

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
word_label = tk.Label(root, text="", font=("Arial", 24))
attempts_label = tk.Label(root, text="", font=("Arial", 16))
letter_entry = tk.Entry(root, width=5, font=("Arial", 16))
#guess_button = tk.Button(root, text="Guess", command=guess_letter, pady=12, padx=10)
#reset_button = tk.Button(root, text="Reset", command=reset_game)
#hint_button = customtkinter.CTkButton(root, text="Hint", command=show_definition, font=("ComicSansMS", 12),fg_color="#d74894")
hint_display = tk.Label(root, text = "", font = ("Arial", 24), wraplength=700)
canvas = customtkinter.CTkCanvas(root, width=700, height=300)
canvas.config(bg="pink") 
guess_button = customtkinter.CTkButton(root, text="Guess", command=guess_letter, font=("ComicSansMS", 12),fg_color="#d74894")
reset_button = customtkinter.CTkButton(root, text="Reset", command=reset_game, font=("ComicSansMS", 12),fg_color="#d74894")
#hint_display = tk.Label(root, text = "", font = ("Arial", 24), wraplength=700)
#hint_button = customtkinter.CTkButton(root, text="Hint", command=show_definition, font=("ComicSansMS", 12),fg_color="#d74894")
#hint_button = tk.Button(root, text = "get hint", command = show_definition)
label = customtkinter.CTkLabel(root, text="Biology Hangman", font=("ComicSansMS", 24))
label.pack(pady=12, padx=10)
#play_button = customtkinter.CTkButton(button_frame, text="▷",width=2, command=play,font=("ComicSansMS", 12),fg_color="#d74894")
#play_button.pack(side="left")
#stop_button = customtkinter.CTkButton(button_frame, text="||", width=2,command=stop,font=("ComicSansMS", 12),fg_color="#d74894")
#stop_button.pack(side="left")
stats_button = customtkinter.CTkButton(root, text="Game stats", command=show_stats)


# pack GUI elements
hint_display.pack()
#hint_button.pack()
canvas.pack()
word_label.pack()
attempts_label.pack()
letter_entry.pack()
guess_button.pack()
reset_button.pack()
guessed_letters_label.pack()
guessed_letters_display.pack()
stats_button.pack()


# initial display
update_word_display()
update_attempts_display()
draw_hangman()

#run the window
root.mainloop()
