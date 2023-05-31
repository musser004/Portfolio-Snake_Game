from turtle import Turtle

# CONSTANTS

NUMBER_OF_TURTLES = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    # Initializing snake and setting snake head variable

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Method to add an additional snake segment

    def add_segment(self, position):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")
        turtle.goto(position)
        self.segments.append(turtle)

    # Method to create initial snake on screen at constant starting position

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Method to move the snake segments to where their leading segment previously was, then move snake head forward
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Methods to change snake head direction. Does not allow instant 180 degree turns

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Method to add a segment to the tail end of the snake

    def extend(self):
        self.add_segment(self.segments[-1].position())

