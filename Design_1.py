from tkinter import *
from PIL import Image, ImageTk
from random import randint
from tkinter.messagebox import askyesno

# Make Game Window
root = Tk()
root.geometry("1000x500")       # Window Size
root.title("Rock Paper Scissor Game")       # Title of the window
root.configure(bg="skyblue")        # Window Color
icon_of_window = PhotoImage(file="logo.png")     # Path of window icon
root.iconphoto(False, icon_of_window)      # Displaying Icon on Window
root.resizable(False, False)        # To stop window increase or decrease 

# To destroy window
def close():
    comfimation = askyesno(title="Exit", message="Do you want to Exit ?")
    if comfimation:
        root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

# About
about_label = Label(root, text="Ⓒ Copyright 2024 Made by Parveen Biswas", bg="skyblue", font=("Arial 10"))
about_label.place(x=370, y=470)

# Display inside in Window
welcome_text = Label(root, text="Welcome To ROCK PAPER SCISSOR", fon=("monotype 24 bold underline"), fg="blue", bg="skyblue")
welcome_text.pack(pady= 20)

player_label = Label(root, text="PLAYER", font=("monotype 20 bold underline"), bg="skyblue", fg="blue")
player_label.place(x=200, y=90)
computer_label = Label(root, text="COMPUTER", font=("monotype 20 bold underline"), bg="skyblue", fg="blue")
computer_label.place(x=650, y=90)

score_label = Label(root, text="SCORE", font=("monotype 20 bold underline"), bg="skyblue", fg="blue")
score_label.place(x=448, y=150)

player_score = Label(root, text=0, font=("monotype 20 bold"), bg="skyblue", fg="blue")
player_score.place(x=460, y=200)
computer_score = Label(root, text=0, font=("monotype 20 bold"), bg="skyblue", fg="blue")
computer_score.place(x=520, y=200)


# Image for player
player_rock = ImageTk.PhotoImage(Image.open("Rock.png"))
player_paper = ImageTk.PhotoImage(Image.open("Paper.png"))
player_scissor = ImageTk.PhotoImage(Image.open("Scissor.png"))
# Image for computer
computer_rock = ImageTk.PhotoImage(Image.open("Rock-com.png"))
computer_paper = ImageTk.PhotoImage(Image.open("Paper-com.png"))
computer_scissor = ImageTk.PhotoImage(Image.open("Scissor-com.png"))

# display image in player frame
player_display_label = Label(root,image=player_rock, bg="skyblue")
player_display_label.place(x=150, y=130)
# display image in computer frame
computer_display_label = Label(root,image=computer_rock , bg="skyblue")
computer_display_label.place(x=595, y=130)

# result Message
result_message = Label(root, font=("momtype 18 bold"), fg="red", bg="skyblue")
result_message.place(x=380, y=360)

# UpdateMessages
def update_message(x):
    result_message['text'] = x

# Update Player Score
def update_player_score():
    score = int(player_score["text"])
    score += 1
    player_score["text"] = str(score)

# Update Computer Score
def update_computer_score():
    score = int(computer_score["text"])
    score += 1
    computer_score["text"] = str(score)

# player winner
def check_winner(player, computer):
    if player == computer:
        update_message(">>>>>>>TIE!<<<<<<<")
    elif player == "rock":
        if computer == "scissor":
            update_message(">>>>YOU WINS<<<<")
            update_player_score()
        else:
            update_message(">>>>YOU LOSE<<<<")
            update_computer_score()
    elif player == "paper":
        if computer == "rock":
            update_message(">>>>YOU WINS<<<<")
            update_player_score()
        else:
            update_message(">>>>YOU LOSE<<<<")
            update_computer_score()
    elif player == "scissor":
        if computer == "paper":
            update_message(">>>>YOU WINS<<<<")
            update_player_score()
        else:
            update_message(">>>>YOU LOSE<<<<")
            update_computer_score()
    else:
        pass

# computer choices
computer_random_choices = ["rock", "paper", "scissor"]
def get_computer_choices(x):
    #computer choices
    computer_choice = computer_random_choices[randint(0,2)]
    if computer_choice == "rock":
        computer_display_label.configure(image=computer_rock)
    elif computer_choice == "paper":
        computer_display_label.configure(image=computer_paper)
    else:
        computer_display_label.configure(image=computer_scissor)

    # player choices
    if x == "rock":
        player_display_label.configure(image=player_rock)
    elif x == "paper":
        player_display_label.configure(image=player_paper)
    else:
        player_display_label.configure(image=player_scissor)

    check_winner(x, computer_choice)
            
r_button = Button(root, text="Rock", border=2, relief=SOLID, fg="red", bg="white", 
                  activebackground="red", activeforeground="white", font="monotype 15 bold", width=10, command=lambda:get_computer_choices("rock"))
p_button = Button(root, text="Paper", border=2, relief=SOLID, fg="red", bg="white", 
                  activebackground="red", activeforeground="white", font="monotype 15 bold", width=10, command=lambda:get_computer_choices("paper"))
s_button = Button(root, text="Scissor", border=2, relief=SOLID, fg="red", bg="white", 
                  activebackground="red", activeforeground="white", font="monotype 15 bold", width=10, command=lambda:get_computer_choices("scissor"))
r_button.place(x=270,y=400)
p_button.place(x=433,y=400)
s_button.place(x=595,y=400)
              
root.mainloop()