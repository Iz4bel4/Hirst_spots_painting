import turtle
import random


# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('painting.jpg',30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

tur = turtle.Turtle()
turtle.colormode(255)
list_of_colors = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]


turtle.setup(width=800, height=800)

tur.hideturtle()
tur.speed('fastest')
tur.penup()
tur.setheading(225)
tur.forward(300)
tur.setheading(0)
dots_going_up = 10
dots_going_right = 10

for x in range(dots_going_up):
    for y in range(dots_going_right):
        tur.dot(20, random.choice(list_of_colors))
        tur.forward(50)

    tur.left(90)
    tur.forward(50)
    tur.left(90)
    tur.forward(500)
    tur.setheading(0)


turtle.exitonclick()

