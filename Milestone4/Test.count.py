inhalt = "Hier kommt ein String-Inhalt"
print ( inhalt.count("i") )

#3

# "Hier kommt ein String-Inhalt" = in diesem String befinden sich 3 kleine "i" welche mit "print ( inhalt.count("i") )" ausgegeben werden.

inhalt = "Hier kommt ein String-Inhalt"
print ( inhalt.count("in") )

#2

# Das Wort „in“ kommt 2-mal vor in unserem String.

inhalt = "Hier kommt ein String-Inhalt"
kleinbuchstaben = inhalt.lower()
print ( kleinbuchstaben )
print ( kleinbuchstaben.count("in") )

#3

# durch den String-Methode .lower wurden alle Buchstaben in Kleinbuchstabenumgesetz und somit auch "in" in dem Wort inhalt erfasst.

inhalt = "Hier kommt ein String-Inhalt"
print ( inhalt.count("in", 0, 15) )

#1

# Wollen wir nur innerhalb der ersten 15 Zeichen den String überprüfen lassen, können wir dies über die optionalen Parameter für den Bereich (also Anfangspunkt und Endpunkt) erreichen.
# Es wird dann nur der Teil des Strings mit dem Inhalt „Hier kommt ein“ ausgewertet und dort wird dann einmal der gesuchte Teilstring „in“ gefunden im letzten Wort „ein“.
