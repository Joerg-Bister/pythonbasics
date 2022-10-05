inhalt = "Vier"
ausgabe = inhalt.rjust(10)
print(ausgabe)

#      Vier

#Hierbei werdn 6 Leerzeichen vor dem Wort "Vier" eingefügt.

inhalt = "Vier"
ausgabe = inhalt.rjust(10)
print(ausgabe, ", weiterer Text")

#      Vier , weiterer Text

#Hier fällt das Leerzeichen vor unserem „weiteren Text“, sprich vor dem Komma auf.

inhalt = "Vier"
ausgabe = inhalt.rjust(10)
print(ausgabe + ", weiterer Text")

#Vier, weiterer Text

inhalt = "Vier"
ausgabe = inhalt.rjust(10, '.')
print(ausgabe + ", weiterer Text")

#......Vier, weiterer Text

inhalt = "Vier"
ausgabe = inhalt.rjust(2, '.')
print(ausgabe + ", weiterer Text")

#Vier, weiterer Text

