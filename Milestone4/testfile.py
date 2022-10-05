colums = 6*"1234567890"
colums2 = "000000000111111111122222222223333333333444444444455555555556"
teststring = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
sonderzeichen = "%$§\"\`\'#/:;-"

charx = sonderzeichen[0]
startX = "Sonderzeichen"
footerx = "ist so oft vertreten"
delmitter = ":"

countx = teststring.count(charx)
countxstr = str(countx)
startx = startx.ljust(19," ")
footerx = footerx.rjust(29, " ")
countxstr = countxstr.zfill(2).rjust(5, " ")

out= startx + charx + footerx + delmitter + countxstr
print(colums2)
print(colums)
print(out)




