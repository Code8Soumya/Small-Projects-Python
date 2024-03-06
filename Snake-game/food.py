from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed(0)
        self.shapesize(stretch_wid= 0.5, stretch_len= 0.5)
        self.refresh()

    def refresh(self):
        rand_X = random.randint(-280, 280)
        rand_Y = random.randint(-280, 280)
        self.setposition(rand_X, rand_Y)

