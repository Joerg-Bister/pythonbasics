# Hier wird der Klarname ausgegeben.

inhalt ="  Python rocks"
ausgabe = inhalt.lstrip()
print(ausgabe)

inhalt =" Python rocks "
ausgabe = inhalt.lstrip()
print(ausgabe +",daherPython lernen")

inhalt ="321 Python 3 rocks "
ausgabe = inhalt.lstrip('123')
print(ausgabe)

inhalt ="321 Python 3 rocks "
ausgabe = inhalt.lstrip('123456789')
print(ausgabe)
