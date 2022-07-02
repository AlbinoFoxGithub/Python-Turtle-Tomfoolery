import turtle
import json

defaultColors = open('./interesting spiral/Profiles/default.json')

colors = json.load(defaultColors)

# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
turtle.done()
