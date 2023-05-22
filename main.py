from tkinter import *

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
enemy_image = PhotoImage(file=r"robot.jpg")


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




rock_button = Button(root, image=rock_image, borderwidth=0, bg="#79aed9")
rock_button.place(x=800, y=15)

paper_button = Button(root, image=paper_image, borderwidth=0, bg="#79aed9")
paper_button.place(x=800, y=200)

scissors_button = Button(root, image=scissors_image, borderwidth=0, bg="#79aed9")
scissors_button.place(x=801, y=385)



root.mainloop()