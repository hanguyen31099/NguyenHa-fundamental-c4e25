from turtle import *
pencolor("red")
for i in range(4):
    forward(90)
    left(90)
for i in range(7):
    forward(90)
    if i<6:
        left(60)
pencolor("blue")
for i in range(2):
    left(120)
    forward(90)
left(228)
for j in range(4):
    forward(90)
    right(72)
mainloop()