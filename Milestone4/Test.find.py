inhalt = "Hier kommt ein String-Inhalt"
print ( inhalt.find("e"))

#2

# Wollen wir das erste Vorkommen bestimmen, können wir die Methode find() nutzen.
# Die Zählung beginnt bei 0, daher ist die dritte Stelle dann die Nummer 2.

inhalt = "Hier kommt ein String-Inhalt"
print ( inhalt.find("e", 3))

#11

# Wollen wir das nächste Vorkommen von „e“ finden, können wir den Start mitgeben als weitere Parameter.
# das erste "e" befindet sich an 14ter Stelle, abzüglich von Startparameter 3.

inhalt = "Hier kommt ein String-Inhalt"
print ( inhalt.find("i", 5, -10))

#12
# die Ausgabe 12 kann ich nicht nachvollziehen!!

  
