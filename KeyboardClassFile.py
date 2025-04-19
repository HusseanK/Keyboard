import tkinter
from tkinter import RIDGE, BOTH, X, BOTTOM, LEFT

'''
Just a file that holds all my Classes
for things like Buttons, Frames, and Labels
i like objects being separated
'''

class BaseClass:
    '''
    Just using a base class for my tkinter window
    mainly so that i can set it up all in here
    *seems* unnecessary, but if i want to actually expand a little, may come in handy

    I can probably add the root window to this class, and have others access it easier
    but honestly this is fine for now
    '''
    def __init__(self, master):
        self.master = master
        self.master.title("Interactive Keyboard")
        self.master.geometry("1800x1200") #Set the window size to 1800x1200
        self.master.config(bg="#666699")


class ButtonClass(tkinter.Button):
    '''
    Button class, inherits the original tkinter.Button class
    this is so that each button is an actual button, rather than a reference
    So that i dont have to access buttons by doing current_button.button
    '''
    def __init__(self, master, text, **kwargs):
        ''' Takes the original init from the button, sets text and bg colour(Default)'''
        super().__init__(master, text=text, bg="#666699")

        '''takefocus is 0, because i dont want space/tab to touch the buttons by default'''
        self.config(height=1,takefocus=0,
            font=("Arial", 26, "bold"),
            fg="white")
        self.pack(expand = True, padx=5, pady=5, anchor='s')

        '''
        looping through kwargs
        apparently newer Python has this inbuilt'''
        for key, value in kwargs.items():
            if key in self.config().keys():
                self.config(**{key: value})
            if key in self.pack_info():
                self.pack_configure(**{key: value})
    

    '''
    theres a specific reason for this, and right now seems unnecessary
    but it is neccesary i promise
    '''
    def invoke_button(self, event=None):
        self.invoke(event)

    '''changed the str dunder method
    because i like using str(button) over button.text
    May change it later'''
    def __str__(self):
        return self.cget('text')

class LabelClass:
    '''
    Need to update this later, but not currently neccessary
    want it to inherit from the label class like the other two
    '''
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
        self.label.pack(expand = True,fill=BOTH, padx=5, pady=5, anchor='s')

        #looping through kwargs
        for key, value in kwargs.items():
            if key in self.label.config().keys():
                self.label.config(**{key: value})
            if key in self.label.pack_info():
                self.label.pack_configure(**{key: value})
        


class FrameClass(tkinter.Frame):
    '''
    Frame class, inherits the original tkinter.Frame class
    this is so that each Frame is an actual Frame, rather than a reference
    So that i dont have to access franes by doing current_frame.frame
    '''
    def __init__(self, master, **kwargs):
        '''takes the original init'''
        super().__init__(master, bg="#1f1f2e")
        self.pack(fill=BOTH, padx=5, pady=5, anchor="s")

        #looping through kwargs
        for key, value in kwargs.items():
            if key in self.config().keys():
                self.config(**{key: value})
            if key in self.pack_info():
                self.pack_configure(**{key: value})
