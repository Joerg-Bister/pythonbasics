


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

# gasteintrag aus gaestebuch laden
#gasteintrag = gaestebuch[0]

##################################################################################
# hier kommt unser programm

def hauptmenue():
    print("")

# basisschleife aufbauen
while True:
    # Hauptmenue ausgeben

    # benutzereingabe abfragen
    hmeingabe = input("bitte wähle eine Option des Hauptmenüs:")

    #bedingung prüfen inclusive beingung "schleifenabbruch"