import tkinter

window = tkinter.Tk()
window.title("WHEN THE BUTTON IS CLICKED, THE LABEL SHOWS YOUR INPUT")
window.minsize(width=700, height=400)

label = tkinter.Label(text="PRESS THE BUTTON TO CONFIGURE THIS MSG")
label.pack()


def click():
    a = entry.get()
    label.config(text=a)


button = tkinter.Button(text="Press Me", command=click)
button.pack()

entry = tkinter.Entry()
entry.pack()

window.mainloop()
