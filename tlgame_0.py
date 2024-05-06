import tkinter as tk
import random

# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
ROAD_WIDTH = 50
INTERSECTION_SIZE = 100
NUM_INTERSECTIONS = 10
MAX_DELAY = 60  # Maximum delay in seconds for each traffic light

# Define colors
BACKGROUND_COLOR = "#FFFFFF"
ROAD_COLOR = "#808080"
INTERSECTION_COLOR = "#000000"
CAR_COLOR = "#FF0000"

# Create the main window
root = tk.Tk()
root.title("Traffic Optimization Game")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Create the canvas
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

# Define a function to create a road
def create_road(start_x, start_y, end_x, end_y):
    canvas.create_rectangle(start_x, start_y, end_x, end_y, fill=ROAD_COLOR, outline="")

# Define a function to create an intersection
def create_intersection(x, y):
    canvas.create_rectangle(x - INTERSECTION_SIZE // 2, y - INTERSECTION_SIZE // 2,
                            x + INTERSECTION_SIZE // 2, y + INTERSECTION_SIZE // 2,
                            fill=INTERSECTION_COLOR, outline="")

# Define a function to create a car
def create_car(x, y, direction):
    car = canvas.create_rectangle(x, y, x + 20, y + 10, fill=CAR_COLOR, outline="")
    canvas.move(car, 10, 5)
    canvas.update()
    return car

# Define a function to move a car
def move_car(car, direction, delay):
    if direction == "left":
        canvas.move(car, -10, 0)
    elif direction == "right":
        canvas.move(car, 10, 0)
    elif direction == "up":
        canvas.move(car, 0, -10)
    elif direction == "down":
        canvas.move(car, 0, 10)
    canvas.after(delay, move_car, car, direction, delay)

# Create roads and intersections
for i in range(NUM_INTERSECTIONS):
    x = random.randint(ROAD_WIDTH, WINDOW_WIDTH - ROAD_WIDTH)
    y = random.randint(ROAD_WIDTH, WINDOW_HEIGHT - ROAD_WIDTH)
    create_road(0, y, WINDOW_WIDTH, y)
    create_road(x, 0, x, WINDOW_HEIGHT)
    create_intersection(x, y)

# Create cars and move them
directions = ["left", "right", "up", "down"]
for i in range(10):
    x = random.randint(ROAD_WIDTH, WINDOW_WIDTH - ROAD_WIDTH - 20)
    y = random.randint(ROAD_WIDTH, WINDOW_HEIGHT - ROAD_WIDTH - 10)
    direction = random.choice(directions)
    car = create_car(x, y, direction)
    delay = random.randint(10, MAX_DELAY)
    move_car(car, direction, delay)

# Start the main event loop
root.mainloop()