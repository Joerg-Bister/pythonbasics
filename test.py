



teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "

#colums = "123456789012345678901234567890123456789012345678901234567890"
colums = 6*"1234567890"
colums2 = "000000000111111111122222222223333333333444444444455555555556"
#colums2 = 9*"0"+10*"1"+10*"2"+10*"3"+10*"4"+10*"5"+"6"



charx = "'"
countx = teststring.count(charx)

countx = 5

countxstr = str(countx); countxstr = countxstr.zfill(2)

countxstr = str(countx).zfill(2)

print(countxstr)

startx = "Sonderzeichen"
#startx = "Klammern"
startx = startx.ljust(19," ")

print(colums2)
print(colums)

footerx = "ist so oft vertreten"
delmitter = ":"

footerx = footerx.center(29, " ")


out = startx + charx + footerx + delmitter + countxstr


print(out)
print (3-4)
print (3/3)
print (0/3)
print(4**3)
print(7//2)
print(type(25))

