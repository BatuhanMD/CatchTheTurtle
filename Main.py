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
turtle_object.turtlesize(2)

# Score properties
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 350)
score_turtle.write("Score: 0", align="center", font=("Arial", 32, "normal"))

# Timer properties
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(0, 300)
timer_turtle.write("Time: 30", align="center", font=("Arial", 32, "normal"))

def update_score(new_score):
    score_turtle.clear()
    score_turtle.write(f"Score: {new_score}", align="center", font=("Arial", 32, "normal"))

def update_timer(time_left):
    timer_turtle.clear()
    timer_turtle.write(f"Time: {time_left}", align="center", font=("Arial", 32, "normal"))

def end_timer():
    timer_turtle.clear()
    timer_turtle.hideturtle()
    timer_turtle.penup()
    timer_turtle.goto(0, 300)
    timer_turtle.write("Game Over!", align="center", font=("Arial", 32, "normal"))

def random_turtle(): # Kaplumbağanın rastgele konumlandırılması için 
    turtle_object.penup()
    turtle_object.speed(0)
    turtle_object.goto(randint(-255, 255), randint(-255, 255))  

def increase_score(x,y):
    score_turtle.clear
    global new_score
    new_score += 1
    update_score(new_score)

turtle_object.onclick(increase_score)

time_left = 30
new_score = 0

while time_left > 0:
    turtle_object.hideturtle()  
    time.sleep(0.3)  
    random_turtle() 
    turtle_object.showturtle()  
    time.sleep(0.3)  
    time_left -= 1
    update_timer(time_left)

turtle_object.hideturtle()
end_timer()
turtle.done()
