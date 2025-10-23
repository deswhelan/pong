from turtle import Screen, Turtle

COURT_COLOUR = "royal blue"
COURT_LENGTH = 1000
COURT_TITLE = "Pong"
COURT_WIDTH = 600
NET_COLOUR = "white"

class Court:
    def __init__(self):
        super().__init__()
        self.court = self.create_court()

    def create_court(self):
        court = Screen()
        court.title(COURT_TITLE)
        court.setup(COURT_LENGTH, COURT_WIDTH)
        court.bgcolor(COURT_COLOUR)
        self.paint_net()
        return court

    def paint_net(self):
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