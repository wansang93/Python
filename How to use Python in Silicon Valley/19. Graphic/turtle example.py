from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()

turtle.color('red', 'yellow')
turtle.begin_fill()
turtle.shape('turtle')
speed = 1

while True:
    speed += 0.5
    turtle.speed(speed)
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break

turtle.end_fill()

turtle.pencolor('white')
turtle.backward(200)
turtle.pencolor('blue')
turtle.color('green', 'blue')
for i in range(100):
    turtle.fd(i * 2)
    turtle.left(360 / 5 * 2)
    turtle.speed(3+i)

screen.mainloop()