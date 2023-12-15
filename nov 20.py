from os import name
from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Registration Form")
root.minsize(500,300)
root.maxsize(500,300)

label = Label(root, text='Registration', bg='green',fg='white', width= 20)
label.pack(fill=BOTH, expand=0)
img = PhotoImage(file='logo.png')
Label(root, image=img).pack()
message_text = 'Please fill out the registration from by completing the details.'
Message(root, text=message_text, width=250).pack()

entry = Entry(root)
entry.insert(0, 'Full name')
entry.pack()
entry.bind("<FocusIn>", lambda event: entry.selection_range(0, END))

selection = StringVar()
selection.set(None)
Radiobutton(root, variable=selection, text='Mr.', value='MR').pack(anchor='w')
Radiobutton(root, variable=selection, text='Ms.', value='MS').pack(anchor='w')
Radiobutton(root, variable=selection, text='Mx.', value='MX').pack(anchor='w')

status = IntVar()
Checkbutton(root, text='Married', variable=status).packk(anchor='w')



extra = StringVar()
Listbox = Listbox(root, height=0, selectmode=MULTIPLE, listvariable = extra)
Listbox.insert(1, 'Parking')
Listbox.insert(2, 'Dinner')
Listbox.insert(3, 'Hotel')
Listbox.pack(anchor='w')


def submit():
    output = "Summary"
    output += '\nName: ' + name.get()
    output += '\nPrefix: ' + selection.get()
    output += '\nMarried: ' 
    output += 'Yes' if status.get() else 'No'
    output += '\nAmenities'
    
    for i in Listbox.curselection():
        output += ('(' + Listbox.get(i) + ')')
    
    
    messagebox.showinfo("Summary", output)
    
    print(Listbox.get(0))
    print(Listbox.get(1))
    print(Listbox.get(2))
    print(Listbox.curselection())
    


Button(root, text = 'Submit').pack()




root.mainloop()