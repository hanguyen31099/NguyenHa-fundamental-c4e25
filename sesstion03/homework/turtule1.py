from turtle import *
pencolor("blue")
for i in range(4):
    forward(90)
    left(90)
pencolor("yellow")
for i in range(7):
    forward(90)
    if i<6:
        left(60)
pencolor("red")
for i in range(2):
    left(120)
    forward(90)
left(228)
pencolor("brown")
for j in range(4):
    forward(90)
    right(72)
pencolor("grey")
for i in range(7):
    forward(90)
    right(360/7)
mainloop()