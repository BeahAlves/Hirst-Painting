'''import colorgram

colors = colorgram.extract('damien_hirst.jpg', 25)
total_colors = []

for x in colors:
    r = x.rgb.r
    g = x.rgb.g
    b = x.rgb.b
    new_color = (r, g, b)
    total_colors.append(new_color)

print(total_colors)'''

import random
from turtle import Turtle, Screen, colormode

colormode(255)
t = Turtle()
t.shape("turtle")
t.speed('fastest')
t.hideturtle()

colors = [(158, 152, 148), (147, 149, 154), (130, 84, 76), (70, 117, 150), (224, 78, 98), (15, 21, 30),
          (83, 19, 9), (174, 139, 146), (114, 36, 27), (108, 120, 159), (1, 60, 143), (128, 87, 94), (102, 105, 102),
          (31, 19, 26), (4, 9, 8), (187, 93, 81), (186, 188, 203), (132, 130, 119), (100, 41, 51), (197, 195, 179)]
t.penup()
t.setpos(-200, -200)
pos = -200

x = 0
while x < 10:
    for i in range(10):
        t.dot(15)
        t.pencolor(random.choice(colors))
        t.fd(50)
        t.penup()

    x += 1
    pos += 40
    t.setpos(-200, pos)

screen = Screen()
screen.exitonclick()


