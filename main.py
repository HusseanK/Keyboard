#All logic is within the keyboard creator
import keyboard_creator

'''
An interactive keyboard made as a test project

main file has been redesigned entirely.
'''

if __name__ =="__main__":
    #my 3 loops 
    keyboard_creator.run_keyboard() #20ms refresh
    keyboard_creator.check_keyboard_caps() #20ms refresh
    keyboard_creator.check_auto_complete() #60ms refresh

    #tkinters standard window-loop
    keyboard_creator.master.mainloop()