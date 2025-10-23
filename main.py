from court import Court
from paddle import PlayerPaddle

court = Court().court

player_paddle = PlayerPaddle()
court.onkeypress(player_paddle.move_up, "Up")
court.onkeypress(player_paddle.move_down, "Down")


court.exitonclick()

# TODO: create Ball class
    # make it move
    # detect collision with wall and bounce accordingly
    # detect collision with paddle
    # detect when paddle misses (i.e. collision with edge of screen
# TODO: create Scoreboard class
