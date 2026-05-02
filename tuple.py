Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple
>>> a=(5,4,7,2,1,9,8]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> a=(5,4,7,2,1,9,8)
>>> print(a)
(5, 4, 7, 2, 1, 9, 8)
>>> type(a)
<class 'tuple'>
>>> b=(3,4.7,"python",4+9j,True,False)
>>> type(b)
<class 'tuple'>
>>> len(a)
7
>>> a.index(2)
3
>>> a.count(7)
1
>>> 
>>> 
>>> #task
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> # output [7,6,4,3,0,9,8,5,2,1]
>>> a.pop(0)
9
>>> a.pop(8)
0
>>> a.append()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.append()
TypeError: list.append() takes exactly one argument (0 given)
>>> a.sort()
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a.insert("7",0)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.insert("7",0)
TypeError: 'str' object cannot be interpreted as an integer
>>> a.insert(0,7)
>>> a
[7, 1, 2, 3, 4, 5, 6, 7, 8]
>>> a.pop(6)
6
>>> a=[9,1,5,2,8,4,6,3,7,0]
a.pop(0,1)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.pop(0,1)
TypeError: pop expected at most 1 argument, got 2
a.pop(0)
9
a.pop(1)
5
a.pop(2)
8
a.pop(3)
6
a.pop(4)
7
print(a)
[1, 2, 4, 3, 0]
a.append([7,6,4,3,0])
a
[1, 2, 4, 3, 0, [7, 6, 4, 3, 0]]
a=[9,1,5,2,8,4,6,3,7,0]
a=[9,1,5,2,8,4,6,3,7,0]

#answer
a=[9,1,5,2,8,4,6,3,7,0]
a1=a[:5]
a1
[9, 1, 5, 2, 8]
a2=a[5:]
a2
[4, 6, 3, 7, 0]
a1.sort()
a1
[1, 2, 5, 8, 9]
a2.sort()
a2
[0, 3, 4, 6, 7]
a1.reverse()
a1
[9, 8, 5, 2, 1]
a2.reverse()
a2
[7, 6, 4, 3, 0]
b=a2+a1
b
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
