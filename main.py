from ball import Ball
from court import Court
from paddle import Paddle

court = Court().court

player_1_paddle = Paddle(court, 1)
court.onkeypress(player_1_paddle.move_up, "w")
court.onkeypress(player_1_paddle.move_down, "s")

player_2_paddle = Paddle(court, 2)
court.onkeypress(player_2_paddle.move_up, "Up")
court.onkeypress(player_2_paddle.move_down, "Down")

ball = Ball(court)

game_is_on = True

while game_is_on:
    ball.move()

    if ball.ycor() >= (court.upper_boundary_ycor - 15):
        ball.bounce_off_top_wall()

    if ball.ycor() <= (court.lower_boundary_ycor + 15):
        ball.bounce_off_bottom_wall()


court.exitonclick()


# TODO: create Scoreboard class
