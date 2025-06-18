import tkinter as tk
from PIL import ImageGrab, ImageTk

class ScreenshotEditor(tk.Toplevel):
    """Simple editor to draw rectangles or lines on a screenshot."""
    def __init__(self, root, image):
        super().__init__(root)
        self.title("Screenshot Editor")
        self.mode = tk.StringVar(value='line')

        toolbar = tk.Frame(self)
        tk.Button(toolbar, text='Line', command=lambda: self.mode.set('line')).pack(side=tk.LEFT)
        tk.Button(toolbar, text='Rect', command=lambda: self.mode.set('rect')).pack(side=tk.LEFT)
        toolbar.pack(fill=tk.X)

        self.canvas = tk.Canvas(self, width=image.width, height=image.height, cursor='cross')
        self.canvas.pack()
        self.img = image
        self.tk_img = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.tk_img, anchor='nw')

        self.start_x = self.start_y = 0
        self.current = None
        self.canvas.bind('<ButtonPress-1>', self.on_start)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_release)

    def on_start(self, event):
        self.start_x, self.start_y = event.x, event.y
        if self.mode.get() == 'line':
            self.current = self.canvas.create_line(event.x, event.y, event.x, event.y,
                                                   fill='red', width=2)
        else:
            self.current = self.canvas.create_rectangle(event.x, event.y, event.x, event.y,
                                                        outline='red', width=2)

    def on_drag(self, event):
        if self.current:
            self.canvas.coords(self.current, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, _event):
        self.current = None


class ScreenshotApp:
    """Main application window for capturing a region of the screen."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screenshot App")
        tk.Button(self.root, text='Capture', command=self.start_capture).pack(padx=20, pady=20)

        self.overlay = None
        self.sel_rect = None
        self.start_x = self.start_y = 0
        self.start_x_screen = self.start_y_screen = 0

    def start_capture(self):
        self.root.withdraw()
        self.overlay = tk.Toplevel(self.root)
        self.overlay.attributes('-fullscreen', True)
        self.overlay.attributes('-alpha', 0.3)
        self.overlay.attributes('-topmost', True)
        self.ov_canvas = tk.Canvas(self.overlay, cursor='cross', bg='gray', highlightthickness=0)
        self.ov_canvas.pack(fill=tk.BOTH, expand=True)

        self.ov_canvas.bind('<ButtonPress-1>', self.on_select_start)
        self.ov_canvas.bind('<B1-Motion>', self.on_select_drag)
        self.ov_canvas.bind('<ButtonRelease-1>', self.on_select_release)

    def on_select_start(self, event):
        self.start_x, self.start_y = event.x, event.y
        self.start_x_screen, self.start_y_screen = event.x_root, event.y_root
        self.sel_rect = self.ov_canvas.create_rectangle(event.x, event.y, event.x, event.y,
                                                        outline='red', width=2)

    def on_select_drag(self, event):
        self.ov_canvas.coords(self.sel_rect, self.start_x, self.start_y, event.x, event.y)

    def on_select_release(self, event):
        x1 = min(self.start_x_screen, event.x_root)
        y1 = min(self.start_y_screen, event.y_root)
        x2 = max(self.start_x_screen, event.x_root)
        y2 = max(self.start_y_screen, event.y_root)
        self.overlay.destroy()
        image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        self.root.deiconify()
        ScreenshotEditor(self.root, image)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    ScreenshotApp().run()
