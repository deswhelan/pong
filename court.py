from turtle import Screen, Turtle

COURT_COLOUR = "royal blue"
COURT_LENGTH = 1000
COURT_TITLE = "Pong"
COURT_WIDTH = 600
NET_COLOUR = "white"

# TODO: stretch - inherit Screen instead of using implementation below
class Court:
    def __init__(self):
        super().__init__()
        self.court = self.create_court()
        self.court.upper_boundary_ycor = (self.court.window_height() / 2)
        self.court.lower_boundary_ycor = - self.court.upper_boundary_ycor
        self.court.upper_boundary_xcor = (self.court.window_width() / 2)
        self.court.lower_boundary_xcor = - self.court.upper_boundary_xcor

    def create_court(self):
        court = Screen()
        court.title(COURT_TITLE)
        court.setup(COURT_LENGTH, COURT_WIDTH)
        court.bgcolor(COURT_COLOUR)
        court.listen()
        court.tracer(0)
        self.paint_net()
        court.update()
        return court

    @staticmethod
    def paint_net():
        """Paints a net in the centre of the court"""
        paint_roller = Turtle()
        paint_roller.hideturtle()
        paint_roller.color(NET_COLOUR)
        paint_roller.pensize(5)
        paint_roller.speed(100)
        paint_roller.penup()

        for y in range(int(-COURT_WIDTH / 2) + 15, int(COURT_WIDTH / 2), 40):
            paint_roller.goto(0, y)
            paint_roller.pendown()
            paint_roller.goto(0, y + 20)
            paint_roller.penup()