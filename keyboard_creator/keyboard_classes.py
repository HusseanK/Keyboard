import tkinter
'''
Just a file that holds all my Classes
for things like Buttons, Frames, and Labels
'''
class BaseClass(tkinter.Tk):
    '''
    Just using a base class for my tkinter window
    mainly so that i can set it up all in here
    *seems* unnecessary, but if i want to actually expand a little, may come in handy
    '''

    def __init__(self, **kwargs):
        super().__init__()

        self.title("Interactive Keyboard")
        self.geometry("1800x800")
        self.config(bg="#666699")

        '''
        looping through kwargs
        apparently newer Python has this inbuilt
        '''
        for key, value in kwargs.items():
            if key in self.config().keys():
                self.config(**{key: value})

class ButtonClass(tkinter.Button):
    '''
    Button class, inherits the original tkinter.Button class
    this is so that each button is an actual button, rather than a reference
    '''
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, bg="#666699")
        #takefocus is 0, because i dont want space/tab to touch the buttons by default
        self.config(height=1,takefocus=0,
            font=("Arial", 26, "bold"),
            fg="white")
        #My Base pack, this just makes everything work *decently* into shape
        self.pack(expand = True, padx=5, pady=5, anchor='s')

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

class LabelClass(tkinter.Label):
    '''
    Updated to create an actual label rather than a reference
    '''
    def __init__(self, master, text, **kwargs):
        #Base label things, all my labels are almost-identical
        super().__init__(master=master,
            text=text,
            font=("Arial", 26, "bold"),
            bg="#666699",
            fg="white",
            width=48,
            height=1,)
        
        self.pack(expand = True,fill='both', padx=5, pady=5, anchor='s')
        
        #looping through kwargs
        for key, value in kwargs.items():
            if key in self.config().keys():
                self.config(**{key: value})
            if key in self.pack_info():
                self.pack_configure(**{key: value})

class FrameClass(tkinter.Frame):
    '''
    Frame class, inherits the original tkinter.Frame class
    this is so that each Frame is an actual Frame, rather than a reference
    So that i dont have to access franes by doing current_frame.frame
    '''
    def __init__(self, master, **kwargs):
        super().__init__(master, bg="#1f1f2e")
        self.pack(fill='both', padx=5, pady=5, anchor="s")

        #looping through kwargs
        for key, value in kwargs.items():
            if key in self.config().keys():
                self.config(**{key: value})
            if key in self.pack_info():
                self.pack_configure(**{key: value})
