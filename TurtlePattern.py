import turtle
turtle.bgcolor('black')
turtle.speed(0)
col=('white','red','white','red','white','red')
for i in range(360):
    turtle.pencolor(col[i%6])
    turtle.width(i/5+1)
    turtle.forward(i)
    turtle.right(30)
print("Done")