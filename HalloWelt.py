Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======== RESTART: C:/Users/JB000/OneDrive/Dokumente/_Workspace/Hallo.py ========
Hallo, Welt
Hallo, Welt
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Hallo, Welt
NameError: name 'Hallo' is not defined

===== RESTART: C:/Users/JB000/OneDrive/Dokumente/_Workspace/Hallo.py ====
Hallo, Welt
nachricht
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    nachricht
NameError: name 'nachricht' is not defined
>>> help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
===== RESTART: C:/Users/JB000/OneDrive/Dokumente/_Workspace/Hallo.py ====
Hallo, Welt
>>> 
==== RESTART: C:/Users/JB000/Documents/_Workspace/HalloWelt/Hallo.py ====
Hallo, Welt
>>> python -i Hallo.py
SyntaxError: invalid syntax
>>> python -i Hallo.py
SyntaxError: invalid syntax
>>> 
==== RESTART: C:/Users/JB000/Documents/_Workspace/HalloWelt/Hallo.py ====
Hallo, Welt
>>> !
SyntaxError: invalid syntax
>>> nachricht
'alles in Ordnung'
