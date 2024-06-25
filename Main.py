import turtle
from random import randint
import time

# Game board properties
game_board = turtle.Screen()
game_board.bgcolor("Light Gray")
game_board.title("Catch The Turtle",)

# Turtle properties
turtle_object = turtle.Turtle()
turtle_object.shape("turtle")
turtle_object.color("Green")
turtle_object.turtlesize(2)

# Timer properties
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(0, 300)
timer_turtle.write("Time: 30", align="center", font=("Arial", 32, "normal"))

start_time = 30

def update_timer(time_left):
    timer_turtle.clear()
    timer_turtle.write(f"Time: {time_left}", align="center", font=("Arial", 32, "normal"))

def random_turtle():
    turtle_object.penup()
    turtle_object.speed(0)
    turtle_object.goto(randint(-255, 255), randint(-255, 255))  

time_left = start_time

while start_time > 0:
    turtle_object.hideturtle()  # Kaplumbağayı gizle
    time.sleep(1)  # 1 saniye bekle
    random_turtle()  # Kaplumbağayı rastgele bir konuma taşı
    turtle_object.showturtle()  # Kaplumbağayı göster
    time.sleep(1)  # 1 saniye bekle
    time_left -= 1
    update_timer(time_left)

turtle.done()
