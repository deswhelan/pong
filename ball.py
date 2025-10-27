import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self, court):
        super().__init__()
        self.court = court
        self.color("yellow")
        self.shape("circle")
        self.penup()
        # set angle of initial "serve"
        self.left(35)

    # TODO: stretch randomise angle of serve
    def serve(self):
        player_2_is_serving = self.is_moving_right(self.heading())

        self.home()
        self.court.update()
        time.sleep(1)

        if player_2_is_serving:
            self.setheading(145)
        else:
            self.setheading(35)

    def move(self, ball_speed):
        time.sleep(0.01)
        self.fd(ball_speed)
        self.court.update()

    @staticmethod
    def is_moving_right(direction):
        return 0 <= direction < 90 or 270 < direction <= 360

    @staticmethod
    def is_moving_up(direction):
        return 0 < direction <= 180

    # TODO: refactor/consolidate logic in both "bounce" methods
    def bounce_off_wall(self):
        current_direction = self.heading()
        self.setheading(0)

        if self.is_moving_right(current_direction):
            if self.is_moving_up(current_direction):
                self.right(current_direction)
            else:
                self.left(360 - current_direction)
        else:
            if self.is_moving_up(current_direction):
                self.left(-current_direction)
            else:
                self.right(current_direction)

    def bounce_off_paddle(self):
        current_direction = self.heading()
        self.setheading(0)

        if self.is_moving_right(current_direction):
            if self.is_moving_up(current_direction):
                self.left(180 - current_direction)
            else:
                self.right(current_direction - 180)
        else:
            if self.is_moving_up(current_direction):
                self.right(180 + current_direction)
            else:
                print("bouncing")
                self.left(180 - current_direction)

