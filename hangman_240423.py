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
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
from tkinter import Label
from PIL import Image, ImageSequence

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
root.geometry("500x900")
root.title("Biology Hangman")
#root.iconbitmap('c:/guis/exe/codemy.ico')
root.config(cursor="heart")


#creating a frame inside the root window
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=0, padx=0, fill="both", expand=False)

#play and pause button frames
#button_frame = tk.Frame(root)
#button_frame.pack(pady=10) 

# retrieve gif from path and display gif on screen
image_path = "smallkirby.gif"  
img = Image.open(image_path)
img = img.resize((300, 300))  
photo = ImageTk.PhotoImage(img)

image_label = customtkinter.CTkLabel(master=frame, image=photo, text="")  
image_label.image = photo  # Reference

#using code snippet of a function to allow gif to play inside ctkinter

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
        """
        Plays the GIF infinitely.
        """
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
guessed_letters_label = tk.Label(root, text="Guessed Letters: ", font=("ComicSansMS", 16))
guessed_letters_display = tk.Label(root, text="", font=("ComicSansMS", 16))

# error pop up

def show_invalid_input_popup():
    # new toplevel window for the custom popup
    popup_window = tk.Toplevel(root)
    popup_window.title("Invalid Input")
    popup_window.geometry("300x300")
    popup_window.resizable(False, False)

    error_frame = customtkinter.CTkFrame(master=popup_window)  # Use popup_window as master
    error_frame.pack(pady=10, padx=10, fill="both", expand=True)

    error_image_path = "madkirby.png.png"  
    error_img = Image.open(error_image_path)
    error_img = error_img.resize((140, 140))  
    error_photo = ImageTk.PhotoImage(error_img)

    error_image_label = customtkinter.CTkLabel(master=error_frame, image=error_photo, text="")  
    error_image_label.image = error_photo  # Reference
    error_image_label.pack()

    # custom message
    message = "Please enter a single letter!"

    #  label to display the message
    message_label = tk.Label(popup_window, text=message, font=("Comic Sans", 24))
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
    
# you already guessed this letter

# error pop up

def guessed_popup():
    # new toplevel window for the custom popup
    popup_window = tk.Toplevel(root)
    popup_window.title("Invalid Input")
    popup_window.geometry("300x300")
    popup_window.resizable(False, False)

    error_frame = customtkinter.CTkFrame(master=popup_window)  # Use popup_window as master
    error_frame.pack(pady=10, padx=10, fill="both", expand=True)

    error_image_path = "madkirby.png.png"  
    error_img = Image.open(error_image_path)
    error_img = error_img.resize((140, 140))  
    error_photo = ImageTk.PhotoImage(error_img)

    error_image_label = customtkinter.CTkLabel(master=error_frame, image=error_photo, text="")  
    error_image_label.image = error_photo  # Reference
    error_image_label.pack()

    # custom message
    message = "You already guessed this letter!"

    #  label to display the message
    message_label = tk.Label(popup_window, text=message, font=("Comic Sans", 20))
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
    



