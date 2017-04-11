mylist = [45, 100, 455, 0, -23, "Rubber baby buggy bumpers", "Experience is simply the name we give our mistakes", "Tell me and I forget. Teach me and I remember. Involve me and I learn.", "", [1,7,4,21], [3,5,7,34,3,2,113,65,8,89], [4,34,22,68,9,13,3,5,7,9,2,12,45,923], [], ['name','address','phone number','social security number']]

for n in mylist:
    if type(n)==int:
        if n>=100:
            print "That's a big number!"
        elif n<=100:
            print "That's a small number"
    if type(n)==str:
        if len(n)>=50:
            print "Long sentence."
        elif len(n)<=50:
            print "Short sentence."
    if type(n) is list:
        if len(n)>=10:
            print "Big list!"
        if len(n)<=10:
            print "Short list."

