import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")

        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.color = "black"
        self.brush_size = 2

        self.setup_buttons()

        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)

        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, width=self.brush_size)

    def change_brush_size(self, size):
        self.brush_size = size

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def setup_buttons(self):
        frame = tk.Frame(self.root, bg="gray")
        frame.pack(fill=tk.BOTH, expand=True)

        brush_button = tk.Button(frame, text="Brush Size", command=lambda: self.change_brush_size(2), width=10)
        brush_button.grid(row=0, column=0)

        color_button = tk.Button(frame, text="Color", command=self.change_color, width=10)
        color_button.grid(row=0, column=1)

        clear_button = tk.Button(frame, text="Clear Canvas", command=self.clear_canvas, width=10)
        clear_button.grid(row=0, column=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
