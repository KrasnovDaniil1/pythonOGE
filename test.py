from turtle import *

screensize(5000, 5000)
tracer(False)

m=20


for i in range(2):
    forward(10 * m)
    right(90)
    forward(18 * m)
    right(90)

penup()

forward(5 * m)
right(90)
forward(7 * m)
right(90)

pendown()

for i in range(2):
    forward(10 * m)
    right(90)
    forward(7 * m)
    right(90)

penup()
for x in range(0, 11):
    for y in range(-18, 1):
        goto(x*m, y*m)
        dot(3, "red")

update()
done()