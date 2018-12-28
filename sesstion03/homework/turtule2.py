from turtle import *
colors =  [ 'red','blue','brown','yellow','gray']
for i in range(len(colors)):
    color(colors[i])
    begin_fill()
    for j in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
mainloop()