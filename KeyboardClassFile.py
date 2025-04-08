import tkinter
from tkinter import RIDGE, BOTH, X, BOTTOM, LEFT

class BaseClass:
    def __init__(self, master):
        self.master = master
        self.master.title("Interactive Keyboard")
        self.master.geometry("1800x800") #Set the window size to 800x600
        self.master.config(bg="#666699")

class ButtonClass:
    def __init__(self, master, text, command, **kwargs):
        self.button = tkinter.Button(master, text=text, command=command, takefocus=0)
        self.button.config(
            font=("Arial", 26, "bold"),
            bg="#666699",
            fg="white")
        self.button.pack()

        for key, value in kwargs.items():
            if key in self.button.config().keys():
                self.button.config(**{key: value})
            if key in self.button.pack_info():
                self.button.pack_configure(**{key: value})
        
    def invoke_button(self, event=None):
        self.button.invoke()

class LabelClass:
    def __init__(self, master, text):
        self.master = master
        self.label = tkinter.Label(
            master,
            text=text,
            font=("Arial", 26, "bold"),
            bg="#666699",
            fg="white",
            width=48,
        )
        self.label.pack()