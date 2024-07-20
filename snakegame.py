import tkinter
import random
ROWS = 25
COLS = 25
TILE_SIZE = 25
WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
window = tkinter.Tk()
window.title("SNAKE GAME")
window.resizable(False, False)
canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bd=0, highlightthickness=0)
canvas.pack()
# Center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
# Initialize the game
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)  # Snake head
food = Tile(random.randint(0, COLS - 1) * TILE_SIZE, random.randint(0, ROWS - 1) * TILE_SIZE)
snake_body = []
velocityX = 0
velocityY = 0
gameover = False
score = 0
snake_colors = ["lime green", "yellow", "cyan", "magenta", "blue"]
current_color_index = 0
def change_direction(e):
    global velocityX, velocityY
    if gameover:
        return
    if e.keysym == "Up" and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0
    elif e.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0
def move():
    global snake, food, snake_body, gameover, score, current_color_index
    if gameover:
        return
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        gameover = True
        return
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            gameover = True
            return
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
        global current_color_index#change colour of snake as it eats
        current_color_index = (current_color_index + 1) % len(snake_colors)
        # Update score
        global score
        score += 1
 # Update the snake body
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i].x = snake_body[i - 1].x
        snake_body[i].y = snake_body[i - 1].y
    if snake_body:
        snake_body[0].x = snake.x
        snake_body[0].y = snake.y
  # Move the snake head
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE
def draw():
    global snake, food, snake_body, gameover, current_color_index, score

    move()
    canvas.delete("all")

    # Draw the snake head
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill=snake_colors[current_color_index])

    # Draw the snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill=snake_colors[current_color_index])
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")
    canvas.create_text(10, 10, text=f"Score: {score}", fill="white", font=("Arial", 16), anchor="nw")
    if gameover:
        canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, text="GAME OVER", fill="white", font=("Arial", 24))

    window.after(100, draw)  # 100ms = 1/10 seconds, 10 frames/sec

draw()
window.bind("<KeyPress>", change_direction)

window.mainloop()
