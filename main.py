from tkinter import *

# Colours used for the background:
# #5188b5
# #79aed9
# 4b81ad
# #5e9dd1
# #052f52



root = Tk()
root.geometry("1000x600")
root.title("Rock Paper Scissors")
root.resizable(0, 0)
root.configure(bg="#4b81ad")

rock_image = PhotoImage(file=r"rock.png")
paper_image = PhotoImage(file=r"paper.png")
scissors_image = PhotoImage(file=r"scissors.png")


selecting_frame = Frame(root, bg="#79aed9", height=600, width=240)
selecting_frame.place(x=760, y=0)


rock_button = Button(root, image=rock_image, borderwidth=0, bg="#79aed9")
rock_button.place(x=800, y=15)

paper_button = Button(root, image=paper_image, borderwidth=0, bg="#79aed9")
paper_button.place(x=800, y=200)

scissors_button = Button(root, image=scissors_image, borderwidth=0, bg="#79aed9")
scissors_button.place(x=801, y=385)


root.mainloop()