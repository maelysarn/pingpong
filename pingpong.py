from random import random, uniform
from time import sleep
import turtle as t
playerAscore=0
playerBscore=0
play = True

minimumSpeed=0.2

#create the game window using the screen() call
window=t.Screen()

def leave():
    global play, setup_stage
    setup_stage = "done"
    play = False

window.listen()
window.onkeypress(leave, 'k')

# setting the game here
maxPoints = 5 # default 
setup_stage = "welcome"  # "welcome", "colors", "points", "done"
selected_theme = None
theme_colors = {    
    "pink": {"bg": "lavenderblush2", "paddle": "white", "ball": "indianred1", "text": "lightpink2"},
    "ocean": {"bg": "lightblue", "paddle": "navy", "ball": "darkturquoise", "text": "darkblue"},
    "forest": {"bg": "lightgreen", "paddle": "darkgreen", "ball": "brown", "text": "forestgreen"},
    "sunset": {"bg": "lightyellow", "paddle": "orange", "ball": "red", "text": "darkorange"}
}

window.title=("Gripping Turtle Pong")
window.bgcolor("white")
window.setup(width=1000, height=600)
window.tracer(0)

pen=t.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()

def welcome():
    pen.goto(0, 200)
    pen.write("WELCOME TO GRIPPING TURTLE PONG!", align="center", font=('Arial', 30, 'normal'))
    pen.goto(0, 150)
    pen.write("Press 'k' to exit the game at any time.", align="center", font=('Arial', 16, 'normal'))
    pen.goto(0, 100)
    pen.write("Click to start setting up your game.", align="center", font=('Arial', 16, 'normal'))


def display_color_selection():
    pen.clear()
    pen.goto(0, 200)
    pen.write("CHOOSE YOUR COLOR THEME", align="center", font=('Arial', 30, 'normal'))
    pen.goto(0, 150)
    pen.write("Click on a color theme below:", align="center", font=('Arial', 16, 'normal'))
    
    # display theme options
    themes = list(theme_colors.keys())
    y_pos = 50
    for i, theme in enumerate(themes):
        x_pos = -300 + i * 200
        pen.goto(x_pos, y_pos)
        pen.color(theme_colors[theme]["text"])
        pen.write(theme.upper(), align="center", font=('Arial', 20, 'bold'))
        
        # sample box
        pen.goto(x_pos - 50, y_pos - 30)
        pen.fillcolor(theme_colors[theme]["bg"])
        pen.begin_fill()
        for _ in range(4):
            pen.forward(100)
            pen.right(90)
        pen.end_fill()

def display_points_selection():
    pen.clear()
    pen.goto(0, 200)
    pen.write("CHOOSE MAXIMUM POINTS", align="center", font=('Arial', 30, 'normal'))
    pen.goto(0, 150)
    pen.write("Click on the number of points to win:", align="center", font=('Arial', 16, 'normal'))
    
    # point options
    point_options = [3, 5, 7, 10]
    y_pos = 50
    for i, points in enumerate(point_options):
        x_pos = -225 + i * 150
        pen.goto(x_pos, y_pos)
        pen.color("black")
        pen.write(str(points), align="center", font=('Arial', 30, 'bold'))
        pen.goto(x_pos, y_pos - 30)
        pen.write("points", align="center", font=('Arial', 12, 'normal'))

def handle_setup_click(x, y):
    global setup_stage, selected_theme, maxPoints
    
    if setup_stage == "welcome":
        # takes any click
        setup_stage = "colors"
        display_color_selection()

    elif setup_stage == "colors":
        # for which theme was clicked
        themes = list(theme_colors.keys())
        for i, theme in enumerate(themes):
            theme_x = -300 + i * 200
            if theme_x - 50 <= x <= theme_x + 50 and -70 <= y <= 80:
                selected_theme = theme
                setup_stage = "points"
                display_points_selection()
                break
                
    elif setup_stage == "points":
        point_options = [3, 5, 7, 10]
        for i, points in enumerate(point_options):
            point_x = -225 + i * 150
            if point_x - 75 <= x <= point_x + 75 and 20 <= y <= 80:
                maxPoints = points
                setup_stage = "done"
                break

window.onclick(handle_setup_click)

# start screen
welcome()

# setup loop
while setup_stage != "done":
    window.update()


# apply selected theme and start game
if setup_stage == "done" and selected_theme and play:
    theme = theme_colors[selected_theme]
    window.bgcolor(theme["bg"])
    
    pen.clear()
    pen.color(theme["text"])

