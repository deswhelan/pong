from turtle import Turtle

PADDLE_COLOUR = "white"
PADDLE_HEIGHT = 5

class Paddle(Turtle):
    def __init__(self, court, player):
        super().__init__()
        self.court = court
        self.shape("square")
        self.penup()
        self.color(PADDLE_COLOUR)
        self.left(90)
        # TODO: stretch - increase/decrease paddle size as game feature (e.g. power-ups)?
        self.shapesize(stretch_len=PADDLE_HEIGHT)
        self.centre_to_end_offset = (PADDLE_HEIGHT * 20) / 2
        self.go_to_starting_position(court, player)

    def go_to_starting_position(self, court, player):
        """Sends paddle to the appropriate baseline of the court"""
        if player == 1:
            baseline_offset = self.court.lower_boundary_xcor + 20
        elif player == 2:
            baseline_offset = self.court.upper_boundary_xcor - 20
        # TODO: stretch - implement better exception handling (e.g. prompt user for valid input)
        else:
            print(f"Nah-ah-ah!")
            return

        # TODO: stretch - fix slight discrepancy in player 1 and player 2 buffers to screen edge
        self.goto(self.xcor() + baseline_offset, self.ycor())
        court.update()

    # TODO: stretch - fix slight boundary overshooting
    def move_up(self):
        # Don't move paddle beyond upper boundary of court
        if self.ycor() >= (self.court.upper_boundary_ycor - self.centre_to_end_offset):
            return

        self.forward(20)
        self.court.update()

    def move_down(self):
        # Don't move paddle beyond upper lower of court
        if self.ycor() <= (self.court.lower_boundary_ycor + self.centre_to_end_offset):
            return

        self.backward(20)
        self.court.update()

# TODO: reintroduce automated/computer paddle

# TODO: stretch - allow user to determine whether each player should be a Player (i.e. playable) paddle or a Computer (i.e. automated) paddle
