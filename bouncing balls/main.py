import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("I Love Balls")
wn.tracer(0)

balls = []

# balls
for _ in range(20):
    balls.append(turtle.Turtle())

colors = ["red", "green", "blue", "purple", "orange", "white"]
shapes = ["square", "circle", "triangle"]

for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(0, 290)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-1, 1)
    ball.da = random.randint(-2, 2)

gravity = 0.001

while True:
    wn.update()
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # check wall
        if ball.xcor() > 300:
            ball.dx *= -1
            ball.da *= -1
        if ball.xcor() < -300:
            ball.dx *= -1
            ball.da *= -1

        # Bounce
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1
        if ball.ycor() > 300:
            ball.sety(300)
            ball.dy *= -1
            ball.da *= -1

    #check for ball hits
    for i in range(0, len(balls)):
        for j in range(i +1, len(balls)):
            if balls[i].distance(balls[j]) < 20:
                #balls[i].color(random.choice(colors))
                #balls[j].color(random.choice(colors))
                balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy
                balls[i].da, balls[j].da = balls[j].da, balls[i].da

wn.mainloop()
