from tkinter import *
from tkinter import messagebox
from random import randint
import os
import sys

# Colours used for the background:
# #5188b5
# #79aed9
# 4b81ad
# #5e9dd1
# #052f52
# #4b6fad
# #3f6a99

root = Tk()
root.geometry("1000x600")
root.title("Rock Paper Scissors")
root.resizable(0, 0)
root.configure(bg="#4b81ad")

rock_image = PhotoImage(file=r"rock.png")
paper_image = PhotoImage(file=r"paper.png")
scissors_image = PhotoImage(file=r"scissors.png")
player_image = PhotoImage(file=r"finger_pointing_at_you.png")
enemy_image = PhotoImage(file=r"robot.png")
rock_winner_image = PhotoImage(file=r"rock_winner.png")
paper_winner_image = PhotoImage(file=r"paper_winner.png")
scissors_winner_image = PhotoImage(file=r"scissors_winner.png")



win_or_lose = StringVar()

enemy_score_value = 0
enemy_score = StringVar()
enemy_score.set(enemy_score_value)

player_score_value = 0
player_score = StringVar()
player_score.set(player_score_value)

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def button_disable():
    rock_button["state"] = DISABLED
    paper_button["state"] = DISABLED
    scissors_button["state"] = DISABLED

def button_enable():
    rock_button["state"] = NORMAL
    paper_button["state"] = NORMAL
    scissors_button["state"] = NORMAL

def tksleep(t):
    ms = int(t+1000)
    var = IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)
    '''
    from the internet
    '''

def win():
    if player_score_value == 4:
        win_one_round()
        lose_one_round()
        messagebox.showinfo(title="You win!", message="Good Job!!")
        root.destroy()

def lose():
    if enemy_score_value == 4:
        win_one_round()
        lose_one_round()
        messagebox.showinfo(title="Enemy wins!", message="You lost...")
        root.destroy()

def win_one_round():
    global player_score_value
    player_score_value = player_score_value + 1
    player_score.set(player_score_value)

    win_or_lose_label.configure(fg="lightgreen")
    win_or_lose.set("You win!")

    player_frame.config(highlightbackground="green", highlightthickness=4)
    enemy_frame.config(highlightbackground="red", highlightthickness=4)

def lose_one_round():
    global enemy_score_value
    enemy_score_value = enemy_score_value + 1
    enemy_score.set(enemy_score_value)

    win_or_lose_label.configure(fg="red")
    win_or_lose.set("Enemy wins!")

    enemy_frame.config(highlightbackground="green", highlightthickness=4)
    player_frame.config(highlightbackground="red", highlightthickness=4)

def draw_one_round():
    win_or_lose_label.configure(fg="orange")
    win_or_lose.set("It's a draw!")

    enemy_frame.config(highlightbackground="orange", highlightthickness=4)
    player_frame.config(highlightbackground="orange", highlightthickness=4)

def rock():

    random = randint(1, 3)

    rock_winner = Label(root, image=rock_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
    rock_winner.place(x=225, y=225)

    win()
    lose()

# draw
    if random == 1:
        draw_one_round()
        rock_winner2 = Label(root, image=rock_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
        rock_winner2.place(x=385, y=225)
        button_disable()
        tksleep(5)
        button_enable()

# lose
    elif random == 2:
        lose_one_round()
        paper_winner = Label(root, image=paper_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
        paper_winner.place(x=385, y=225)
        button_disable()
        tksleep(5)
        button_enable()

# win
    elif random == 3:
        win_one_round()
        scissors_winner = Label(root, image=scissors_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
        scissors_winner.place(x=385, y=225)
        button_disable()
        tksleep(5)
        button_enable()



def paper():

    random = randint(1, 3)

    paper_winner = Label(root, image=paper_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
    paper_winner.place(x=225, y=225)


    win()
    lose()



# win
    if random == 1:
        win_one_round()
        rock_winner = Label(root, image=rock_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
        rock_winner.place(x=385, y=225)
        button_disable()
        tksleep(5)
        button_enable()


# draw
    elif random == 2:
        draw_one_round()
        paper_winner = Label(root, image=paper_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
        paper_winner.place(x=385, y=225)
        button_disable()
        tksleep(5)
        button_enable()


# lose
    elif random == 3:
        lose_one_round()
        scissors_winner = Label(root, image=scissors_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
        scissors_winner.place(x=385, y=225)
        button_disable()
        tksleep(5)
        button_enable()


def scissors():

    random = randint(1, 3)

    scissors_winner = Label(root, image=scissors_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
    scissors_winner.place(x=225, y=225)



    win()
    lose()

# lose
    if random == 1:

        lose_one_round()
        rock_winner = Label(root, image=rock_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
        rock_winner.place(x=385, y=225)
        button_disable()
        tksleep(5)
        button_enable()



# win
    elif random == 2:

        win_one_round()
        paper_winner = Label(root, image=paper_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
        paper_winner.place(x=385, y=225)
        button_disable()
        tksleep(5)
        button_enable()

# draw
    elif random == 3:

        draw_one_round()
        scissors_winner = Label(root, image=scissors_winner_image, bg="#4b81ad", borderwidth=0, fg="#4b81ad")
        scissors_winner.place(x=385, y=225)
        button_disable()
        tksleep(5)
        button_enable()




selecting_frame = Frame(root, bg="#79aed9", height=600, width=240)
selecting_frame.place(x=760, y=0)

player_frame = Frame(root, bg="#3f6a99", height=400, width=200)
player_frame.place(x=25, y=100)

enemy_frame = Frame(root, bg="#3f6a99", height=400, width=200)
enemy_frame.place(x=525, y=100)

text_frame = Frame(root, bg="#79aed9", height=60, width=760)
text_frame.place(x=0, y=0)

text_frame_text = Label(root, text="Rock Paper Scissors Game", bg="#79aed9", fg="black", font=("consolas", 22, "bold"))
text_frame_text.place(x=200, y=10)



player_avatar = Label(root, image=player_image, borderwidth=0, bg="#3f6a99")
player_avatar.place(x=34, y=110)

enemy_avatar = Label(root, image=enemy_image, borderwidth=0, bg="#3f6a99")
enemy_avatar.place(x=535, y=110)



enemy_score_label = Label(root, textvariable=enemy_score, font=("Calbri", 60, "bold"), bg="#3f6a99")
enemy_score_label.place(x=600, y=350)




player_score_label = Label(root, textvariable=player_score, font=("Calbri", 60, "bold"), bg="#3f6a99")
player_score_label.place(x=100, y=350)


rock_button = Button(root, image=rock_image, borderwidth=0, bg="#79aed9", command=rock)
rock_button.place(x=800, y=15)

paper_button = Button(root, image=paper_image, borderwidth=0, bg="#79aed9", command=paper)
paper_button.place(x=800, y=200)

scissors_button = Button(root, image=scissors_image, borderwidth=0, bg="#79aed9", command=scissors)
scissors_button.place(x=801, y=385)

win_or_lose_label = Label(root, textvariable=win_or_lose, font=("consolas", 20), bg="#4b81ad", fg="black")
win_or_lose_label.place(x=300, y=550)


root.mainloop()
