>>> x = [19,2,54,-2,7,12,98,32,10,-3,6]

>>> len(x) / 2
5
>>> x[len(x)/2]
12
>>> x.sort()
>>> x[:len(x)/2]
[-3, -2, 2, 6, 7]
>>> x[len(x)/2:]
[10, 12, 19, 32, 54, 98]
>>> firstHalf = x[:len(x)/2]
>>> secondHalf = x[len(x)/2:]
newStr = []
firstHalf = newStr
newStr.extend(secondHalf)
print newStr
