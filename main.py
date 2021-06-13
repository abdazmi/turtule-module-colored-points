from random import Random
from turtle import Turtle, Screen, colormode
color_palette =[(198, 13, 32),  (250, 238, 17), (27, 40, 156), (215, 75, 13), (198, 15, 11),
               (39, 76, 189), (39, 217, 69), (238, 226, 5), (229, 159, 46),
               (15, 154, 15),(242, 35, 166), (229, 17, 121), (70, 10, 31), (241, 245, 251), (61, 15, 8),
               (224, 141, 209), (11, 97, 62),(222, 160, 8), (51, 212, 230)]

timmy = Turtle()
timmy.shape("classic")
timmy.penup()
timmy.hideturtle()
colormode(255)
timmy.speed("fastest")

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)


for i in range(1,101):
    timmy.dot(20, Random().choice(color_palette))
    timmy.forward(50)

    if i % 10 ==0 :
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen=Screen()
screen.exitonclick()