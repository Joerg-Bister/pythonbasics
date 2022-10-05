teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
# teststring = ' <html> ist eine tolle Sprache</html> '
# teststring = "Hacker schleusen auch gerne Code ein! test()"
# teststring = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
# teststring = "Oder am Ende von Eingaben "
# teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n"""
# teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print('wahr')\nelse:\n    print('falsch')\n"""
# teststring = "<dieser String ist nun sanitized>"


sani1 = teststring.strip ('')
print ("Bereiniger Strings:\n' + sanil")
