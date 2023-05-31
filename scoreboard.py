from turtle import Turtle

# CONSTANTS

ALIGNMENT = "center"


class Scoreboard(Turtle):

    # Default score/high-score set to 0. Setting initial position and color, hiding turtle, and initial write. Also,
    # high score text file is checked and high score set accordingly

    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0, 275)
        self.hideturtle()
        self.color("white")
        with open('high_score.txt', mode="r") as file:
            self.high_score = int(file.read())
            file.close()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", move=False, align=ALIGNMENT)

    # Method for adding a point. Clears and rewrites score after adding point to tally

    def point(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", move=False, align=ALIGNMENT)

    # Method for game over message after loss condition is met

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="YOU STINK, LOSER", align="center")

    # Method for scoreboard updating. Clear and rewriting score without changing it

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", move=False, align=ALIGNMENT)

    # Method that checks for high score, updates it if condition is met

    def end(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
                file.close()
        self.update_scoreboard()
