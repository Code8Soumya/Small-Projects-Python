from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.pu()
        self.speed(0)
        self.setposition(0,270)
        self.write(arg= f"Score: {self.score}", align= "center", font= ("courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!!", align="center", font=("courier", 50, "normal"))

    def incscore(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("courier", 15, "normal"))

