from turtle import Turtle, Screen
screen = Screen()
class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score_board()
    
    def update_score_board(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score_board()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
    
    def welcoming(self):
        self.goto(0, 0)
        speed = screen.textinput("Speed Selection", "Enter snake speed (slow, medium, fast):").strip().lower()
        return speed

