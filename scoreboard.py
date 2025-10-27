from turtle import Turtle

ALIGN = "center"
COLOUR = "white"
FONT = ("Courier", 32, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color(COLOUR)
        self.hideturtle()
        self.penup()
        self.setpos(0, 250)
        self.display_current_score()

    def display_current_score(self):
        self.write(f"{self.player_1_score}  {self.player_2_score}", align=ALIGN, font=FONT)

    def update_score(self, is_player_1_score):
        self.clear()

        if is_player_1_score:
            self.player_1_score += 1
        else:
            self.player_2_score += 1

        self.display_current_score()