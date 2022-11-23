import tkinter as tk

window = tk.Tk()
window.title('Alphabatic Calculator')
frame = tk.Frame(window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(frame, borderwidth=3, width=40)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)

def myclick(number):
    entry.insert(tk.END, number)

button_1 = tk.Button(frame, text='A', padx=15, pady=5, width=3, command=lambda: myclick('A'))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(frame, text='B', padx=15, pady=5, width=3, command=lambda: myclick('B'))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(frame, text='C', padx=15, pady=5, width=3, command=lambda: myclick('C'))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(frame, text='D', padx=15, pady=5, width=3, command=lambda: myclick('D'))
button_4.grid(row=1, column=3, pady=2)
button_5 = tk.Button(frame, text='E', padx=15, pady=5, width=3, command=lambda: myclick('E'))
button_5.grid(row=2, column=0, pady=2)
button_6 = tk.Button(frame, text='F', padx=15, pady=5, width=3, command=lambda: myclick('F'))
button_6.grid(row=2, column=1, pady=2)
button_6 = tk.Button(frame, text='G', padx=15, pady=5, width=3, command=lambda: myclick('G'))
button_6.grid(row=2, column=2, pady=2)
button_6 = tk.Button(frame, text='H', padx=15, pady=5, width=3, command=lambda: myclick('H'))
button_6.grid(row=2, column=3, pady=2)
button_6 = tk.Button(frame, text='I', padx=15, pady=5, width=3, command=lambda: myclick('I'))
button_6.grid(row=3, column=0, pady=2)
button_6 = tk.Button(frame, text='J', padx=15, pady=5, width=3, command=lambda: myclick('J'))
button_6.grid(row=3, column=1, pady=2)
button_6 = tk.Button(frame, text='K', padx=15, pady=5, width=3, command=lambda: myclick('K'))
button_6.grid(row=3, column=2, pady=2)
button_6 = tk.Button(frame, text='L', padx=15, pady=5, width=3, command=lambda: myclick('L'))
button_6.grid(row=3, column=3, pady=2)
button_6 = tk.Button(frame, text='M', padx=15, pady=5, width=3, command=lambda: myclick('M'))
button_6.grid(row=4, column=0, pady=2)
button_6 = tk.Button(frame, text='N', padx=15, pady=5, width=3, command=lambda: myclick('N'))
button_6.grid(row=4, column=1, pady=2)
button_6 = tk.Button(frame, text='O', padx=15, pady=5, width=3, command=lambda: myclick('O'))
button_6.grid(row=4, column=2, pady=2)
button_6 = tk.Button(frame, text='P', padx=15, pady=5, width=3, command=lambda: myclick('P'))
button_6.grid(row=4, column=3, pady=2)
button_6 = tk.Button(master=frame, text='Q', padx=15, pady=5, width=3, command=lambda: myclick('Q'))
button_6.grid(row=5, column=0, pady=2)
button_6 = tk.Button(frame, text='R', padx=15, pady=5, width=3, command=lambda: myclick('R'))
button_6.grid(row=5, column=1, pady=2)
button_6 = tk.Button(frame, text='S', padx=15, pady=5, width=3, command=lambda: myclick('S'))
button_6.grid(row=5, column=2, pady=2)
button_6 = tk.Button(frame, text='T', padx=15, pady=5, width=3, command=lambda: myclick('T'))
button_6.grid(row=5, column=3, pady=2)
button_6 = tk.Button(frame, text='U', padx=15, pady=5, width=3, command=lambda: myclick('U'))
button_6.grid(row=6, column=0, pady=2)
button_6 = tk.Button(frame, text='V', padx=15, pady=5, width=3, command=lambda: myclick('V'))
button_6.grid(row=6, column=1, pady=2)
button_6 = tk.Button(frame, text='W', padx=15, pady=5, width=3, command=lambda: myclick('W'))
button_6.grid(row=6, column=2, pady=2)
button_6 = tk.Button(frame, text='X', padx=15, pady=5, width=3, command=lambda: myclick('X'))
button_6.grid(row=6, column=3, pady=2)
button_6 = tk.Button(frame, text='Y', padx=15, pady=5, width=3, command=lambda: myclick('Y'))
button_6.grid(row=7, column=1, pady=2)
button_6 = tk.Button(frame, text='Z', padx=15, pady=5, width=3, command=lambda: myclick('Z'))
button_6.grid(row=7, column=2, pady=2)


window.mainloop()