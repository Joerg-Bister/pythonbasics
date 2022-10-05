inhalt =" Python 3 rocks "
ausgabe = inhalt.rstrip()
print(ausgabe + ",daher Python lernen")

# Python 3 rocks,daher Python lernen

print ("\n\n\n")

inhalt =" Python 3 rocks 1233 4444"
ausgabe = inhalt.rstrip('4')
print(ausgabe + ",daher Python lernen")

# Python 3 rocks 1233 ,daher Python lernen
# Mit ausgabe = inhalt.rstrip('4') werden alle 4ren die rechts entfernt werden sollen beseitigt.

print ("\n\n\n")

inhalt =" Python 3 rocks 1233 4444"
ausgabe = inhalt.rstrip('1234 ?XYZ')
print(ausgabe + ",daher Python lernen")

# 

print ("\n\n\n")

inhalt =" Python 3 rocks \n \r\n"
ausgabe = inhalt.rstrip('')
print(ausgabe + ",damit sichtbar wird, was gelöscht wurde")

print ("\n\n\n")

inhalt =" Python 3 rocks \n \r\n"
ausgabe = inhalt.rstrip('\n')
print(ausgabe + ",damit sichtbar wird, was gelöscht wurde")

print ("\n\n\n")

inhalt =" Python 3 rocks \n \r\n"
ausgabe = inhalt.rstrip('\n \r')
print(ausgabe + ",damit sichtbar wird, was gelöscht wurde")
