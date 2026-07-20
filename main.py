# print("konda\nthanuja")
# print(r"\tcurrent\new\folder")
# #/ is escape character 


# #write a program to find odd or even with function:
# def check(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# check(11)

# l=[1,2,3,4,5]
# l.pop()
# print(l)


# dict={
# "name":"thanuja",
# "gender":"female",
# "age":20,
# "courses":["python","java","datascience"]
# }
# dict["name"]="thanuja konda"
# dict.update({"courses":["python","java","machine learning"]})

# print(dict)
# print(dict.get("name"))
# print(dict["name"])
# print(dict.keys())
# print(dict.values())
# print(dict.items())

# def count(*args):
#     print(type(args))
# count(1,2,3,4,5)

# def dicts(**kwargs):
#     print(type(kwargs))
# dicts(name="thanuja",age=20,gender="female")

# def default(gender,age,name="thanuja"):
#     print(name,age,gender)

# #OOPS

 
# l=[1,2,3]
# s="string"
# len(l)
# len(s)

#4 pillars of OOPS
#Encapsulation 
#Abstraction
#Inheritance
#Polymorphism
#take a string as input and 
# print it back by removing the first and last character of the input string
# x="thanuja"
# x=x[1:-1]
# x=x[::-1]
# print(x)

#create an example whikle loop 
# not terminate ,and prints hi in each iteration 
# and how will you stop the program manually ?
# while True:
#     print("hi")
#     break



#take a number as input and find the sum of numbers from 1 to that number
n=int(input("enter number:"))
sum=n*(n+1)//2
print("the sum of 1 to n:",sum)
#another way 
x=int(input())
sum=0
for i in range(1,x):
    sum+=i
print(sum)
#another way 
sum=0
while 