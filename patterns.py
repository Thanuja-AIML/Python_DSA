# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# right angled triangle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# inverted right angled triangle
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")  
#     print()
    
# diamond pattern
# first how many rows 
# second how many spaces 
# third how many stars
# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ") 
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end=" ") 
#     for j in range(2*i+1)     :
#         print("*",end=" ")
#     print()


# # Armstrong Number
# num=int(input("enter a number:"))
# t1=num
# t2=num
# c=0
# while t1>0:
#     c+=1
#     t1=t1//10
# arm=0
# while t2>0:
#     d=t2%10
#     arm=arm+d**c 
#     t2=t2//10
# if num==arm:
#     print("Armstrong")
# else:
#     print("Not Armstrong") 
    
# another way 
# num=int(input("enter a number:"))
# sum=0
# length=len(str(num))
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
# if sum==num:
#     print(num,"is an armstrong number")
# else:
#     print(num,"is not an armstrong number")



# hollow square pattern 
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# pascals patterns
n=5
for i in range(n):
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*
    print()
 
