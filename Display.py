from KeyboardClassFile import LabelClass, FrameClass
from tkinter.constants import *

final_text: list[str] = []
current_text: list[str] = []
receive_box = None

def run(master):
    global receive_box
    box_frame = FrameClass(master, bg="#3e3e5b", fill="both", side="top", padx=5, pady=5, expand=True)
    receive_box = LabelClass(box_frame, "Enter Text", side=TOP,fg="white",bg="#3e3e5b",wraplength=640)
    text_box = LabelClass(master, "Press a key to see the output")
    text_box.label.config(fg="white",bg="#1f1f2e",)


    return [box_frame,receive_box,text_box]


def set_text(text_box) -> None:
    #Stopping at 32 chars 
    if len(current_text) <= 32:
        text_box.label.config(text="")
        text_box.label.config(text="".join(current_text))