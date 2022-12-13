from tkinter import *
import sys, os
import single_player_pong

root = Tk()
root.title("Pong")

program_directory=sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "icon.png")))

bcg = PhotoImage(file = "./pong/bg_pong.png")
label1 = Label( root, image = bcg)
label1.place(x = -1,y = -50)

root.geometry("500x400")
root.resizable(False, False)


def launch_double():
    Label(root, text="Sorry I was Procrastinating!").place(x=285,y=360)

def launch_single():
    root.destroy()
    single_player_pong.main()

Button(
   root, 
   text="Single Player", 
   command=launch_single
).place(x=190,y=300)

Button(
   root, 
   text="Double Player\n(coming soon!)", 
   command=launch_double
).place(x=310,y=300)



root.mainloop()