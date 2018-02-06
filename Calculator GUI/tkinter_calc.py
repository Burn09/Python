# Calculator GUI

import tkinter

# List of lists of tuples for calculator keys.
keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]

mainWindowPadding = 8

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding
# 'padx' is how many pixels to pad the widget from OUTSIDE its borders - CENTERS
# 'ipadx' is how many pixels to pad the widget from INSIDE the widgets border - EQUALLY EXPANDS

# Calculator display
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

# Defining the frame where all keys will be located? How does it expand?
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1


mainWindow.update()
mainWindow.minsize(keyPad.winfo_width()+mainWindowPadding, result.winfo_height()+keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width()+50+mainWindowPadding, result.winfo_height()+50+keyPad.winfo_height())


mainWindow.mainloop()
