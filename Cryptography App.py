import Cryptography as e
from tkinter import *
from tkinter import filedialog as fd
try:
    import webbrowser as wb
except:
    print('`webbrowser` - package is not installed, so one feature may not work!')

app = Tk()
app.geometry('700x500')
app.title('Cryptography')
app_width = app.winfo_screenwidth()
app_height = app.winfo_screenheight()
app.geometry(str(int(app_width))+'x'+ str(int(app_height)))
menu = Menu(app)

key = Entry(app, font = (('Courier'), ('20'), ('italic')), justify = CENTER)
key.place(x = 10, y = 50)

label1 = Label(app, text = 'Text To Encode/Decode :', font = 'Courier 18')
label2 = Label(app, text = 'Key :', font = 'Courier 18 bold')
label1.place(x = 10, y = 90)
label2.place(x = 10, y = 10)
text_input = Text(app, width = 50, height = 20, fg ='white', bg = 'navyblue', font = (('Courier'), (18), ('bold')))
text_input.place(x = 0, y = 150)

def go_to():
    wb.open_new('https://github.com/Parvat-web-dev/Simple-Cryptography/')
    pass

def encode(event = None):
    text = text_input.get('1.0', 'end-1c')
    Key = key.get()
    a = e.Cryptography(Key, text)
    b = a.encode(True)
    text_return = Text(app)
    text_return.config(fg = 'white', bg = 'black', font = 'Consolas 16')
    text_return.insert('1.0', b)
    text_return.update()
    text_return.config(state = DISABLED)
    text_return.config(height = 22, width = 52)
    text_return.update()
    text_return.place(x = 704, y = 150)

def decode(event = None):
    text = text_input.get('1.0', 'end-1c')
    Key = key.get()
    a = e.Cryptography(Key, text)
    b = a.decode(True)
    text_return = Text(app)
    text_return.config(fg = 'white', bg = 'black')
    text_return.insert('1.0', b)
    text_return.update()
    text_return.config(state = DISABLED)
    text_return.config(height = 33, width =78)
    text_return.update()
    text_return.place(x = 704, y = 150)

file = Menu(menu, tearoff = 0)
file.add_separator()
file.add_cascade(label = 'Exit', command = app.destroy)

crypto = Menu(menu, tearoff = 0)
crypto.add_cascade(label = 'Encode    Ctrl+e', command = encode)
crypto.add_cascade(label = 'Decode    Ctrl+d', command = decode)

def Credits():
    cre = Tk()
    cre.config(bg = 'black')
    cre.geometry('570x400')
    cre.title('Credits')
    cre.resizable(False, False)
    label = Label(cre, text = '''This GUI App is created by:
        R. Parvat -
Launched in github on :
        Dec 31 2020   12:45
This Program is created using:
    1. Python 3.9   - Programming Language
    2. Python IDLE      -      Text Editor
    3. Tkinter       -       Python Module
''', font = (('Curlz MT'),(24),('italic')), fg = 'white', bg = 'black')
    label.place(x = 0, y = 0)

Help = Menu(menu, tearoff = 0)
Help.add_cascade(label = 'Online Docs')
Help.add_cascade(label = '  Credits  ', command = Credits)

menu.add_cascade(label = 'File', menu = file)
menu.add_cascade(label = 'Cryptography', menu = crypto)
menu.add_cascade(label = 'Help', menu = Help)

text_input.bind_all('<Control-Key-e>', encode)
text_input.bind_all('<Control-Key-d>', decode)

btn1 = Button(app, text = ' Encode ', command = encode, font = (('Consolas'),(18),('bold')), fg = 'white', bg = 'green')
btn2 = Button(app, text = ' Decode ', command = decode, font = (('Consolas'),(18),('bold')), fg = 'darkgreen', bg = 'white')
btn1.place(x = 450, y = 50)
btn2.place(x = 600, y = 50)


app.config(menu = menu)
app.mainloop()
