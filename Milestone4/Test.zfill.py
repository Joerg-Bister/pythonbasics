text = "20"
print(text.zfill(8))

#00000020

# mit zfill werden am Anfang Nullen aufgefüllt.

text = "Inhalt länger als 8 Zeichen"
print(text.zfill(8))

#Inhalt länger als 8 Zeichen

# Wenn der Inhalt länger als die angegebenen Zeichen ist, wird nur der inhalt ohne Nulle angezeigt.

text = "-123"
print(text.zfill(8))

#-0000123

# Wenn es ein führendes +/- Zeichen gibt, werden die anzuhängenden Nullen nach den +/- Zeichen aufgefüllt.


text = "-123"
print(text.rjust(8,"0"))

#0000-123

# Hier können wir aber das Zeichen angeben, mit dem der String aufgefüllt werden soll
