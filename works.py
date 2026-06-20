# a = input("Enter a number: ")
# b = input("Enter second number: ")
# print(type(a))

# n=int(a)
# m=int(b)

# sum=n+m
# diff=n-m
# mul=n*m
# div=n/m
# f=n//m

# print(sum)

# del n
# print(n)

# a=5
# b=12
# print(a,b)
# a,b=b,a
# print(a,b)


# x=int(input("Enter the Number: "))
# for i in range(1,x+1):
#     for j in range(x-1):
#         print(" ",end="")
#         for k in range(i+1):
#            print("*",end=" ")
#     print( )
# x=int(input("Enter Number of Rows: "))
# for i in range(1,x+1):
#     for j in range(x-1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#             print("*",end="   ")
#     print()
# y=int(input("Enter Number of Rows: "))
# rowy
# for i in range(y+1):
#     print(" "*(row-1)+"* " *i)

# x=int(input("Enter Number of Rows: "))
# for i in range(1,x+1):
#     for j in range(x-i):
#         print("  ",end=" ")
#     for k in range(1,i+1):
#             print(k,end="     ")
#     print()

# x=[1,2,3]
# for i in x:
#     print(i)

# x=int(input("Enter a nuber: "))
# y=1
# while y<11:
#     if y==5:
#        y=y+1
#        continue
#     else:
#         print(f"{y}x{x}={y*x}")
#     y=y+1

# x=int(input("Enter the Number: "))

# if x%2==0:
#     print(f"{x} is Multiple of 2")
# elif x%3==0:
#     print(f"{x} is a Multiple of three")
# elif x%2!=0:
#     print(f"{x} is NOT a Multiple of 2")
# else:
#     print("Not Multiple")

# x=int(input("Enter the Number: "))
# if x>0:
#     if x==0:
#         print("Zero")
#     else:

#         print(f"{x} is Positive")
# else:
#     print(f"{x} is Negative")

# x=input("Enter a string: ")
# count=0
# for i in x:
 
#  print(x[ : :-1])

# x=input("Enter: ")
# rev=""
# for i in x:
#     rev=i+rev
# print(rev)

# x=input("Enter the String 1: ")
# y=input("Enter the String 2: ")
# print(x+y)
# print(len(x+y))
# print(x in y)
# print(x.upper())
# print(y.lower())
# print(x.title())
# print(x.capitalize())
# print(x.swapcase())
# print(x.find("r"))
# print(x.find("H"))
# print(x.count("e"))
# print(x.startswith("sr"))
# print(x.endswith("e"))
# print(x.replace("e","i"))
# print(x.strip())
# print(x.split(","))

# x=[1,2,3,4,5,6]
# print(x[2])
# print(x[0:2])
# print(len(x))
# x.append([7,8,9])
# print(x)

#REVERSED.
# x=int(input("Enter the numbers to be Reversed: "))
# temp=x
# rev=0

# while temp>0:
#     dig=temp%10
#     rev=(rev*10)+dig
#     temp=temp//10
# print(f"Reversed Number is {rev}") 

# x.remove(2)
# print(x)
# print(x.pop())
# print(x.pop(3))
# del x[3]
# print(x)
# x.clear()
# print(x)
# print(x)
# x.count(2)
# 3 in x

# l=[]
# n=int(input("Enter the size of list: "))

# for i in range(n):
#     x=int(input("Enter the value:"))
#     l.append(x)
# print(l)

# # for i in range(n):
# #     for j in range(n-1):
# #         if l[j]>l[j+1]:
# #             temp=l[j]
# #             l[j]=l[j+1]
# #             l[j+1]=temp
# # print(l)

# l.sort()
# print(l)

# l.sort(reverse=True)
# print(l)

# sorted(l)
# print(l)

# x=l.copy()
# print(x)
# y=input("Enter a string: ")
# y=list(y)
# print(y)
# print(y*2)

# a=input("Enter a String: ")
# v=0
# c=0
# vowels=["A","E","I","O","U","a","e","i","o","u"]

# for i in a:
#     if i.isalpha()==True:
#         if i in vowels:
#             v+=1
#         else:
#             c+=1

# print(f"The Number of Vowels is {v} and Number of Consonants is {c}")
# print(ord('a'))
# print(chr(65))

# x=input("Enter input String: ")
# b=None

# for i in x:
#     if i =='z':
#         nxt='a'
#     elif i == 'Z':
#         nxt='A'
#     else:
#         nxt=chr(ord(i)+1)
    
#     print(nxt,end=" ")
 
# t=1,2,3
# print(t)
# a,b,c=t
# print(a,b,c)

# s={1,2,3,4,5}
# print(s)
# n=frozenset(s)
# r=set()
# print(r)
# print(n)
# print(type(s))
# print(len(s))
# s.add(6)
# print(s)
# s.update([7,8])
# print(s)
# s.remove(2)
# print(s)
# s.discard(4)
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)
# r={4,5,6,7,8}
# print(r)
# print(s|r)
# print(s&r)
# print(s^r)
# print(r.issubset(s))
# print(r.issuperset(s))
# b=s.copy()
# print(b)
# print(sorted(b))
# print(max(s))
# print(min(s))
# print(sum(s))



# d={"name":"Hari","age":20,}
# print(d["name"])
# r={}
# print(r)
# print(d.get("name"))
# d["Gender"]="Male"
# print(d)
# d.update({"age":19})
# print(d)
# d.setdefault("d",4)
# d.pop("d")
# print(d)
# d.popitem()
# print(d)
# del d["age"]
# print(d)

# print(d.keys())
# print(d.values())
# print(dict([(1,'a')]))
# print("a" in d)
# print("x" not in d)

# for k in d:
#     print(k)

# for v in d.values():
#     print(v)

# for k,v in d.items():
#     print(k,v)

# print(d.items())

# x=('apple',[1,2,3,4,5],2.5,7,{'a':25,'b':75})
# x[1][2]=10
# print(x)
# x[4]["a"]=75
# print(x)

# x=['name','age','qualification']
# y=['anu',24,'post Graduate']

# d={}
# for i in x:
#     for j in y:
#         d={i:j}


# for i in range(len(x)):
#     d.update({x[i]:y[i]})
# print(d)


# x=input("Enter a string: ")
# d={}
# for i in x:
#     d.update({i:x.count(i)})
# print(d)

# Roshin=3
# Gay=3
# a=["true" if Roshin==Gay else ]

# x=10
# r='Even' if x%2==0 else 'Odd'
# print(r)

# a=5
# b=8
# c=7
# max=a if a>b&a>c else b if b>c else c
# print(max)

# def findSq(num):
#     result = num*num
#     return result
# square=print(findSq(3))

# def pow(a,b):
#     return a**b

# x=int(input("Enter The Number: "))
# y=int(input("Enter the Power:"))
# print(pow(x,y))


# def amst(x):
#     while(x!=0):
#         sum=0
#         n=x
#         digit=x%10
#         cube=digit*digit*digit
#         sum=sum+cube
#         x=x//10

#     if(sum==n):
#         print("True")
#     else:
#         print("False")
        
    
# a=int(input("Enter A 3 Digit Value: "))
# amst(a)

import math
sqrt=math.sqrt(4)

print(sqrt)


        

