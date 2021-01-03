import Cryptography as e
from tkinter import *
from tkinter import filedialog as f
from datetime import datetime as d
try:
    import webbrowser as wb
except:
    print('`webbrowser` - package is not installed, so one feature may not work!')
    
#The window configuration:
app = Tk()
app.geometry('700x500')
app.title('Cryptography')
app.resizable(False, False)

#The Help Prompt:
def Credits():
    c = Tk()
    c.geometry('510x320')
    c.resizable(False, False)
    c.title('Credits')
    c.config(bg = 'black')
    txt = '''This GUI App is created by:
        R. Parvat
        
    Launched in github on :
        Dec 31 2020   12:45
        
    This Program is created using:
        1. Python 3.9   -   Programming Language
        2. Python IDLE  -   Text Editor
        3. Tkinter      -   Python Module
        4. Datetime     -   Python Inbuilt Module
    '''
    l = Label(c, text = txt, fg = 'white', bg = 'black', font=(('Curls MT'),(18),('italic')), justify = LEFT)
    l.place(x = 0, y = 0)


#The text-input area:
text_input = Text(app, width = 25, height = 18, font='Courier 18')
text_input.place(x = 0, y = 50)

#The key entry:
key = Entry(app, bg = 'black', fg = 'white', font='Courier 16')
key.place(x = 90, y = 12)
key_l = Label(app, text = 'Key :', font='Arial 16')
key_l.place(x = 10, y = 10)

#the decoded code:
code = ''

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
    text_return.config(height = 20, width = 27)
    text_return.update()
    text_return.place(x = 365, y = 10)
    global code
    code = b

def decode(event = None):
    text = text_input.get('1.0', 'end-1c')
    Key = key.get()
    a = e.Cryptography(Key, text)
    b = a.decode(True)
    text_return = Text(app)
    text_return.config(fg = 'white', bg = 'black', font = 'Consolas 16')
    text_return.insert('1.0', b)
    text_return.update()
    text_return.config(state = DISABLED)
    text_return.config(height = 20, width = 27)
    text_return.update()
    text_return.place(x = 365, y = 10)
    global code 
    code = b

def Quit(event = None):
    app.destroy()

def go_to():
    try:
        wb.open_new('https://github.com/Parvat-web-dev/Simple-Cryptography/')
    except NameError:
        print('The ~webdrive~ Module was not found!')
def SaveAs(event = None):
    now = d.now()
    day = now.day
    month = now.month
    year = now.year
    time = now.time()
    total = f'y/m/d : {year}/{month}/{day}, TIME: h/m/s/ms: {time}'
    extentions = [('Text File', '*.txt'), ('Document File', '*.doc')]
    FILE = f.asksaveasfile(mode = 'w', filetypes = extentions, defaultextension = extentions)
    KEY = key.get()
    TEXT = text_input.get('1.0', 'end-1c')
    CODE = code
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

#The menu:
menu = Menu(app)

#The file menu:
file = Menu(menu, tearoff = 0)
file.add_cascade(label = 'Save As   Ctrl-s')
file.add_separator()
file.add_cascade(label = 'Exit      Ctrl-q', command = app.destroy)

#The cryptography menu:
crypto = Menu(menu, tearoff = 0)
crypto.add_cascade(label = ' Encode     Ctrl-e', command = encode)
crypto.add_cascade(label = ' Decode     Ctrl-d', command = decode)

#The help menu
HeLp = Menu(menu, tearoff = 0)
HeLp.add_cascade(label = ' Online Docs ', command = go_to)
HeLp.add_cascade(label = '   Credits   ', command = Credits)

#Adding all the menu in the main menu:
menu.add_cascade(label = ' File ', menu = file)
menu.add_cascade(label = ' Cryptography ', menu = crypto)
menu.add_cascade(label = ' HELP ', menu = HeLp)

#The shortcut keys:
app.bind_all('<Control-Key-e>', encode)
app.bind_all('<Control-Key-d>', decode)
app.bind_all('<Control-Key-q>', Quit)
app.bind_all('<Control-Key-s>', SaveAs)

#The main loop of the window:
app.config(menu = menu)
app.mainloop()
