# from court import Court
# court = Court()

from turtle import Screen, Turtle

# TODO: move to a new "Court" class
COURT_LENGTH = 1000
COURT_WIDTH = 600
court = Screen()
court.setup(COURT_LENGTH, COURT_WIDTH)
court.bgcolor("royal blue")

def erect_net():
    """Paints a net in the centre of the court"""
    paint_roller = Turtle()
    paint_roller.hideturtle()
    paint_roller.color("white")
    paint_roller.pensize(5)
    paint_roller.speed(100)
    paint_roller.penup()

    for y in range(int(-COURT_WIDTH/2) + 15, int(COURT_WIDTH/2), 40):
        paint_roller.goto(0, y)
        paint_roller.pendown()
        paint_roller.goto(0, y + 20)
        paint_roller.penup()

erect_net()


court.exitonclick()
# TODO: create Paddle class
    # move paddle
    # create second paddle
# TODO: create Ball class
    # make it move
    # detect collision with wall and bounce accordingly
    # detect collision with paddle
    # detect when paddle misses (i.e. collision with edge of screen
# TODO: create Scoreboard class
