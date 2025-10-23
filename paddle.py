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
    # TODO: stretch - prevent paddle from overshooting boundaries when moving quickly
    def move_up(self):
        if self.paddle[0].ycor() >= 290:
            return

        for paddle_segment in reversed(self.paddle):
            paddle_segment.forward(20)

    def move_down(self):
        if self.paddle[-1].ycor() <= -290:
            return

        for paddle_segment in self.paddle:
            paddle_segment.backward(20)

# TODO: stretch - allow user to determine whether each player should be a Player (i.e. playable) paddle or a Computer (i.e. automated) paddle and update positioning/logic of child classes below accordingly
class PlayerPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.go_to_starting_position()

    # TODO: stretch - use update/sleep to make paddle "appear"?
    def go_to_starting_position(self):
        """Sends player paddle to the starting position"""
        for paddle_segment in self.paddle:
            paddle_segment.goto(paddle_segment.xcor() - 480, paddle_segment.ycor() + 30)

class ComputerPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.go_to_starting_position()
        self.play()

    # TODO: stretch - use update/sleep to make paddle "appear"?
    def go_to_starting_position(self):
        """Sends player paddle to the starting position"""
        for paddle_segment in self.paddle:
            paddle_segment.goto(paddle_segment.xcor() + 480, paddle_segment.ycor() + 30)

    def play(self):
        """Makes the computer paddle "play" by automating its movement"""
        while True:
            while self.paddle[0].ycor() < 290:
                self.move_up()

            while self.paddle[-1].ycor() > -290:
                self.move_down()
