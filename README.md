<h1 align = 'center'>Simple-Cryptography</h1>
<h6 align = 'right'>A simple Cryptography module that encrypts and decrypts some text with a key.</h6>
<hr>

### A simple Python module that when used asks you to input some text that you need to _ENCRYPT_ and a _key_ that is used to encrypt the text with the unique combination of the given _key_ and the text this is to be _encrypted_. Only the person who knows the _key_ can crack the encoded text! Without that _key_, even I(_the developer of this program_) cannot **crack the** _encrypted text_!
<br>
<hr>

### Requirements:

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

#Declaring a variable for the encoded text:
a = c.Cryptography('key', 'the text to be encoded')

#Calling the encode function:
a.encode(True)      #If the parameter is True, it will print the encoded text
```

### If we run the file in the IDLE shell:

```shell
'32101 25279 31722 56736 29827 31722 33617 29827 62042 32101 27932 62042 25279 24142 62042 26416 27553 30964 30206 23763 31722 26037 '
```

<p>You can see that it prints some wierd numbers which are the encoded text, encoded using your key!</p>
<h3>Lets decoded some text:</h3>
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

<h6>For any errors reply at <a href = 'mailto:replyerrors.parvat@gmail.com'>replyerrors.parvat@gmail.com</a></h6>
<ul>Created By:
  <li>R. Parvat
</ul>
