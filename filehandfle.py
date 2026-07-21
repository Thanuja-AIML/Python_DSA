# with open("file1.txt","w") as file:
#     file.write("hello world")
# with open("file1.txt","r") as file:
#     print(file.read())
# with open("file1.txt","a") as file:
#     file.write(" python programming")


#task1
#keep asking valid integet number
#if not valid integer number,print error
# while True:
#     try:
#         a=int(input("enter a number:"))
#         print(a)
#         break
#     except ValueError as e:
#         print(e)
        
#TASK2
##handle index error while accessing list if it is out of range handle it 

L=[1,2,3,4,5,6,7,8,9,10]
try:
    print(L[10])
except IndexError as e:
    print(e)

    
        