import time
from turtle import Turtle

# detect collision with wall and bounce accordingly
# detect collision with paddle
# detect when paddle misses (i.e. collision with edge of screen

class Ball(Turtle):
    def __init__(self, court):
        super().__init__()
        self.court = court
        self.color("yellow")
        self.shape("circle")
        self.penup()
        # always aim initial "serve" at corner of court
        # self.left(30.96)
        # TODO: restore angle above
        # self.left(45)
        self.right(80)

    def move(self):
        time.sleep(0.01)
        self.fd(3)
        self.court.update()

    #TODO consolidate into a single "bounce off wall" method?
    def bounce_off_top_wall(self):
        # TODO: handle moving right to left
        original_direction = self.heading()
        self.setheading(0)
        self.right(original_direction)

    def bounce_off_bottom_wall(self):
        # TODO: handle moving right to left
        print("bouncing off bottom wall now")
        original_direction = self.heading()
        print(original_direction)
        self.setheading(0)
        self.left(360 - original_direction)