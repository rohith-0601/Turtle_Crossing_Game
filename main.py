import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#screen settings
screen = Screen()
screen.title("FINISH FAST SCORE MORE")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

#create lines or road
pen = Turtle()
pen.color("white")
pen.pensize(6)
pen.hideturtle()
pen.penup()
for y in range(-260,290 +1,50):
    pen.goto(-300,y)
    pen.setheading(0)
    while pen.xcor() < 300:
        pen.pendown()
        pen.forward(30)
        pen.penup()
        pen.forward(15)


#calling player class
player = Player()
#calling cars
car_manager = CarManager()
car_manager.add_cars()
#calling scoreboard
scoreboard = Scoreboard(screen)

#user keys
screen.listen()
screen.onkey(player.move_up,"Up")

time.sleep(1)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #creating cars
    car_manager.add_new_cars()
    car_manager.move_cars()
    scoreboard.score_display()

    #check collision with car
    for car in car_manager.cars_list:
        if player.distance(car) < 15:
            game_is_on = False
            screen.reset()
            scoreboard.also_game_over()


    if player.xcor() == 290:
        game_is_on = False
        scoreboard.game_over()
        time.sleep(1)
    else:
        scoreboard.update_score()

    if scoreboard.score <= 0:
        game_is_on = False
        screen.reset()
        scoreboard.also_game_over()



screen.exitonclick()