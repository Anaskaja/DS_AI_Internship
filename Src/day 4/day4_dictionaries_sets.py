
a ={"key": value}

NameError: name 'value' is not defined. Did you mean: 'False'?
a ={"key":"value"}
print(a)
{'key': 'value'}
student = {"name":"amit",
           "age":21,
           "course":"Engineering"}
print(student["name"])
amit
student["age"]=22
student["city"]="Delhi"
print(student)
{'name': 'amit', 'age': 22, 'course': 'Engineering', 'city': 'Delhi'}
marks ={"maths":80,"science":75,"english":85]
 '{'
marks ={"maths":80,"science":75,"english":85}
print(marks.get("math"))
None
print(marks.get("maths"))
80
print(marks.get("history",0))
0
for subject,score in marks.items():
    print(subject,score)

    
print(marks)

marks.update({"maths":100})
print(subject,score in marks.items():
      

print(subject,score,marks)
      
english 85 {'maths': 100, 'science': 75, 'english': 85}
######################################################
      
purchases={
    "Alice":40,
    "Bob":60,
    "john":52}
      
for name,amount in purchases.items():
      print(f"{name} spent ${amount}")

      
Alice spent $40
Bob spent $60
john spent $52
n = int(input("Enter number of Customers:"))
      
Enter number of Customers:3
user_purchases[name]= amount
      
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    user_purchases[name]= amount
NameError: name 'user_purchases' is not defined
user_purchases={}
      
for i in range(n):
      name =input("Enter customer name:"
      amount=int(input("Enter purchase amount for {name}:"))
                  
SyntaxError: '(' was never closed

user_purchases={}
      
for i in range(n):
      name =input("Enter customer name:")
      amount=int(input("Enter purchase amount for {name}:"))
                  
SyntaxError: multiple statements found while compiling a single statement
for i in range (n):
                  name= input("Enter customer  name:")
                  amount=int(input("Enter purchase amount for {name}:"))
                  user_purchases[name] = amount
                  print("Customer Purchase Data:",user_purchases)

...                   
Enter customer  name:sum
Enter purchase amount for {name}:99999
Customer Purchase Data: {'sum': 99999}
Enter customer  name:ji
Enter purchase amount for {name}:88
Customer Purchase Data: {'sum': 99999, 'ji': 88}
Enter customer  name:hoi
Enter purchase amount for {name}:0909
Customer Purchase Data: {'sum': 99999, 'ji': 88, 'hoi': 909}
>>> purchases.update({"David": 500})
...                   
>>> print(purchases)
...                   
{'Alice': 40, 'Bob': 60, 'john': 52, 'David': 500}
>>> purchases.update({"charlie": 656})
...                   
>>> print("all customers present:", purchases)
...                   
all customers present: {'Alice': 40, 'Bob': 60, 'john': 52, 'David': 500, 'charlie': 656}
>>> purchases.pop("and")
...                   
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    purchases.pop("and")
KeyError: 'and'
>>> purchase.pop("charlie")
...                   
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    purchase.pop("charlie")
NameError: name 'purchase' is not defined. Did you mean: 'purchases'?
>>> purchases.pop("Charlie")
...                   
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    purchases.pop("Charlie")
KeyError: 'Charlie'
>>> purchases.pop("charlie")
                  
656
print(purchases)
                  
{'Alice': 40, 'Bob': 60, 'john': 52, 'David': 500}
