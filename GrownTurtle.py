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
    
# Function draw triangle (equilatera)
def draw_triangle():
    side_lengths = []
    for index in range(3):
        side_length = screen.textinput("side lenght",f"Enter the side length {index + 1} of the square: ")
        # Convert string data type to float
        side_length = float(side_length)
        # Add side_length to the end of array side_lengths
        side_lengths.append(side_length)
    # Draw triangle
    for length in side_lengths:
        t.forward(length)
        t.left(120)
        
# Function draw circle
def draw_circle():
    radius = float(screen.textinput("Circle", "Enter the radius: "))
    # Draw circle
    t.begin_fill()
    t.fillcolor("yellow")
    t.pencolor("red")
    t.circle(radius)
    t.end_fill()
    t.penup()
    
# Function draw rectangle
def draw_rectangle():
    width = float(screen.textinput("Rectangle", "Enter the width: "))
    height = float(screen.textinput("Rectangle", "Enter the height: "))

    # Draw rectangle
    t.begin_fill()
    t.fillcolor("blue")
    t.pencolor("purple")

    for length in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()
    
# Main function
def main():
    shape = screen.textinput("Shapes","Enter the shape to draw (rectangle, circle, square, triangle): ").lower()
    if shape == "square":
        draw_square()
    elif shape == "triangle":
        draw_triangle()
    else:
        t.write("Invalid shape! Please enter again!")
main()
