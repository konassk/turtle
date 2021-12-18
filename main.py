# import turtle
import turtle as t
import random

import colorgram
# import colorgram as c

# import heroes
# timmy = Turtle()
t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colour = (r, g, b)
#     return random_colour
#
#
# # directions = [0, 90, 180, 270]
# # t.width(15)
# t.speed("fastest")
# for i in range(200):
#     t.color(random_color())
#     t.forward(30)
#     t.setheading(random.choice(directions))

# for shape in range(3, 11):
#     )
#     draw_shape(shape)
# rgb_colors = []
colours = colorgram.extract("image.jpg", 30)
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)
k = 0
colour_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
               (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
               (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
               (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
               (176, 192, 208), (168, 99, 102)]
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)

t.speed("fastest")


def dots():
    for i in range(10):
        t.color(random.choice(colour_list))
        t.dot(20)
        t.up()
        t.forward(50)
        t.down()


for i in range(5):
    dots()
    t.penup()
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(50)
    dots()
    t.penup()
    t.setheading(90)
    t.forward(50)
    t.setheading(360)
    t.forward(50)

# for i in range(0, 10):
#     t.dot(20, random_color())
#     t.forward(20)
#     t.up()
#     t.forward(20)
#     t.down()

# t.exitonclick()
