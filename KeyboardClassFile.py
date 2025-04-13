import tkinter
from tkinter import RIDGE, BOTH, X, BOTTOM, LEFT

class BaseClass:
    def __init__(self, master):
        self.master = master
        self.master.title("Interactive Keyboard")
        self.master.geometry("1800x800") #Set the window size to 800x600
        self.master.config(bg="#666699")

class ButtonClass(tkinter.Button):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, bg="#666699")
        # self.button = tkinter.Button(master, text=text, command=command)
        self.config(height=1,takefocus=0,
            font=("Arial", 26, "bold"),
            fg="white")
        
        self.pack(expand = True, padx=5, pady=5)

        for key, value in kwargs.items():
            if key in self.config().keys():
                self.config(**{key: value})
            if key in self.pack_info():
                self.pack_configure(**{key: value})
        
    def invoke_button(self, event=None):
        self.invoke(event)
    
    def __str__(self):
        return self.cget("text")

class LabelClass:
    def __init__(self, master, text, **kwargs):
        self.master = master
        self.label = tkinter.Label(
            master,
            text=text,
            font=("Arial", 26, "bold"),
            bg="#666699",
            fg="white",
            width=48,
            height=1,
        )
        self.label.pack(expand = True,fill=BOTH, padx=5, pady=5)

        for key, value in kwargs.items():
            if key in self.label.config().keys():
                self.label.config(**{key: value})
            if key in self.label.pack_info():
                self.label.pack_configure(**{key: value})
        


class FrameClass(tkinter.Frame):
    #Inherits from the Frame class
    #Need to do the same to top 3 classes ^^
    def __init__(self, master, **kwargs):
        #Turns the actual class into a direct widget, rather than reference
        super().__init__(master, bg="#1f1f2e")
        self.pack(fill=BOTH, padx=5, pady=5)
        #Checks any in-put kwargs and separates them
        for key, value in kwargs.items():
            if key in self.config().keys():
                self.config(**{key: value})
            if key in self.pack_info():
                self.pack_configure(**{key: value})
