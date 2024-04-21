# Turtle Lap #4
# Code will be start below this line
import turtle
# Set up the turtle
t = turtle.Turtle()
screen = turtle.Screen()

# Set up pen size, color.
t.pendown()
t.pensize(5)
t.pencolor("blue")

# Function draw square
def draw_square():
    side_length = 0.0
    # Create a loop that re-enters the length if less than or equal to 0
    while side_length <= 0: 
        side_length = screen.textinput("side lenght","Enter the side length of the square: ")
        # Convert string data type to float
        side_length = float(side_length)
        if side_length > 0:
            break
    # Draw square
    t.begin_fill()
    t.fillcolor("yellow")
    for _ in range(4):
        t.forward(side_length)
        t.left(90)
    t.end_fill()
    t.penup()

# Main function
def main():
    shape = screen.textinput("Shapes","Enter the shape to draw (rectangle, circle, square, triangle): ").lower()
    if shape == "square":
        draw_square()
    else:
        print("Invalid shape! Please enter again!")
main()
