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
        self.left(80)
        # self.right(80)

    def move(self):
        time.sleep(0.01)
        self.fd(3)
        self.court.update()

    def bounce_ball_off_wall(self):
        current_direction = self.heading()

        is_moving_right = (0 <= current_direction < 90 or 270 < current_direction <= 360)

        # TODO: stretch - investigate edge case of heading exactly 180, and similar above
        is_moving_up = 0 < current_direction <= 180

        self.setheading(0)

        if is_moving_right:
            if is_moving_up:
                self.right(current_direction)
            else:
                self.left(360 - current_direction)
        else:
            # TODO: implement is_moving_left
            pass