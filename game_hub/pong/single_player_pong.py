from graphics_lib import *
import os, time, platform
from random import randint

CIRCLE_RADIUS = 5  # Radius of the Ball
CIRCLE_X_SPEED = 5    # Speed with which the X axis moves, when the ball is moving
CIRCLE_Y_SPEED = -2   # Since Y axis increases while going down, we use negative value so that it travels up when we initiate the game

WINDOW_WIDTH = 600   # Width and Height of the game window
WINDOW_HEIGHT = 400

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

CIRCLE_X = randint(0+CIRCLE_RADIUS, WINDOW_WIDTH - CIRCLE_RADIUS )  # X axis of the position where the ball will start at
CIRCLE_Y = randint(0, WINDOW_WIDTH//2)  # Y axis of the position where the ball will start at

PADDLE_X = randint(0,600-PADDLE_WIDTH) # Dimentions and Speed of the paddle
PADDLE_Y = 350

PADDLE_SPEED = 0

st = time.time()

# Draws a circle and a rectangle
def draw_frame():
    global CIRCLE_X, CIRCLE_Y, CIRCLE_X_SPEED, CIRCLE_Y_SPEED, PADDLE_X, PADDLE_WIDTH, PADDLE_SPEED
    draw_circle(CIRCLE_X, CIRCLE_Y, CIRCLE_RADIUS, "white")
    draw_rectangle(PADDLE_X, PADDLE_Y, PADDLE_X + PADDLE_WIDTH, PADDLE_Y + PADDLE_HEIGHT, "white")

    # If ball hits the side walls, it bounces back
    if CIRCLE_X + CIRCLE_RADIUS >= WINDOW_WIDTH or CIRCLE_X - CIRCLE_RADIUS <= 0:
        CIRCLE_X_SPEED *= -1

    # If the balls hits the paddel, it bounces back
    if  (
        PADDLE_Y <= CIRCLE_Y + CIRCLE_RADIUS < PADDLE_Y + CIRCLE_Y_SPEED and
        PADDLE_X <= CIRCLE_X <= PADDLE_X + PADDLE_WIDTH
    ):
        CIRCLE_Y_SPEED *= -1.3

    # If the ball hits the bottom, freeze it
    if CIRCLE_Y + CIRCLE_RADIUS >= WINDOW_HEIGHT:
        CIRCLE_X_SPEED = 0
        CIRCLE_Y_SPEED = 0
        PADDLE_SPEED = 0

        et = time.time()
        
        def main_menu():
            death.destroy()
            os.system ("python ./pong/pong.py")

        def play_again():
            death.destroy()
            os.system("python ./pong/single_player_pong.py")

        def exit_game():
            if platform.system() == "Linux":
                os.system("killall python")
            elif platform.system() == "Windows":
                os.system('wmic process where name="Python.exe" delete')
        death = Tk()
        death.title("Die")

        death.geometry("300x200")
        death.resizable(False, False)

        Label(death, text="Game Over").place(x=110,y=20)

        with open ("./pong/high_score.txt", "r+") as file:
            for score in file:
                if os.path.getsize("./pong/high_score.txt") == 0 or score == 0 :
                    Label(death, text=f"Congratulations!! New Highscore: {et-st:.2f}").place(x=35,y=50)
                    file.write(f"{et-st}")
                else:
                    if et - st >= float(score):
                        Label(death, text=f"Congratulations!! New Highscore: {et-st:.2f}").place(x=35,y=50) 
                        with open ("./pong/high_score.txt", "w") as new_file:
                            new_file.write(str(et-st))
                    else:
                        Label(death, text=f"Lasted {et-st:.2f} seconds!").place(x=85,y=50)

        Button(death, text="Play Again", command=play_again).place(x=105,y=80)
        Button(death, text="Return to Main Menu", command=main_menu).place(x=70,y=120)
        Button(death, text="Exit", command=exit_game).place(x=120,y=160)

        death.mainloop()
        

    # If the ball hits the top of the screen, it bounces back
    if CIRCLE_Y - CIRCLE_RADIUS <= 0:
        CIRCLE_Y_SPEED *= -1
    
    # Makes it so that the paddle stays inside the game window
    if PADDLE_X < 0 or PADDLE_X + PADDLE_WIDTH > WINDOW_WIDTH:
        PADDLE_SPEED = 0
        PADDLE_X = max(0, PADDLE_X)
        PADDLE_X = min(WINDOW_WIDTH - PADDLE_WIDTH, PADDLE_X)
    
    # Moving the ball
    CIRCLE_X += CIRCLE_X_SPEED
    CIRCLE_Y += CIRCLE_Y_SPEED
    PADDLE_X += PADDLE_SPEED

# Recognizing keyboard press
def key_press(key):
    global PADDLE_SPEED

    if key == "Left":
        PADDLE_SPEED = -5
    if key == "Right":
        PADDLE_SPEED = 5


def main():
    # Drawing the actual graphics
    start_graphics(
        draw_frame,
        window_width = WINDOW_WIDTH,
        window_height = WINDOW_HEIGHT,
        window_title = "Pong",
        key_press = key_press,
        )

    
if __name__ == "__main__":
    main()



'''
To Do
1) Randomize ball direction after impact
2) 
3) Music?
4) 
5) Implement 2 player game
6) 


'''