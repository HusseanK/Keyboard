import Display
from KeyboardClassFile import ButtonClass, LabelClass
from tkinter.constants import *
from KeyCreator import button_nodes
import ctypes
import Spellchecker


from multiprocessing import Process, Queue


word_changed = False

'''
All my key-command and button-command logic is in here

a little convoluted but works :)

'''

def clear_text_box(event=None) -> None:
    global word_changed
    '''
    Just a simple clear-button, to restart from scratch
    '''
    Display.final_text.clear()
    Display.current_text.clear()
    Display.receive_box.label.config(text="")
    word_changed = True

def caps_lock_key(event=None)->None:
    '''
    Both the physical Capslock key, as well as the button are bound to this func

    The button uses Pyautogui to set off the keyboards Caps key
    and then i use Ctypes to check the caps state
    This ensures if that someone presses caps/button key too fast, it'll always be accurate
    '''
    if bool(ctypes.WinDLL("User32.dll").GetKeyState(0x14)):
        if str(button_nodes[0]).islower():
            for each_button in button_nodes:
                current_text = str(each_button)
                each_button.config(text=current_text.upper())
    else:
        if str(button_nodes[0]).isupper():
            for each_button in button_nodes:
                current_text = str(each_button)
                each_button.config(text=current_text.lower())


def erase(event=None)-> None:
    global word_changed

    '''
    Self explanatory - removes the last char
    '''
    if len(Display.current_text) > 0:
        Display.current_text.pop(-1)
    word_changed = True

def enter(event=None)-> None:
    global word_changed

    '''
    adds current text to the display window
    Limiting it to 32 characters, because words shouldnt exceed 32
    (Okay theres like 3 words that do in English, but most are under)
    '''
    if len(Display.current_text) > 0 :
        Display.final_text.append("".join(Display.current_text[ :32]) + " ")
        Display.receive_box.label.config(text = "".join(Display.final_text))
        Display.current_text.clear()

    clear_auto_text()
    word_changed = True

def button_invoke(key: str, event=None) -> None:
    global word_changed

    '''
    Set mainly for qwerty keys
    this is to just display text
    '''
    Display.current_text.append(key)
    word_changed = True



def check_auto_correct(master):
    global word_changed

    if word_changed:
        word_changed = False

        if len(Display.current_text) >= 2 and not Spellchecker.is_running:
            new_word = ''.join(Display.current_text)
            new_q = Queue()
            new_pr = Process(target = Spellchecker.autocorrect_text, args=(new_word, new_q))
            new_pr.start()

            def get_results():
                if not new_q.empty():
                    checks = new_q.get()
                    master.after(0, lambda: update_spellcheck_ui(checks))
                else:
                    master.after(10, get_results)
            get_results()
            

def update_spellcheck_ui(checks):
    for i in range(len(checks)):
        spell_checks[i].config(text="")
        spell_checks[i].config(text="".join(str(checks[i])))

    Spellchecker.is_running = False


def auto_correct(corrected: str) -> None:
    Display.current_text.clear()
    Display.current_text.append(corrected)

def clear_auto_text():
    for i in range(len(spell_checks)):
        spell_checks[i].config(text='')

def key_bindings(master) -> None:
    """Binds button keys
    Tab is a little odd,
    right now i have it to add a *tab space*
    but i think i want to remove this entirely
    rest are self-explanatory"""
    master.bind("<Tab>", lambda event: button_invoke("\t"))
    master.bind("<Return>", enter)
    master.bind("<space>", enter)
    master.bind("<Caps_Lock>", caps_lock_key)
    master.bind("<BackSpace>", erase)

    #Figure out what to do with Shift later
    # master.bind("<Shift_L>", caps_lock_key)
    # master.bind("<Shift_R>", caps_lock_key)

    '''
    This is a weird way i've made it so that the Qwerty keys on a physical keyboard bind properly
    Basically it uses the Keypress (eg <Q>) to call button_invoke.
    it's weird, but works.'''
    for new_button in button_nodes:
        master.bind("<"+ str(new_button).lower() + ">",
                     lambda event, btn= new_button: button_invoke(str(btn).lower()))
        master.bind("<"+ str(new_button).upper() + ">",
            lambda event, btn = new_button: button_invoke(str(btn).upper()))

spell_checks = []

def run(tk, box_frame) -> None:
    '''
    runs this file, inserting the root window
    box-frame is used for the *clear* button solely. Might change this
    '''
    key_bindings(tk)


    #Make func later, fix
    clear_button = ButtonClass(
        master = box_frame, text = "Clear",
        command =  clear_text_box,
        side=RIGHT, bg="#1f1f2e", expand=False)
    
    hollow_space = LabelClass(
        master = box_frame, 
        text = "",
        width=12,
        side=LEFT, expand=True,
        anchor='s',fg="white",bg="#3e3e5b",
        )
    
    spell_check1 = ButtonClass(
        master = box_frame, text = "test1",
        width=12,
        command = lambda : auto_correct(str(spell_check1)),
        side=LEFT, bg="#1f1fff", expand=True)
    
    spell_check2 = ButtonClass(
        master = box_frame, text = "test2",
        width=12,
        command = lambda : auto_correct(str(spell_check2)),
        side=LEFT, bg="#1f1fff", expand=True)
    
    spell_check3 = ButtonClass(
        master = box_frame, text = "test3",
        width=12,
        command = lambda : auto_correct(str(spell_check3)),
        side=LEFT, bg="#1f1fff", expand=True)
    
    spell_checks.append(spell_check1)
    spell_checks.append(spell_check2)
    spell_checks.append(spell_check3)

    hollow_space2 = LabelClass(
        master = box_frame, 
        text = "",
        width=12,
        side=LEFT, expand=True,
        anchor='s',fg="white",bg="#3e3e5b",
        )
