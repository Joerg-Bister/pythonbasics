teststring = "abcdefghijklm"

durchlauf = 1
abbruch = len(teststring)
while durchlauf <= abbruch :
      cnr = durchlauf - 1
      charx = teststring[cnr]
      print("hallo " + durchlauf.__str__() + " " + charx )
      durchlauf += 1

print("dies kommt nach der schleife")
