import tkinter as tk

CELL_SIZE = 40
ERASER_SIZE = 20
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 400

def on_mouse_move(event):
    canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
    overlapping = canvas.find_overlapping(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
    for item in overlapping:
        if item != eraser:
            canvas.itemconfig(item, fill='red')

root = tk.Tk()
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Draw grid
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue', outline='black')

# Create eraser (initial position offscreen)
eraser = canvas.create_rectangle(-ERASER_SIZE, -ERASER_SIZE, 0, 0, fill='pink', outline='')

canvas.bind("<Motion>", on_mouse_move)

root.mainloop()
