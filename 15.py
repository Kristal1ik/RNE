# from turtle import *
#
# speed(0)
# forward(100)
# right(90)
# forward(120)
# right(90)
# forward(100)
# right(90)
# forward(120)
# right(45)
# forward(71)
# right(90)
# forward(71)
# right(45)
# up()
# forward(30)
# right(90)
# forward(7)
# down()
# forward(33)
# left(90)
# forward(33)
# left(90)
# forward(33)
# left(90)
# forward(33)
# left(90)
# down()
# up()
# forward(53)
# down()
# forward(33)
# left(90)
# forward(33)
# left(90)
# forward(33)
# left(90)
# forward(33)
# left(90)
# left(90)
# up()
#
# forward(50)
# right(90)
# forward(2)
# down()
# left(90)
# forward(40)
# left(90)
# forward(30)
# left(90)
# forward(40)
# left(90)
# forward(15)
# left(90)
# forward(40)
# right(180)
# forward(40)
# left(90)
# forward(15)
# done()

# k = 10 # Масштаб
# up()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         goto(x*k, y*k)
#         dot(5)
# down()


for A in range(1000):
    for x in range(1000):
        for y in range(1000):
            if not((3 * x + y > 48) or (x > y) or (4 * x + y < A)):
                print(A)
