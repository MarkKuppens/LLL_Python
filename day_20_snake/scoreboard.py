from turtle import Turtle

HIGH_SCORE_FILE = "data.txt"

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(HIGH_SCORE_FILE) as data:
            self.high_score = int(data.read())
        self.clear()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def write_high_score(self):
        """Write the current high score to a file."""
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()