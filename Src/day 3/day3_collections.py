
#list example
numbers=[10,20,30,40]
#tuple example
coordinates=(5,10)
print(numbers)
[10, 20, 30, 40]
print(coordinates)
(5, 10)
"""""""""""""
SyntaxError: unterminated string literal (detected at line 1)
##########################################
#slicing and indexing
a[100,200,300,500]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[100,200,300,500]
NameError: name 'a' is not defined
>>> 
>>> a=[100,200,300,500]
>>> a[-3:-1]
[200, 300]
>>> a[-1:-3]
[]
>>> a[1:4]
[200, 300, 500]
>>> #skip
>>> a[1:4:2]
[200, 500]
>>> a[1:4:1]
[200, 300, 500]
>>> a=[100,200,300,400,500,600,700,800,900]
>>> a[1:4:3]
[200]
>>> a[1:9:3]
[200, 500, 800]
>>> a[-8:9:-2]
[]
>>> a[-8:-2:2]
[200, 400, 600]
>>> 
>>> ##############################################################################3
>>> #list methods and mutability
>>> 
>>> marks=[85,43,56,70,30,50]
>>> marks.append(90)
>>> print(marks)
[85, 43, 56, 70, 30, 50, 90]
>>> marks.pop()
90
>>> print(marks)
[85, 43, 56, 70, 30, 50]
>>> marks.sort()
>>> print(marks)
[30, 43, 50, 56, 70, 85]
>>> marks.reverse()
>>> print(marks)
[85, 70, 56, 50, 43, 30]
>>> marks.extend([90])
>>> print(marks)
[85, 70, 56, 50, 43, 30, 90]
>>> marks.insert(60,5)
>>> print(marks)
[85, 70, 56, 50, 43, 30, 90, 5]
>>> marks.remove(5)
>>> print(marks)
[85, 70, 56, 50, 43, 30, 90]
>>> len(marks)
7