def win_popup():
    # new toplevel window for the custom popup
    win_popup_window = tk.Toplevel(root)
    win_popup_window.title("You win!")
    win_popup_window.geometry("300x300")
    win_popup_window.resizable(False, False)

    # custom message
    message = "You win!"

    #creating a frame inside the pop up window
    win_frame = customtkinter.CTkFrame(master=win_popup_window)
    win_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # retrieve gif from path and display gif on screen
    win_gif_path = "win_kirby.gif"
    win_img = Image.open(win_gif_path)
    win_img = win_img.resize((140, 140))  
    win_photo = ImageTk.PhotoImage(win_img)

    win_image_label = customtkinter.CTkLabel(master=win_frame, image=win_photo, text="")  
    win_image_label.image = win_photo  # Reference
    win_image_label.pack()

    # tkinter loop for you win gif
    win_gif_player = gifplay(win_image_label, win_gif_path, 0.1)
    win_gif_player.play()

    #  label to display the message
    message_label = tk.Label(win_popup_window, text=message, font=("Comic Sans", 24))
    message_label.pack()
    # close button
    close_button = customtkinter.CTkButton(win_popup_window, text="Close", fg_color="#d74894", command=win_popup_window.destroy)
    close_button.pack(pady=10)

    # centering the pop up
    win_popup_window.update_idletasks()
    width = win_popup_window.winfo_width()
    height = win_popup_window.winfo_height()  # Update this line
    x = (win_popup_window.winfo_screenwidth() // 2) - (width // 2)
    y = (win_popup_window.winfo_screenheight() // 2) - (height // 2)
    win_popup_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # display pop up
    win_popup_window.mainloop()




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
            if letter in word_to_guess: #compare letter w word
                update_word_display()
                if check_win():
                    reset_game()
                    win_popup()
            else:
                attempts -= 1
                update_attempts_display()
                draw_hangman()
                if check_lost():
                    messagebox.showinfo("Hangman", "You lose! The word was: " + word_to_guess)
                    reset_game()
        letter_entry.delete(0, tk.END)  # clears the input field
    else:
       show_invalid_input_popup()



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

def graph():
    fig = Figure(figsize = (5, 5), dpi = 100)
    y = [i**2 for i in range(101)] 
    plot1 = fig.add_subplot(111) 
    plot1.plot(y)
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 

def show_stats():
    tk.messagebox.showinfo("Game Summary",  "Wins and losses this session") 

# function to update attempts display
def update_attempts_display():
    attempts_label.config(text=f"Attempts left: {attempts}", font=("ComicSansMS", 16))

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
word_label = tk.Label(root, text="", font=("Comic Sans", 24))
attempts_label = tk.Label(root, text="", font=("Comic Sans", 16))
letter_entry = tk.Entry(root, width=5, font=("Comic Sans", 16))
#guess_button = tk.Button(root, text="Guess", command=guess_letter, pady=12, padx=10)
#reset_button = tk.Button(root, text="Reset", command=reset_game)
#hint_button = customtkinter.CTkButton(root, text="Hint", command=show_definition, font=("ComicSansMS", 12),fg_color="#d74894")
hint_display = tk.Label(root, text = "", font = ("Comic Sans", 24), wraplength=700)
canvas = customtkinter.CTkCanvas(root, width=250, height=260)
canvas.create_line(50, 250, 250, 250, width=4)# Base line
canvas.create_line(200, 250, 200, 100, width=4)# Post
canvas.create_line(100, 100, 200, 100, width=4)# Beam
canvas. create_line(150, 100, 150, 120, width=4)# Beam
canvas.config(bg="pink") 


guess_button = customtkinter.CTkButton(root, text="GUESS", command=guess_letter, font=("ComicSansMS", 16),fg_color="#d74894")
reset_button = customtkinter.CTkButton(root, text="RESET", command=reset_game, font=("ComicSansMS", 16),fg_color="#d74894")
#hint_display = tk.Label(root, text = "", font = ("Arial", 24), wraplength=700)
#hint_button = customtkinter.CTkButton(root, text="Hint", command=show_definition, font=("ComicSansMS", 12),fg_color="#d74894")
#hint_button = tk.Button(root, text = "get hint", command = show_definition)
label = customtkinter.CTkLabel(root, text="BioBlanks", font=("ComicSansMS", 30))
label.pack(pady=12, padx=10)
#play_button = customtkinter.CTkButton(button_frame, text="▷",width=2, command=play,font=("ComicSansMS", 12),fg_color="#d74894")
#play_button.pack(side="left")
#stop_button = customtkinter.CTkButton(button_frame, text="||", width=2,command=stop,font=("ComicSansMS", 12),fg_color="#d74894")
#stop_button.pack(side="left")
stats_button = customtkinter.CTkButton(root, text="Game stats", command=show_stats,fg_color="#5e1147")


# pack GUI elements

image_label.pack()
hint_display.pack()
#hint_button.pack()
canvas.pack()
word_label.pack()
attempts_label.pack()
letter_entry.pack()
guessed_letters_label.pack()
guessed_letters_display.pack()
guess_button.pack()
reset_button.pack(pady=12, padx=10)
stats_button.pack(pady=12, padx=10)

# initial display
update_word_display()
update_attempts_display()
draw_hangman()

#run the window
root.mainloop()
