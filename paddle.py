from turtle import Turtle

PADDLE_COLOUR = "white"
PADDLE_LENGTH = 3
PADDLE_SEGMENT_HEIGHT = 20

class Paddle:
    def __init__(self):
        super().__init__()
        self.paddle = []
        self.set_starting_paddle(PADDLE_LENGTH)

    @staticmethod
    def get_paddle_segment():
        """Creates and returns a paddle segment"""
        paddle_segment = Turtle("square")
        paddle_segment.penup()
        paddle_segment.color(PADDLE_COLOUR)
        return paddle_segment

    # TODO: stretch - increase/decrease paddle size as part of game (e.g. power-ups) ?
    # TODO: stretch - use update/sleep to make paddle "appear" ?
    def set_starting_paddle(self, paddle_length):
        """Creates a new paddle of specified length"""
        self.paddle.append(self.get_paddle_segment())
        for _ in range(paddle_length - 1):
            self.add_paddle_segment()

    def add_paddle_segment(self):
        """Adds a new paddle segment to the existing paddle"""
        bottom_segment = self.paddle[-1]
        new_segment = self.get_paddle_segment()
        new_segment.setpos(bottom_segment.xcor(), bottom_segment.ycor() - 20)

        self.paddle.append(new_segment)

# TODO:
# move paddle
# create second paddle
class PlayerPaddle(Paddle):
    def __init__(self):
        super().__init__()