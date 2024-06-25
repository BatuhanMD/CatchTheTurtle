import turtle
from random import randint
import time

# Game board properties
game_board = turtle.Screen()
game_board.bgcolor("Light Gray")
game_board.title("Catch The Turtle")

# Turtle properties
turtle_object = turtle.Turtle()
turtle_object.shape("turtle")
turtle_object.color("Green")

def random_turtle():
    turtle_object.penup()
    turtle_object.goto(randint(-255, 255), randint(-255, 255))  

i = 0
while i < 5:
    turtle_object.hideturtle()  # Kaplumbağayı gizle
    time.sleep(1)  # 1 saniye bekle
    random_turtle()  # Kaplumbağayı rastgele bir konuma taşı
    turtle_object.showturtle()  # Kaplumbağayı göster
    time.sleep(1)  # 1 saniye bekle
    i += 1

turtle.done()
