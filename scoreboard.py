from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = self.retrieve_highscore()
        self.retrieve_highscore()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def retrieve_highscore(self):
        with open("data.txt") as file:
            return int(file.read())

    def save_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

