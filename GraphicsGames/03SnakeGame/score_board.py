from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,250)
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.show_score()
        
        
    def incr_score(self):
        self.score += 1
        self.clear()
        self.show_score()
    
    def show_score(self):
        self.write(arg= f"Score : {self.score}" , align= "center" , font= ("Arial" , 15 , "bold"))






