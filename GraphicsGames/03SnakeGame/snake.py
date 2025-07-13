from turtle import Turtle , Screen


my_screen = Screen()
class Snake:

    # Structure all snakes
    def __init__(self):      
        self.segment = [] 
        self.create_snake()
        self.head = self.segment[0]
        self.tail_pos = self.segment[-1].pos()

    def create_snake(self):
        i=20
        for _ in range (3):
            new_turtle = Turtle()
            new_turtle.fillcolor('white')
            new_turtle.penup()
            new_turtle.shape('square')
            new_turtle.setx(i)
            self.segment.append(new_turtle)
            i-=20

    def extend_body(self):
        new_turtle = Turtle()
        new_turtle.fillcolor('white')
        new_turtle.penup()
        new_turtle.shape('square')
        new_turtle.goto(self.tail_pos)
        self.segment.append(new_turtle)

        
    # Functionality for moving
    def move(self):
        for i in range(len(self.segment) - 1,0,-1):
            t = self.segment[i]
            pos = self.segment[i-1].pos()
            t.goto(pos)

        self.head.forward(20)
        self.key(self.head)



    
    # Functions of keys
    def key(self,t1):
        def turn_up():
            if t1.heading() != 270:
                t1.seth(90)
        
        def turn_down():
            if t1.heading() != 90:
                t1.seth(270)
            
        
        def turn_left():
            if t1.heading() != 0:
                t1.seth(180)
            
        
        def turn_right():
            if t1.heading() != 180:
                t1.seth(0)
        
        my_screen.listen()
        my_screen.onkey(turn_up , 'Up')
        my_screen.onkey(turn_down , 'Down')
        my_screen.onkey(turn_left , 'Left')
        my_screen.onkey(turn_right , 'Right')
