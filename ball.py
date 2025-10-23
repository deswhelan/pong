import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self, court):
        super().__init__()
        self.court = court
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.left(30.96)
        self.move()

    def move(self):
        # TODO: update/refactor this condition
        while True:
            time.sleep(0.01)
            self.fd(3)
            self.court.update()
