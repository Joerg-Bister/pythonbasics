ausgabetext = "Der Preis für 2 Socken beträgt 2 DM und 2 Paar kosten 3.50 DM"
ausgabetext = ausgabetext.replace("DM", "Euro")
ausgabetext = ausgabetext.replace("2", "zwei", 2)
print("Nach dem Austauschen über replace():")
print(ausgabetext)

#Der Preis für zwei Socken beträgt zwei Euro und 2 Paar kosten 3.50 Euro

# ausgabetext.replace("DM", "Euro")= hiermit werden DM gegen Euro ausgetauscht.
# ausgabetext = ausgabetext.replace("2", "zwei", 2)= die Zahl 2 wird gegen zwei ausgetauscht und mit der letzten 2 in Klammern wird die Ausgabe hierfür festgelegt.

ausgabetext = "1 1 2 2 3 3 4 4"
ausgabetext = ausgabetext.replace("1", "eins")
ausgabetext = ausgabetext.replace("2", "zwei")
ausgabetext = ausgabetext.replace("3", "drei")
print("Nach dem Austauschen über replace():")
print(ausgabetext)

#eins eins zwei zwei drei drei 4 4
# ausgabetext = ausgabetext.replace("1", "eins")=  die Zahl 1 wird mit eins ersetzt.
# ausgabetext = ausgabetext.replace("2", "zwei")=  die Zahl 2 wird mit eins ersetzt.
# ausgabetext = ausgabetext.replace("3", "zwei")=  die Zahl 3 wird mit eins ersetzt.
# da die Zahl 4 nicht replacet wird bleibt sie als solche erhalten.

ausgabetext = "1 1 2 2 3 3 4 4"
ausgabetext = ausgabetext.replace("1", "eins").replace("2", "zwei").replace("3", "drei")
print("Nach dem Austauschen über replace():")
print(ausgabetext)

#eins eins zwei zwei drei drei 4 4

# Es wird die gleiche Ausgabe erreicht wie im vorangegangenen String, allerdings in einer Zeile eingegeben.
