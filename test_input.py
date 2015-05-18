from Tkinter import Tk, Entry

root = Tk()

def click(key):
    # print the key that was pressed
    #print key.char
    print entry.get()

entry = Entry()
entry.grid()
# Bind entry to any keypress
entry.bind("<Key>", click)

root.mainloop()
