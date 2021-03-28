import Cryptography as e
from tkinter import *
from tkinter import filedialog as f
from datetime import datetime as d
from kivy.core.clipboard import Clipboard
try:
    import webbrowser as wb
except:
    print('`webbrowser` - package is not installed, so one feature may not work!')

app = Tk()
app.geometry('600x500')
app.title('Cryptography')
app.minsize(350, 500)
menu = Menu(app)

key = Entry(app, font = (('Courier'), ('20'), ('italic')), justify = CENTER)
key.place(relx = 0, y = 50, relwidth=1)

label1 = Label(app, text = 'Text To Encode/Decode :', font = 'Courier 18')
label2 = Label(app, text = 'Key :', font = 'Courier 18 bold')
label1.place(x = 10, y = 90)
label2.place(x = 10, y = 10)

text_input = Text(app, fg ='white', bg = 'navyblue', font = (('Courier'), (18), ('bold')), insertbackground='white')
text_input.place(relx = 0, y = 150, relwidth=0.5, relheight=0.7)

text_return = Label(app, wraplength=323, fg = 'white', bg = 'black', font = 'Consolas 16', text='Your Decode Text Or Encoded Text Will Be Shown Here', justify=LEFT)
text_return.config(state=NORMAL)
text_return.place(relx=0.5, y = 150, relheight=0.7, relwidth=0.5)

def go_to():
    try:
        wb.open_new('https://github.com/Parvat-web-dev/Simple-Cryptography/')
    except:
        print('Webbrowser Module Not Found!')
    pass

def encode(event = None):
    text = text_input.get('1.0', 'end-1c')
    Key = key.get()
    a = e.Cryptography(Key, text)
    b = a.encode(True)
    text_return['text'] = b

def decode(event = None):
    text = text_input.get('1.0', 'end-1c')
    Key = key.get()
    a = e.Cryptography(Key, text)
    b = a.decode(True)
    text_return['text'] = b
    

def NewWin(event = None):
    return __import__("Cryptography App")

def SaveAs(event = None):
    now = d.now()
    day = now.day
    month = now.month
    year = now.year
    time = now.time()
    total = f'''y/m/d : {year}/{month}/{day}, TIME: h/m/s/ms: {time}
'''
    extentions = [('Text File', '*.txt'), ('Document File', '*.doc')]
    FILE = f.asksaveasfile(mode = 'w', filetypes = extentions, defaultextension = extentions)
    KEY = key.get()
    TEXT = text_input.get('1.0', 'end-1c')
    CODE = text_return['text']
    FILE.write(total)
    FILE.write(f'Key : {KEY}')
    FILE.write('''
''')
    FILE.write(f'Text : {TEXT}')
    FILE.write('''
-------------------------------------------
''')
    FILE.write(f'Result : {CODE}')
    FILE.write('''
''')

def Copy(event=None):
    data = text_return['text']
    Clipboard.copy(data)

def Paste(event=None):
    text_input.delete('1.0', 'end')
    text_input.insert('end', Clipboard.paste())

file = Menu(menu, tearoff = 0)
file.add_cascade(label = 'New Window', command = NewWin)
file.add_cascade(label = 'Save As', command = SaveAs)
file.add_separator()
file.add_cascade(label = 'Exit', command = app.destroy)

crypto = Menu(menu, tearoff = 0)
crypto.add_cascade(label = 'Encode    Ctrl+e', command = encode)
crypto.add_cascade(label = 'Decode    Ctrl+d', command = decode)
crypto.add_cascade(label = 'Copy Encoded', command = Copy)
crypto.add_cascade(label = 'Paste Text', command = Paste)

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
App Link: https://drive.google.com/file/d/1xJeJMSSMleukbhbclPpY-_3OQtOPTUJx/view?usp=sharing
Or The Website: https://cyber-viable.000webhostapp.com/
''', font = (('Curlz MT'),(24),('italic')), fg = 'white', bg = 'black')
    label.place(x = 0, y = 0, relwidth=1, relheight=1)

Help = Menu(menu, tearoff = 0)
Help.add_cascade(label = 'Online Docs')
Help.add_cascade(label = '  Credits  ', command = Credits)

menu.add_cascade(label = 'File', menu = file)
menu.add_cascade(label = 'Cryptography', menu = crypto)
menu.add_cascade(label = 'Help', menu = Help)

#The shortcutkeys
app.bind_all('<Control-Key-e>', encode)
app.bind_all('<Control-Key-d>', decode)
app.bind_all('<Control-Key-s>', SaveAs)
app.bind_all('<Control-Key-n>', NewWin)
def EXIT(event=None):
    app.destroy()
    quit()
app.bind_all('<Control-Key-q>', EXIT)

#The shortcut keys
text_input.bind_all('<Control-Key-e>', encode)
text_input.bind_all('<Control-Key-d>', decode)
text_input.bind_all('<Control-Key-s>', SaveAs)
text_input.bind_all('<Control-Key-n>', NewWin)

#The encode and decode buttons
btn1 = Button(app, text = ' Encode ', command = encode, font = (('Consolas'),(18),('bold')), fg = 'white', bg = 'green')
btn2 = Button(app, text = ' Decode ', command = decode, font = (('Consolas'),(18),('bold')), fg = 'darkgreen', bg = 'white')
btn1.place(relx=0, y = 85, relwidth=0.25)
btn2.place(relx=0.25, y = 85, relwidth=0.25)

#the copy and paste buttons
btn3 = Button(app, text = ' Copy ', command = Copy, font = (('Consolas'),(18),('bold')), fg = 'white', bg = 'green')
btn4 = Button(app, text = ' Paste ', command = Paste, font = (('Consolas'),(18),('bold')), fg = 'darkgreen', bg = 'white')
btn3.place(relx=0.5, y = 85, relwidth=0.25)
btn4.place(relx=0.75, y = 85, relwidth=0.25)


app.config(menu = menu)
app.mainloop()
