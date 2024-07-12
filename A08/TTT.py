import turtle as t

screen = t.Screen()
screen.setup(800, 800)
screen.setworldcoordinates(-5, -5, 5, 5)
screen.bgcolor('light gray')
screen.tracer(0, 0)
t.hideturtle()

# Draw the board
def draw_board():
    t.pencolor('green')
    t.pensize(10)
    t.up()
    t.goto(-3, -1)
    t.seth(0)
    t.down()
    t.fd(6)
    t.up()
    t.goto(-3, 1)
    t.seth(0)
    t.down()
    t.fd(6)
    t.up()
    t.goto(-1, -3)
    t.seth(90)
    t.down()
    t.fd(6)
    t.up()
    t.goto(1, -3)
    t.seth(90)
    t.down()
    t.fd(6)

# Check if the position is within the grid boundaries
def is_within_boundaries(x, y):
    return -3 <= x <= 3 and -3 <= y <= 3

# Draw Circle Shape
def draw_circle(x, y):
    if is_within_boundaries(x, y):
        box_size = 2
        box_x = int((x + box_size / 2) // box_size) * box_size
        box_y = int((y + box_size / 2) // box_size) * box_size
        t.up()
        t.goto(box_x, box_y - 0.75)
        t.seth(0)
        t.color('red')
        t.down()
        t.circle(0.75, steps=100)
        t.up()

# Draw X Shape
def draw_x(x, y):
    if is_within_boundaries(x, y):
        box_size = 2
        box_x = int((x + box_size / 2) // box_size) * box_size
        box_y = int((y + box_size / 2) // box_size) * box_size
        t.color('blue')
        t.up()
        t.goto(box_x - 0.75, box_y - 0.75)
        t.down()
        t.goto(box_x + 0.75, box_y + 0.75)
        t.up()
        t.goto(box_x - 0.75, box_y + 0.75)
        t.down()
        t.goto(box_x + 0.75, box_y - 0.75)
        t.up()

def draw(b):
    draw_board()
    screen.update()

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
draw(b)

screen.listen()

def play_x():
    screen.title("Current Player: X")
    t.getcanvas().config(cursor="X_cursor")
    screen.onclick(lambda x, y: draw_x(x, y))

def play_circle():
    screen.title("Current Player: O")
    t.getcanvas().config(cursor="circle")
    screen.onclick(lambda x, y: draw_circle(x, y))

screen.onkey(play_x, 'x')
screen.onkey(play_circle, 'o')

play_x()
t.mainloop()
