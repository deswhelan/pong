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
        paddle_segment.speed(100)
        paddle_segment.left(90)
        return paddle_segment

    # TODO: stretch - increase/decrease paddle size as part of game (e.g. power-ups) ?
    # TODO: stretch - use update/sleep to make paddle "appear"?
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

    # TODO: implement update/sleep to animate "smooth" paddle movement
    # TODO: impose upper/lower court boundaries
    def move_up(self):
        for paddle_segment in reversed(self.paddle):
            paddle_segment.forward(20)

    def move_down(self):
        for paddle_segment in self.paddle:
            paddle_segment.backward(20)

# TODO: create second (i.e. "computer" and/or "player 2 (use WASD?)") paddle
class PlayerPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.go_to_starting_position()

    # TODO: stretch - use update/sleep to make paddle "appear"?
    def go_to_starting_position(self):
        """Sends player paddle to the starting position"""
        for paddle_segment in self.paddle:
            paddle_segment.goto(paddle_segment.xcor() - 480, paddle_segment.ycor() + 30)
