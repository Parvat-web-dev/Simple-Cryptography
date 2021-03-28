<h1 align = 'center'>Simple-Cryptography</h1>
<h6 align = 'right'>A simple Cryptography module that encrypts and decrypts some text with a key.</h6>
<a href='https://sprin-g-reen.github.io/simple%20cryptography/'><img src="https://img.shields.io/badge/Website-SPRINGREEN-blue"></a>
<hr>

## Download the Cryptography App: Link: [Google Drive](https://drive.google.com/file/d/1xJeJMSSMleukbhbclPpY-_3OQtOPTUJx/view?usp=sharing)

<hr>
<a href='#'><img src='https://img.shields.io/badge/Current%20Status-Under--Long%20Time--Development-brightgreen'></a>
<a href='https://telegram.me/Parvat_R'><img src='https://img.shields.io/badge/Telegram%20Us-@Parvat_R-brightgreen'></a>
<a href='mailto:relpyerrors.parvat@gmail.com'><img src='https://img.shields.io/badge/Mail%20Please%20To-replyerrors.parvat@gmail.com-brightgreen'></a>

### A simple Python module that when used, asks you to input some text that you need to _ENCRYPT_ and a _key_ that is used to encrypt the text with an unique combination of the given _key_ and the text that is to be _encrypted_. Only the person who knows the _key_ can crack the encoded text! Without that _key_, even I(_the developer of this program_) cannot **crack the** _encrypted text_!
<br>
<hr>

# The Cryptography App(_.exe_):
### A simple app made with Tkinter and converted into _.exe_ file with the help of [pyinstaller](https://pypi.org/project/pyinstaller/). The app has the following features:

<ul>
  <li>Encodes and Decodes the text given in the _blue_ area.
    <ul>Shotrcut Keys:
      <li>Ctrl+e</li>
      <li>Ctrl+d</li>
    </ul>
  </li>
  <li>Can save the encoded text
    <ul>Shortcut Keys
      <li>Ctrl+s</li>
    </ul>
  </li>
  <li>Can copy the encoded or decoded text in the black area.
    <ul>Usage:
      <li>The 'Paste' and 'Copy' buttons are in the 'Cryptography' menu at the top.</li>
    </ul>
  </li>
</ul>

<hr>

### Requirements for the module:

<ul>
<li>Python 3.9 or above
<li>Tkinter(module)
<li>webbrowser(module)
</ul>
<h2 align = 'center'>How To Use:</h2>

Read the below code to understand how to use the _module_:

<br>

```python
#Importing the module:
import Cryptography as c

## Declaring a variable for the encoded text:
a = c.Cryptography('key', 'the text to be encoded')

## Calling the encode function:
a.encode(True)      #If the parameter is True, it will print the encoded text
```

### If we run the file in the IDLE shell:

```shell
'32101 25279 31722 56736 29827 31722 33617 29827 62042 32101 27932 62042 25279 24142 62042 26416 27553 30964 30206 23763 31722 26037 '
```

<p>You can see that it prints some wierd numbers which are the encoded text, encoded using your key!</p>
<h3>Lets decode some text:</h3>
<p>The text to be decoded is :</p>
<p>'40439 24142 30964 51430 54462 37407 33238 30206 53704 30206 22626 36270 29448 54462 23005 29069 23384 33617 29069 24142 23005 59389 29827 30964 29448 54462 29069 29069 31343 35512 47640 '</p>
<p>The person who had encoded this text had given me the "key" which is : 'secret'</p>

In the File:
```python
#Importing the module:
import Cryptography as c

#The encoded text:
encoded_text = '40439 24142 30964 51430 54462 37407 33238 30206 53704 30206 22626 36270 29448 54462 23384 32480 23384 33617 29069 24142 23005 59389 29827 30964 29448 54462 29069 29069 31343 35512 47640 '

#Declaring a variable for the encoded text:
a = c.Cryptography('secret', encoded_text)

#Calling the encode function:
a.decode(True)      #If the parameter is True, it will print the encoded text
```

### It will return in the IDLE shell:

```shell
'Hey, you have decoded the text!'
```

>Note: The key can be anything when you are encoding the text. But the same key should be used to decode the text, which was used to encode that text!


#### Thats all, you know all about this module!
### Reporting 
<a href="https://t.me/Venilabots"><img src="https://img.shields.io/badge/Message%20Now-Venila%20Bots-blue"></a>
<a href="https://www.paypal.me/rohith204"><img src="https://img.shields.io/badge/Donate%20-Paypal-blue"></a>
<a href="mailto:replyerrors.parvat@gmail.com "><img src="https://img.shields.io/badge/Gmail-Compose%20Now-red"></a>
<h6>For any errors reply at <a href = 'mailto:replyerrors.parvat@gmail.com'>replyerrors.parvat@gmail.com</a></h6>

<ul>Created By:
  <li>R. Parvat</li>
  <li>S.V. Rohithaditya</li>
</ul>

## © [SPRINGREEN](https://t.me/venilabots) 

###### Please dont misuse it!
