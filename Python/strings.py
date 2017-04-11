C:\Users\Mal>python
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.

Find/Replace

>>> string = "It's thanksgiving day. It's my birthday, too!"
>>> string.find("day")
18
>>> string.replace("day", "month")
"It's thanksgiving month. It's my birthmonth, too!"
>>>


Min/Max

>>> x = [2,54,-2,7,12,98]
>>> min(x)
-2
>>> max(x)
98
>>>


First/Last

>>> x = ["hello",2,54,-2,7,12,98,"world"]
>>> print(x[0])
hello
>>> print(x[len(x)-1])
world
>>> first = x[0]
>>> last = x[len(x)-1]
>>> newList = first + last
>>> print(newList)
helloworld
>>> newList = [first + " " + last]
>>> print(newList)
['hello world']
>>>


New List

>>> x = [19,2,54,-2,7,12,98,32,10,-3,6]
>>> x.sort()
>>> print x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> len(x) / 2
5
>>> 5
5
>>> x[len(x)/2]
10
>>> 12
12
>>> x[:len(x)/2]
[-3, -2, 2, 6, 7]
>>> [-3, -2, 2, 6, 7]
[-3, -2, 2, 6, 7]
>>> x[len(x)/2:]
[10, 12, 19, 32, 54, 98]
>>> [10, 12, 19, 32, 54, 98]
[10, 12, 19, 32, 54, 98]
>>> firstHalf = x[:len(x)/2]
>>> secondHalf = x[len(x)/2:]
>>> newStr = []
>>> newStr.append(firstHalf)
>>> newStr.extend(secondHalf)
>>> print newStr
[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
>>>