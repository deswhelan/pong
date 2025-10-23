from court import Court
from paddle import PlayerPaddle

court = Court().court

player_1_paddle = PlayerPaddle(court, 1)
court.onkeypress(player_1_paddle.move_up, "w")
court.onkeypress(player_1_paddle.move_down, "s")

player_2_paddle = PlayerPaddle(court, 2)
court.onkeypress(player_2_paddle.move_up, "Up")
court.onkeypress(player_2_paddle.move_down, "Down")

court.exitonclick()

# TODO: create Ball class
    # make it move
    # detect collision with wall and bounce accordingly
    # detect collision with paddle
    # detect when paddle misses (i.e. collision with edge of screen
# TODO: create Scoreboard class
