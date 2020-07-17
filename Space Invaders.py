#Space Invaders
#Python3
import turtle
import os
import math
import random


#set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set score to 0
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Ariel", 14, "normal"))
score_pen.hideturtle()

#create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#choose number enemies
number_of_enemies = 10
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

#Create enemy
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#create players bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.2, 0.2)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready - to fire
#fire - firing
bulletstate = "ready"

#move player L and R
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#bullet

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move bullet above player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

#collision detection
def isCollision(t1, t2):
    distance =math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#create keyboard binding
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.listen()
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#main game loop

while True:

    #move bullet
    if bulletstate == "fire":
        y =bullet.ycor()
        y +=bulletspeed
        bullet.sety(y)

    #check bullet reach top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
    
    for enemy in enemies:
        # move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move enemy back and down
        if enemy.xcor() > 280:
            #moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                #change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1
            
        if enemy.ycor() < -280:
            #moves all enemies down
            for e in enemies:
                x = random.randint(-280, 280)
                y = random.randint(-250, -250)
                enemy.setposition(x, y)
                enemy.hideturtle()


     #check for collision
        if isCollision(bullet, enemy):
             #reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
         #reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
        #update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Ariel", 14, "normal"))


        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            bullet.hideturtle()
            scorestring = "Game Over! Final Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Ariel", 14, "normal"))
            break


