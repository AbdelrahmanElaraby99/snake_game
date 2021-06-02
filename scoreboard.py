from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans MS", 24, "normal")


class ScoreBoard(Turtle):
    """Class responsible for keeping the score and printing score and game over"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """refresh the screen writing"""
        self.clear()
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """print the game over text"""
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increments the score"""
        self.score += 1
        self.update_scoreboard()
