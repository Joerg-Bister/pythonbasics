inhalt = "Vier"
ausgabe = inhalt.ljust(10)
print(ausgabe)

# Vier      

# hier werden hinter "Vier" noch 4 Leerzeichen erzeugt, diese sieht man aber nicht, da kein Text dahinter steht.

inhalt = "Vier"
ausgabe = inhalt.ljust(10)
print(ausgabe, "mehr Text")

# Vier       mehr Text

# Zwischen Vier und "mehr Text" wurden 6 Leerzeichen erzeugt, da "Vier" bereits aus 4 Zeichen besteht.

inhalt = "Vier"
ausgabe = inhalt.ljust(10, '.')
print(ausgabe, "mehr Text")

# Vier...... mehr Text

# Durch '.'  werden die Leerzeichen durch Punkte ersetz.

inhalt = "Vier"
ausgabe = inhalt.ljust(2, '.')
print(ausgabe, "mehr Text")

# Vier mehr Text

# Allerdings hat der Inhalt Vorrang vor Breitenangabe. Ist der Inhalt breiter als die mitgegebene Breite, wird der komplette Inhalt gefolgt von einem Leerzeichen ausgegeben. 

