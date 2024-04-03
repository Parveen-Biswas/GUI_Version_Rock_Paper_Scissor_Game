from tkinter import *
from PIL import ImageTk,Image
from random import randint
from tkinter.messagebox import askyesno

root = Tk()
root.geometry("600x600+200+100")        # window size with position computer display
root.title("ROCK PAPER SCISSOR")        # Title of window
icon_image = ImageTk.PhotoImage(Image.open("logo.png"))      # path of image
root.iconphoto(False, icon_image)       # icon of the window
root.configure(bg="#69EEFB")        # background of the window
root.resizable(False,False)     # stop increase or decrease the window

# To destroy window
def close():
    comfimation = askyesno(title="Exit", message="Do you want to Exit ?")
    if comfimation:
        root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

# About owner
about_label = Label(root, text="Ⓒ Copyright 2024 Made by Parveen Biswas", bg="#69EEFB", font=("Arial 10"))
about_label.place(x=185, y=570)

# Welcome Label
welcome_label = Label(root, text="Welcom To Rock Paper Scissor Game", bg="#69EEFB", fg="red", font=("Arial 18 bold underline"))
welcome_label.pack(pady=30)
# Player Label
player_label = Label(root, text="PLAYER", bg="#69EEFB", fg="blue", font=("Arial 16 bold underline"))
player_label.place(x=82, y=90)
# Computer Label
computer_label = Label(root, text="COMPUTER", bg="#69EEFB", fg="blue", font=("Arial 16 bold underline"))
computer_label.place(x=395, y=90)
# Score Label
score_label = Label(root, text="SCORE", bg="#69EEFB", fg="blue", font=("Arial 16 bold underline"))
score_label.place(x=265, y=430)
# Player Score Label
player_score = Label(root, text=0, bg="#69EEFB", fg="blue", font=("Arial 18 bold"))
player_score.place(x=120, y=430)
# Computer Score Label
computer_score = Label(root, text=0, bg="#69EEFB", fg="blue", font=("Arial 18 bold"))
computer_score.place(x=460, y=430)
# test image
test_image = ImageTk.PhotoImage(Image.open("Rock.png"))
test_lab = Label(root, image=test_image, bg="#69EEFB")
test_lab.place(x=5, y=140)
test_lab2 = Label(root, image=test_image, bg="#69EEFB")
test_lab2.place(x=340,y=140)
# Import image for game
rock_img = ImageTk.PhotoImage(Image.open("Rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Scissor.png"))
rock_com_img = ImageTk.PhotoImage(Image.open("Rock-com.png"))
paper_com_img = ImageTk.PhotoImage(Image.open("Paper-com.png"))
scissor_com_img = ImageTk.PhotoImage(Image.open("Scissor-com.png"))

message_label = Label(root, bg="#69EEFB", fg="red", font="Arial 16 bold")       # text=">>>>You Wins<<<<"
message_label.place(x=200, y=390)                                               # text=">>>>>>TIE!<<<<<<"

# Update Messages
def update_message(x):
    message_label["text"] = x

# Update Player Score
def update_player_score():
    score = player_score["text"]
    score += 1
    player_score["text"] = str(score)

# Update Computer Score
def update_computer_score():
    score = computer_score["text"]
    score += 1
    computer_score["text"] = str(score)

# Player Winner
def check_winner(player, computer):
    if player == computer:
        update_message(">>>>>>TIE!<<<<<<")
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

# computer choice
choices = ["rock", "paper", "scissor"]
def computer_random_choice(x):
    # computer
    computer_choice = choices[randint(0,2)]
    if computer_choice == "rock":
        test_lab2.configure(image=rock_com_img)
    elif computer_choice == "paper":
        test_lab2.configure(image=paper_com_img)
    else:
        test_lab2.configure(image=paper_com_img)

    # player
    if x == "rock":
        test_lab.configure(image=rock_img)
    elif x == "paper":
        test_lab.configure(image=paper_img)
    else:
        test_lab.configure(image=scissor_img)

    check_winner(x, computer_choice)
            

# Button For Action
rock_button = Button(root, text="ROCK", font=("Arial 14 bold"), fg="red", activeforeground="white", activebackground="red", width=12, height=1, border=2, relief=SOLID,
                     command=lambda:computer_random_choice("rock"))
rock_button.place(x=60, y=480)
paper_button = Button(root, text="PAPER", font=("Arial 14 bold"), fg="red", activeforeground="white", activebackground="red", width=12, height=1, border=2, relief=SOLID,
                      command=lambda:computer_random_choice("paper"))
paper_button.place(x=220, y=480)
scissor_button = Button(root, text="SCISSOR", font=("Arial 14 bold"), fg="red", activeforeground="white", activebackground="red", width=12, height=1, border=2, relief=SOLID,
                        command=lambda:computer_random_choice("scissor"))
scissor_button.place(x=380, y=480)


root.mainloop()