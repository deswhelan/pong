from court import Court
from paddle import PlayerPaddle, ComputerPaddle

court = Court().court

player_1_paddle = PlayerPaddle()
court.onkeypress(player_1_paddle.move_up, "Up")
court.onkeypress(player_1_paddle.move_down, "Down")

player_2_paddle = ComputerPaddle()

court.exitonclick()

# TODO: create Ball class
    # make it move
    # detect collision with wall and bounce accordingly
    # detect collision with paddle
    # detect when paddle misses (i.e. collision with edge of screen
# TODO: create Scoreboard class
