vornachname = "Rolf von und zu Maier-Müller"
umgewandelt = vornachname.capitalize()
print(umgewandelt)

#Rolf von und zu maier-müller

# bei .capitalize wird nur der erste Buchstabe in Großschreibung und der Rest in Kleinbuchstaben dargestellt.

zeichenkette = "hIeR kOmMt TeXT"
print(zeichenkette.capitalize())

#Hier kommt text

# Auch hier wird lediglich der erste Buchstabe groß geschrieben.

zeichenkette = "123 Text"
print(zeichenkette.capitalize())

#123 text

# Bei Zahlen oder Vorzeichen verändert sich die AUsgabe nicht, da nur Buchstaben behandelt werden können.

zeichenkette = "+123 Text"
print(zeichenkette.capitalize())

#+123 text

# Bei Zahlen oder Vorzeichen verändert sich die AUsgabe nicht, da nur Buchstaben behandelt werden können.

zeichenkette = "ß Text"
print(zeichenkette.capitalize())

#Ss text

# Das ß am Anfang einer Zeichenkette wird als Ss ausgegeben.

zeichenkette = "äöü Text"
print(zeichenkette.capitalize())

#Äöü text





