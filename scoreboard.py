from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self,screen):
        self.score = 1000
        self.screen = screen
        self.update_score()

    def update_score(self):
        self.score -= 1

    def score_display(self):
        self.screen.title(f"CAR RACE, Score : {self.score}")

    def game_over(self):
        pen_2 = Turtle()
        pen_2.color("white")
        pen_2.pensize(5)
        pen_2.penup()
        pen_2.write(f"GAME OVER\nYour Score:{self.score}",align = "center",font = FONT)

    def also_game_over(self):
        pen_3 = Turtle()
        pen_3.color("white")
        pen_3.pensize(5)
        pen_3.penup()
        pen_3.write(f"GAME OVER\nTry Again!", align="center", font=FONT)



