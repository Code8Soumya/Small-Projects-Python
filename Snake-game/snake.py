from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.Xpos = 0
        self.Ypos = 0
        self.pos = [(0, 0), (0, 0), (0, 0)]
        self.create_snake()

    def create_snake(self):
        for _ in range(1, 4):
            tim = Turtle()
            tim.speed(0)
            tim.color("white")
            tim.shape("square")
            tim.pu()
            tim.setposition(x=self.Xpos, y=self.Ypos)
            self.segments.append(tim)
            self.Xpos -= 20

    def move(self):
        self.pos[0] = self.segments[0].position()
        self.segments[0].forward(20)
        for num in range(1, len(self.segments)):
            self.pos[1] = self.segments[num].position()
            self.segments[num].setposition(self.pos[0])
            self.pos[2] = self.pos[1]
            self.pos[0] = self.pos[2]
            self.segments[num].showturtle()

    def extend(self):
        tim = Turtle()
        tim.hideturtle()
        tim.speed(0)
        tim.color("white")
        tim.shape("square")
        tim.pu()
        self.segments.append(tim)


    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)


