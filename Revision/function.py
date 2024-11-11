import turtle
pen=turtle.Turtle()
paper=turtle.Screen()
paper.bgcolor("light blue")
def move(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()
move(-300,-300)
pen.left(90)
def space(side,angle,side_,angle_):
    for i in range(2):
        pen.forward(side)
        pen.right(angle)
        pen.forward(side_)
        pen.right(angle_)
space(400,90,200,90)
move(-100,-300)
space(300,90,300,90)
input()