# Prolog
# Author: Suzal Regmi, Ricardo Cabrera
# Email: sregmi2@student.gsu.edu,  rcabreramartinez1@student.gsu
# Section: 036

'''
Purpose: 
We recreated Google's Tic Tac Toe as our final project for CSC 1301

Pre-Conditions (input):
The user needs to have installed two external librariers, pygame and numpy (pip install pygame, pip install numpy)
Then they can run the game by 'game.py'

Post-Conditions (output):
The game runs!
'''

## The Code

from tkinter import *
import os, sys

window = Tk()
window.title('Game Hub')
window.geometry("1200x800")
window.resizable(False, False)

window.iconphoto(True, PhotoImage(file=os.path.join("./media/main_icon.png")))

bcg = PhotoImage(file = "./media/bg_gamehub.png")
label1 = Label( window, image = bcg)
label1.place(x = -1,y = -50)


def launch_pong():
    window.destroy()
    os.system("python ./pong/pong.py")

pong_button = Button(window, command=launch_pong)
pong_img = PhotoImage(file="./media/pong_button.png") 
pong_button.config(image=pong_img)
pong_button.place(x=150,y=320)


def launch_tictactoe():
    window.destroy()
    os.system("python ./tictactoe/tictactoe.py")

tictactoe_button = Button(window, command=launch_tictactoe)
tictactoe_img = PhotoImage(file="./media/tictactoe_button.png") 
tictactoe_button.config(image=tictactoe_img)
tictactoe_button.place(x=350,y=320)


window.mainloop()  