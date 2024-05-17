import turtle as t
playerAscore=0
playerBscore=0
x = True

#this space is to initialize quickly a few variables that can be useful later on :
minimumSpeed=5
#set the max point if you want some (if not remove the last if statement in the while true loop)
maxPoints=5 


#creating the base of the game and the desired aesthetic :)
#create the game window using the screen() call
window=t.Screen()
window.title=("PingPong Game")
window.bgcolor("lavenderblush2")
window.setup(width=1000, height=600)
window.tracer(0)


#create the left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(5,1)
leftpaddle.penup()
leftpaddle.goto(-350,0)


#create the right paddle - copy & paste the left paddle
#name it rightpaddle and change the coordinate to (350,0)
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(5,1)
rightpaddle.penup()
rightpaddle.goto(350,0)


#create the ball (choose your shape... a turtle is available :))
ball=t.Turtle()
ball.speed(0)
ball.shape("turtle")
ball.color("indianred1")
ball.penup()
ball.goto(5,5)
ballxdirection=minimumSpeed
ballydirection=minimumSpeed


#create scorecard
pen=t.Turtle()
pen.speed(0)
pen.color("lightpink2")
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
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)


def leftdown(): #same code but decrease the value of y
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)


#moving right paddle
def rightup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)


def rightdown(): 
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)

def leave():
    global x
    x = False

#assign the keys to play to the corresponding function 
window.listen()
window.onkeypress(leftup,'e')
window.onkeypress(leftdown,'d')
window.onkeypress(rightup,'Up')
window.onkeypress(rightdown,'Down')
window.onkeypress(leave, 'k')


#the while true will make the game run and give movement to the ball
while x == True:
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
        playerAscore=playerAscore+1
        pen.clear()
        pen.goto(0,260)
        pen.write("player A:{}    player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24))
        pen.goto(0,240)
        pen.write("press 'k' to exit the game !",align="center",font=('Arial',14,'normal'))


    if ball.xcor()<-440:
        ball.goto(0,0)
        ballxdirection=-minimumSpeed # bc the ball comes back to the person who just lost a point 
        playerBscore=playerBscore+1
        pen.clear()
        pen.goto(0,260)
        pen.write("player A:{}    player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24))
        pen.goto(0,240)
        pen.write("press 'k' to exit the game !",align="center",font=('Arial',14,'normal'))



    #ajust the collisions with the paddle
    if (ball.xcor()>338) and (ball.xcor()<350) and (ball.ycor()<rightpaddle.ycor()+47 and ball.ycor()>rightpaddle.ycor()-47):
        ball.setx(340)
        ballxdirection=ballxdirection*-1
        #increase the speed of the ball ( to make the ball and game go faster)
        ballxdirection-=0.5
        # i don't put it in ballydirection+=0.5 bc it depends which way it came from (up or down)



    if (ball.xcor()<-338) and (ball.xcor()>-350) and (ball.ycor()<leftpaddle.ycor()+47 and ball.ycor()>leftpaddle.ycor()-47):
        ball.setx(-340)
        ballxdirection=ballxdirection*-1
        ballxdirection+=0.5
        # ballydirection+=0.5

    # this game could go to infinity BBUT here we stop the game at __ points
    #so
    if (playerAscore==maxPoints) or (playerBscore==maxPoints):
        x=False


window.bye() # close the window (you could show who won tho)
if playerAscore>playerBscore:
    print("Player A won with " + str(maxPoints) + " against " + str(playerBscore) + "!")
elif playerAscore<playerBscore:
    print("Player B won with " + str(maxPoints) + " against " + str(playerAscore) + "!")
else:
    print("Tied!")
