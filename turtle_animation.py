from turtle import Turtle, Screen
from random import randint

# Set up the screen
screen = Screen()
screen.title("Turtle Race")
screen.bgcolor("lightblue")

# Function to draw the racetrack
def draw_track():
    track_pen = Turtle()
    track_pen.speed(0)
    track_pen.penup()
    track_pen.goto(-140, 140)

    for step in range(15):
        track_pen.write(step, align='center', font=('Arial', 10, 'normal'))
        track_pen.right(90)
        for num in range(8):
            track_pen.penup()
            track_pen.forward(10)
            track_pen.pendown()
            track_pen.forward(10)
        track_pen.penup()
        track_pen.backward(160)
        track_pen.left(90)
        track_pen.forward(20)
    track_pen.hideturtle()

# Function to create a turtle player
def create_turtle(color, start_y):
    player = Turtle()
    player.color(color)
    player.shape('turtle')
    player.penup()
    player.goto(-160, start_y)
    player.pendown()
    return player

# Draw the racetrack
draw_track()

# Initialize turtles
turtle_colors = ['red', 'blue', 'green', 'orange']
start_positions = [100, 70, 40, 10]
players = []

for color, pos in zip(turtle_colors, start_positions):
    players.append(create_turtle(color, pos))

# Add a unique spin for each turtle at the start
spin_angles = [360, -360, 180, -180]
for player, angle in zip(players, spin_angles):
    player.right(angle)

# Start the race
for turn in range(100):
    for player in players:
        player.forward(randint(1, 5))

# Wait for user to close the screen
screen.mainloop()
