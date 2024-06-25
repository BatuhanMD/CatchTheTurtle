import turtle
from random import randint

#Game board properties
game_board = turtle.Screen()
game_board.bgcolor("Light Gray")
game_board.title("Catch The Turtle")

#Turtle properties
turtle_object = turtle.Turtle()
turtle_object.shape("turtle")
turtle_object.color("Green")

def random_turtle():
    turtle_object.speed("slow")
    turtle_object.penup()
    turtle_object.goto(randint(-255,0),randint(0,255))
i = 0
while (i < 5 ):
    random_turtle()
    i += 1


turtle.done()