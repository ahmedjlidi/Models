import ttkbootstrap as ttk
import tkinter as tk
import warnings
from tkinter import filedialog
from PIL import Image, ImageTk

warnings.filterwarnings("ignore")

CONFIG = {"title": "Window", "size": "1280x720", "resizable": False, "logo": "resources/logo.ico"}


def loadFile():
    # Open file dialog and allow user to select an image file
    file_path = filedialog.askopenfilename(title="Select an Image File",
                                           filetypes=[("Image files", "*.jpg *.png *.jpeg")])

    if file_path:
        imgframe.update(file_path)
    else:
        print("No file selected")


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(CONFIG['size'])
        self.title(CONFIG['title'])
        self.resizable(CONFIG['resizable'], CONFIG['resizable'])
        self.iconbitmap(CONFIG['logo'])
        #Run

    def mailoop(self):
        self.mainloop()


class Menu(ttk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initMenu()
        self.parent.config(menu=self)

    def initMenu(self):
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(label="Upload", command=loadFile)
        self.add_cascade(label="File", menu=file_menu)


class SideFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initFrame()

    def initFrame(self):
        # Set the width of the frame to 30% of the parent window
        width = 275

        # Add borders with a relief style and border width
        self.config(width=width, borderwidth=2, relief="solid")  # Border added here
        self.pack(side="left", fill="y")
        self.pack_propagate(False)  # Ensure the frame keeps its set width


class ImageFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.width = 800
        self.height = 600
        self.initFrame()


    def initFrame(self):
        # Add borders with a relief style and border width
        self.config(width=self.width, height=self.height, borderwidth=2, relief="solid")  # Border added here
        self.place(x=380, y=50)
        self.pack_propagate(False)  # Ensure the frame keeps its set wi

    def update(self,path):
        img = Image.open(path)
        if img.size[0] > self.width or img.size[1] > self.height:
            img = img.resize((800, 600), Image.LANCZOS)  # Resize to frame's size
            print("something")
        else:
            print("Nothing")

        self.photo = ImageTk.PhotoImage(img)
            # Create a Label to hold the image
        label = ttk.Label(self, image=self.photo)
        label.pack(expand=True)
        label.place(relx=0.5, rely=0.5, anchor="center")  # Make the label fill the entire frame


window = Window()
menu = Menu(window)

frame = SideFrame(window)
imgframe = ImageFrame(window)

window.mainloop()
