inhalt = "mittig"
print( inhalt.center(12) )

#   mittig

# Innerhalb der angegebenen Zeichen (12) wird der Inhalt (mittig) mittig angegeben.   

inhalt = "mittig"
print( inhalt.center(12,"^") )

# ^^^mittig^^^

# Hier werden die Leerzeichen durch ^ ersetzt.

inhalt = "mittig"
print( inhalt.center(11,"^"))

# ^^^mittig^^

# Bei ungerader Zeichenanzahl, werden die Füllzeichen links mehr ausgegeben.

inhalt = "Mitte"
print( inhalt.center(8,"^") )

# ^Mitte^^

# Bei gerader Zeichenanzahl, werden die Füllzeichen rechts mehr ausgegeben.

inhalt = "Mitte"
print(inhalt.center(2,"^"))

# Mitte

# Unser Beispielwort „Mitte“ benötigt mindestens 5 Zeichen, bekommt aber im Beispiel nur 2 zur Verfügunggestellt. Macht nichts, da wir die Ausgabe des kompletten Beispielwortes erhalten, was allerdings nichtzentriert werden kann.


