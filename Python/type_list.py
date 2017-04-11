myList = ['magical unicorns', 19, 'hello', 98.98, 'world']
newStr = ""
Str = 0
Int = 0
Mixed = 0

printMixed = "The array you entered is of mixed type"
printString = "The array you entered is of string type"
printInt = "The array you entered is of integer type"

printSum = "Sum:",sum(myList)
printnewStr = "String:",newStr

for stuff in myList:
    if type(stuff)==int:
        Int = 1
    elif type(stuff)==str:
        newStr = "" + (stuff)
        Str = 1
    if type(myList)==int and type(myList)==str:
        Mixed = 1

for stuff in myList:
    if Mixed > 0:
        print printMixed
        print printnewStr
        print printSum
    elif Int > 0:
        print printInt
        print printSum
    elif Str > 0:
        print printString
        printnewStr
        


