


#################################################################
# basisdefinitionen

# vornamen
# nachnamen
# telefonnummer
# email
# allergie
# gender

###############################################
#
gasteintrag = {}
gaestebuch = []
gi = {}


gasteintrag['vname'] = "Ben"
gasteintrag['nname'] = "Ertel"
gasteintrag['telnr'] = "+4900000000000"
gasteintrag['mail'] = "Ertel@ben.deutschland"
gasteintrag['allergie'] = "keine"
gasteintrag['gender'] = "backfisch"

#######################################################
# Beispiele
# gast in gaestebuch schreiben
#gaestebuch[0] = gasteintrag
gaestebuch.append(gasteintrag)

# gasteintrag aus gaestebuch laden
#gasteintrag = gaestebuch[0]


##################################################################################
# hier kommt unser programm

def hauptmenue():
    print("")

def neuereintrag():
    global gi               # an dieser Stelle müssen wir die Variable, die Ausserhalb unserer Funktion liegt aus dem Globalen Namespace in die Funktion laden
    global geastebuch       # an dieser Stelle müssen wir die Variable, die Ausserhalb unserer Funktion liegt aus dem Globalen Namespace in die Funktion laden

    gi.clear()
    print("Hier wird ein Neuer Gast eingetragen")
    gi['vname'] = input("Bitte den Vornamen eingeben:")
    gi['nname'] = input("Bitte den Nachname eingeben:")
    gi['telnr'] = input("Bitte den Telefonnummer eingeben:")
    gi['mail'] = input("Bitte den Mail eingeben:")
    gi['allergie'] = input("Bitte den Allergien eingeben:")
    gi['gender'] = input("Bitte den Geschlecht eingeben:")
    gaestebuch.append(gi)

def eintragaendern():
    print()


# basisschleife aufbauen
while True:
    # Hauptmenue ausgeben

    # benutzereingabe abfragen
    hmeingabe = input("bitte wähle eine Option des Hauptmenüs:")

    #bedingung prüfen inclusive beingung "schleifenabbruch"