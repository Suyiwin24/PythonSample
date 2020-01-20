x = 1
while x < 7:
	print(x)
	x += 1

	x = 1
>>> while x < 10:
...     print(x)
...     x += 2
...
1
3
5
7
9

While loop require variable ready.

 x = 1
>>> while x < 7:
...     print(x)
...     if x == 5:
...             break
...     x += 1
...
1
2
3
4
5

> x = 100
>>> x = 10
>>> while x < 100:
...     print(x)
...     if x == 70:
...             break
...     x += 1

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	print(x)
for x in "pineapple":
...     print(x)
...
p
i
n
e
a
p
p
l
e
>>>


for x in fruits:
...     print(x)
...     if x == "pineapple":
...             break
...
apple
banana
orange
pineapple


for x in fruits:
...     if x == "pineapple":
...             break
...     print(x)
...
apple
banana
orange


 for x in fruits:
...     if x == "pineapple" and "coconut":
...             break
...     print(x)
...
apple
banana
orange


for x in fruits:
...     if x == "kiwi":
...             break
...     print(x)
...
apple
banana
orange
pineapple
coconut
cucumber
>>> for x in fruits:
...     print(x)
...     if x == "coconut":
...             break
...             print(x)
...
apple
banana
orange
pineapple
coconut

 for x in fruits:
...     if x == "orange":
...             continue
...     print(x)
...
apple
banana
pineapple
coconut
cucumber

 for x in range(10,100,5):
...     print(x)
...
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95



>>> NumberA = [1, 2, 3, 4, 5]
>>> NumberB = [1, 2, 3, 4, 5]
 for x in NumberA:
...     for y in NumberB:
...             print(x,y)
...
1 1
1 2
1 3
1 4
1 5
2 1
2 2
2 3
2 4
2 5
3 1
3 2
3 3
3 4
3 5
4 1
4 2
4 3
4 4
4 5
5 1
5 2
5 3
5 4
5 5
>>>


>>> NumberA = [1, 2, 3, 4, 5]
>>> NumberB = [1, 2, 3, 4, 5]
>>> NumberC = [1, 2, 3, 4, 5]

>>> for x in NumberA:
...     for y in NumberB:
...             for z in NumberC:
...                     print(x,y,z)
...
1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 2 1
1 2 2
1 2 3
1 2 4
1 2 5
1 3 1
1 3 2
1 3 3
1 3 4
1 3 5
1 4 1
1 4 2
1 4 3
1 4 4
1 4 5
1 5 1
1 5 2
1 5 3
1 5 4
1 5 5
2 1 1
2 1 2
2 1 3
2 1 4
2 1 5
2 2 1
2 2 2
2 2 3
2 2 4
2 2 5
2 3 1
2 3 2
2 3 3
2 3 4
2 3 5
2 4 1
2 4 2
2 4 3
2 4 4
2 4 5
2 5 1
2 5 2
2 5 3
2 5 4
2 5 5
3 1 1
3 1 2
3 1 3
3 1 4
3 1 5
3 2 1
3 2 2
3 2 3
3 2 4
3 2 5
3 3 1
3 3 2
3 3 3
3 3 4
3 3 5
3 4 1
3 4 2
3 4 3
3 4 4
3 4 5
3 5 1
3 5 2
3 5 3
3 5 4
3 5 5
4 1 1
4 1 2
4 1 3
4 1 4
4 1 5
4 2 1
4 2 2
4 2 3
4 2 4
4 2 5
4 3 1
4 3 2
4 3 3
4 3 4
4 3 5
4 4 1
4 4 2
4 4 3
4 4 4
4 4 5
4 5 1
4 5 2
4 5 3
4 5 4
4 5 5
5 1 1
5 1 2
5 1 3
5 1 4
5 1 5
5 2 1
5 2 2
5 2 3
5 2 4
5 2 5
5 3 1
5 3 2
5 3 3
5 3 4
5 3 5
5 4 1
5 4 2
5 4 3
5 4 4
5 4 5
5 5 1
5 5 2
5 5 3
5 5 4
5 5 5
>>>


>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
>>>