#create the left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color(theme["paddle"] if selected_theme else "white")
leftpaddle.shapesize(5,1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#create the right paddle - copy & paste the left paddle
#name it rightpaddle and change the coordinate to (350,0)
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color(theme["paddle"] if selected_theme else "white")
rightpaddle.shapesize(5,1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#create the ball (choose your shape... a turtle is available :))
ball=t.Turtle()
ball.speed(0)
ball.shape("turtle")
ball.color(theme["ball"] if selected_theme else "indianred1")
ball.penup()
ball.goto(5,5)
ballxdirection=minimumSpeed
ballydirection=minimumSpeed

#create scorecard
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("SCORE",align="center",font=('Arial',24,'normal'))
pen.goto(0,240)
pen.write("press 'k' to exit the game !",align="center",font=('Arial',14,'normal'))

#now to create the moving paddles:
#first step to acheive the moving paddles is to create the definition (void functions here)
#that will affect the position of the paddles

#moving the left paddle
def leftup():
    if (leftpaddle.ycor() < 240):
        y=leftpaddle.ycor()
        y=y+90
        leftpaddle.sety(y)

def leftdown(): 
    if (leftpaddle.ycor() > -240):
        y=leftpaddle.ycor()
        y=y-90
        leftpaddle.sety(y)

#moving right paddle
def rightup():
    if (rightpaddle.ycor() < 240):
        y=rightpaddle.ycor()
        y=y+90
        rightpaddle.sety(y)

def rightdown(): 
    if (rightpaddle.ycor() > -240):
        y=rightpaddle.ycor()
        y=y-90
        rightpaddle.sety(y)

#assign the keys to play to the corresponding function 
window.onkeypress(leftup,'e')
window.onkeypress(leftdown,'d')
window.onkeypress(rightup,'Up')
window.onkeypress(rightdown,'Down')

# remove mouse click listener for game (only used for setup now)
window.onclick(None)

# run the game
while play == True:
    window.update()

    #giving movement to the ball :) in both x and y directions
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    #set the border - to be ajusted to the size of the screen
    #the maths done here are just the width or height of the screen
    #divided by 2 and then subtract 10 to that number to leave a margin on each side
    if ball.ycor()>290: 
        ball.sety(290)
        ballydirection=ballydirection*-1 #mirror the movement
         
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    # when out of range/ out of reach ?? 
    if ball.xcor()>440:
        ball.goto(0,0)
        ballxdirection=minimumSpeed #it comes back to original speed (but different angle)
        ballydirection=minimumSpeed  # Reset Y direction too
        ballydirection= uniform(-minimumSpeed, minimumSpeed)  # randomize Y direction
        playerAscore=playerAscore+1
        pen.clear()
        pen.goto(0,260)
        pen.write("player A:{}    player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24))
        pen.goto(0,240)
        pen.write("press 'k' to exit the game !",align="center",font=('Arial',14,'normal'))

    if ball.xcor()<-440:
        ball.goto(0,0)
        ballxdirection=-minimumSpeed # bc the ball comes back to the person who just lost a point 
        ballydirection = uniform(-minimumSpeed, minimumSpeed)  # randomize Y direction
        playerBscore=playerBscore+1
        pen.clear()
        pen.goto(0,260)
        pen.write("player A:{}    player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24))
        pen.goto(0,240)
        pen.write("press 'k' to exit the game !",align="center",font=('Arial',14,'normal'))

    #ajust the collisions with the paddle
    if (ball.xcor()>338) and (ball.xcor()<350) and (ball.ycor()<rightpaddle.ycor()+47 and ball.ycor()>rightpaddle.ycor()-47):
        ball.setx(340)
        ballxdirection=-abs(ballxdirection) - 0.0001  # slight speed increase

    if (ball.xcor()<-338) and (ball.xcor()>-350) and (ball.ycor()<leftpaddle.ycor()+47 and ball.ycor()>leftpaddle.ycor()-47):
        ball.setx(-340)
        ballxdirection=abs(ballxdirection) + 0.0001  
        # ballydirection+=0.5

    # this game could go to infinity BBUT here we stop the game at __ points
    #so
    if (playerAscore==maxPoints) or (playerBscore==maxPoints):
        play=False

end_message = ""
if playerAscore>playerBscore:
    end_message = "Player A won with " + str(playerAscore) + " against " + str(playerBscore) + "!"
elif playerAscore<playerBscore:
    end_message = "Player B won with " + str(playerBscore) + " against " + str(playerAscore) + "!"
else:
    end_message = "Tied with " + str(playerAscore) + " points each!"


window.clear()
window.bgcolor("white")
theme = theme_colors[selected_theme]
window.bgcolor(theme["bg"])
pen.clear()
pen.color(theme["text"])
pen.goto(0, 0)
pen.write(end_message, align="center", font=('Arial', 24, 'bold'))

sleep(10)  # pause to show the end message

window.bye() # close the window 
