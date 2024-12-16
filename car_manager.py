from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
cars_list = []
cars_point = [-235, -185, -135, -85, -35, 15, 65, 115, 165, 215, 265]

class CarManager:
    def __init__(self):
        self.car_count = 0
        self.cars_list = []
        self.add_cars()

    def add_cars(self):
        for i in range(10):
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(0.7,2)
            car.penup()
            car.speed(random.randint(5,9))
            car.car_speed = random.randint(5,9)
            car.goto(290,random.choice(cars_point))
            self.cars_list.append(car)

    def add_new_cars(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(0.7, 2)
        car.penup()
        car.speed(random.randint(5, 9))
        car.car_speed = random.randint(5, 9)
        car.goto(290, random.choice(cars_point))
        self.cars_list.append(car)

    def move_cars(self):
        for cars in self.cars_list:
            cars.setx(cars.xcor() - cars.car_speed)

            if cars.xcor() < -300:
                self.cars_list.remove(cars)
                cars.hideturtle()
                self.car_count += 1








