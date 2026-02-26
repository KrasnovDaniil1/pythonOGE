from turtle import *

screensize(5000, 5000)
tracer(False)

m=20

left(90)

for i in range(2):
    forward(28 * m)
    right(90)
    forward(18 * m)
    right(90)

penup()

forward(14 * m)
right(90)
forward(10 * m)
right(90)

pendown()

for i in range(2):
    forward(30 * m)
    right(90)
    forward(7 * m)
    right(90)

penup()

x_count = 0
y_count = 0
for x in range(0, 19):
    x_count += 1
    y_count = 0
    for y in range(0, 29):
        goto(x*m, y*m)
        dot(3, "red")
        y_count += 1

print(x_count * y_count )

update()
done()