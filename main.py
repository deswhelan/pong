from ball import Ball
from court import Court
from paddle import Paddle
from scoreboard import ScoreBoard

STARTING_BALL_SPEED = 6
BALL_SPEED_INCREMENT = 0.5

court = Court().court

player_1_paddle = Paddle(court, 1)
court.onkeypress(player_1_paddle.move_up, "w")
court.onkeypress(player_1_paddle.move_down, "s")

player_2_paddle = Paddle(court, 2)
court.onkeypress(player_2_paddle.move_up, "Up")
court.onkeypress(player_2_paddle.move_down, "Down")

ball = Ball(court)
scoreboard = ScoreBoard()

ball_speed = STARTING_BALL_SPEED

game_is_on = True

while game_is_on:
    ball.move(ball_speed)

    # bounce ball off sidelines
    if ball.ycor() >= (court.upper_boundary_ycor - 15) or ball.ycor() <= (court.lower_boundary_ycor + 15):
        ball.bounce_off_wall()

    # bounce ball off paddles
    if player_1_paddle.has_hit_ball(ball, 1) or player_2_paddle.has_hit_ball(ball, 2):
        ball_speed += BALL_SPEED_INCREMENT
        ball.bounce_off_paddle()

    # update score and "re-serve" in appropriate direction if ball goes out-of-bounds
    if ball.xcor() >= court.upper_boundary_xcor or ball.xcor() <= court.lower_boundary_xcor:
        ball_speed = STARTING_BALL_SPEED
        is_player_1_score = ball.is_moving_right(ball.heading())
        scoreboard.update_score(is_player_1_score)
        ball.serve()

court.exitonclick()

# TODO: create Scoreboard class
