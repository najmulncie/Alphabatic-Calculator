from tkinter import *
import tkinter as tk
#create window
window = tk.Tk()

#window configuring....
window.geometry('300x300')
window.resizable(width=False, height=False)
window.title('Demo window')
#def first_entry():
    #print('I am your first entry')
    #result = entry_1.get()
    #label_2.configure(text = result)





#label
bt_1 = Button(window, text='A', bg='#000000', fg='#ffffff', width=5, font=('Arial 15'), border=2)
bt_1.grid(row=1, column=0)

bt_2= Button(window, text='A', bg='#000000', fg='#ffffff', width=5, font=('Arial 15'))
bt_2.grid(row=1, column=1)

bt_3 = Button(window, text='A', bg='#000000', fg='#ffffff', width=5, font=('Arial 15'))
bt_3.grid(row=1, column=2)

bt_4 = Button(window, text='A', bg='#000000', fg='#ffffff', width=5, font=('Arial 15'))
bt_4.grid(row=1, column=3)

bt_5 = Button(window, text='A', bg='#000000', fg='#ffffff', width=5, font=('Arial 15'))
bt_5.grid(row=2, column=0)

bt_6 = Button(window, text='A', bg='#000000', fg='#ffffff', width=5, font=('Arial 15'))
bt_6.grid(row=2, column=1)










##entry_1 = Entry(window, width=20)
#entry_1.grid(row=0, column=2)

#bt = Button(window, text= 'Click me!', bg='#000000', fg='#ffffff', width=10, font=('Arial 15'), command=first_entry)
#bt.grid(row=0, column=3)
window.mainloop();