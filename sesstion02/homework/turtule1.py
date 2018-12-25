from turtle import *
pencolor("red")
speed(0)
right(30)
for i in range(4):
    for i in range(4):
        if i % 2==0:
            forward(70)
            left(60)
        else:
            forward(70)
            left(120)
    right(90)    
mainloop()