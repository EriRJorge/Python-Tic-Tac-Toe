
import turtle as t

# Constants
SQUARE_SIZE = 100
BOARD_OFFSET = 150

# Global variable to keep track of the current player
current_player = 'X'

def point_to_square(x, y):
    """
    Maps a point (x, y) to a corresponding square on the Tic-Tac-Toe board.
    """
    col = int((x + BOARD_OFFSET) // SQUARE_SIZE)
    row = int((BOARD_OFFSET - y) // SQUARE_SIZE)

    if 0 <= row <= 2 and 0 <= col <= 2:
        squares = ["Northwest", "North", "Northeast",
                   "West", "Center", "East",
                   "Southwest", "South", "Southeast"]
        return squares[row * 3 + col]
    else:
        return "NoSquare"

def square_to_point(square):
    """
    Returns the center point of the given square on the Tic-Tac-Toe board.
    """
    col = ['Northwest', 'West', 'Southwest'].index(square) if 'West' in square else ['North', 'Center', 'South'].index(square)
    row = ['Northwest', 'North', 'Northeast'].index(square) if 'North' in square else ['West', 'Center', 'East'].index(square)

    return (col * SQUARE_SIZE + SQUARE_SIZE / 2 - BOARD_OFFSET,
            -row * SQUARE_SIZE + SQUARE_SIZE / 2 + BOARD_OFFSET)

def drawX(square):
    """
    Draws an X centered within the specified square on the game board.
    """
    x, y = square_to_point(square)
    t.penup()
    t.goto(x - SQUARE_SIZE / 3, y - SQUARE_SIZE / 3)
    t.pendown()
    t.setheading(45)
    t.forward(SQUARE_SIZE * 0.7)
    t.backward(SQUARE_SIZE * 1.4)
    t.forward(SQUARE_SIZE * 0.7)
    t.left(90)
    t.forward(SQUARE_SIZE * 1.4)
    t.penup()

def drawO(square):
    """
    Draws an O (big circle) centered within the specified square on the game board.
    """
    x, y = square_to_point(square)
    t.penup()
    t.goto(x, y - SQUARE_SIZE / 3)
    t.pendown()
    t.circle(SQUARE_SIZE / 3)
    t.penup()

def mouseclick(x, y):
    """
    Draws the current player's mark upon a mouse click event.
    """
    global current_player
    square = point_to_square(x, y)
    if square != "NoSquare":
        if current_player == 'X':
            drawX(square)
            current_player = 'O'
        else:
            drawO(square)
            current_player = 'X'
    t.title("Current Player: " + current_player)
    update_cursor()

def update_cursor():
    """
    Updates the cursor shape based on the current player.
    """
    if current_player == 'X':
        t.getcanvas().config(cursor="X_cursor")
    else:
        t.getcanvas().config(cursor="circle")

def turnX():
    """
    Sets the current player to X.
    """
    global current_player
    current_player = 'X'
    t.title("Current Player: " + current_player)
    update_cursor()

def turnO():
    """
    Sets the current player to O.
    """
    global current_player
    current_player = 'O'
    t.title("Current Player: " + current_player)
    update_cursor()

def main():
    t.setup(400, 400)
    t.title("Tic-Tac-Toe")
    t.tracer(0)  # Disable animation
    t.hideturtle()
    t.penup()

    # Draw Tic-Tac-Toe board
    for i in range(2):
        t.penup()
        t.goto(-150, 50 - i * 100)
        t.pendown()
        t.forward(300)
        t.penup()
        t.goto(-50 - i * 100, 150)
        t.setheading(-90)
        t.pendown()
        t.forward(300)

    # Register callback functions
    t.listen()
    t.onscreenclick(mouseclick)
    t.onkeyrelease(turnX, 'x')
    t.onkeyrelease(turnO, 'o')

    t.title("Current Player: " + current_player)
    update_cursor()
    t.mainloop()

if __name__ == "__main__":
    main()