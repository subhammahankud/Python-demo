# a=int(input("Enter no1 "))
# b=int(input("Enter no2 "))
# c=a+b/2
# print(a," ",b)
# print(a**2)
# l=[1,2,21,54,21,45,21]
# l.pop(2)
# print(l)
# s="Subham"
# print(s[1])
# s[1]='j'
# print(s)
# l=[1,2,21,54,21,45,21]
# l.sort()
# # print(sum(l))
# a=l.count(21)
# print(a)
# marks={
#     "subh":12,
#     "ram":15,
#     "0":45,
#     12:45
# }
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.get("subh"))
# print(marks["subh"])
# a=int(input())
# if(a>18):
#     print("Adult")
# else:
#     print("kid")
# for i in range(1,11):
#     print(i)
# i=1
# while(i<11):
#     print(i)
#     i+=1
# l=["Subham", 1, True, "Mahankud", False]
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1
# for i in range(0,len(l)):
#     print(l[i])
# f="Subham"
# for i in f:
#     print(i)
# n=int(input("Enter"))
# s=0
# for i in range(1,n+1):
#     s+=i
#     # print(f"{n}x{i}={n*i}")
# print(s) 
# n=int(input("Enter"))
# s=1
# for i in range(1,n+1):
#     s*=i
#     # print(f"{n}x{i}={n*i}")
# print(s)   
# def  fact(n):
#     if(n==1 or n==0):
#         return 1
#     return n*fact(n-1)

# n= int(input())
# print(fact(n))
# def nat(n):
#     for i in range(1,n+1):
#         print(i,end=" ")
# n=int(input())
# nat(n)
# def sum(n):
#     if(n==1):
#         return 1
#     return n+sum(n-1)
# print(sum(4))
# f=open("file.txt")
# data=f.read()
# print(data)
# f.close
# import os
# path=input("Enter Path")
# if os.path.isfile(path):
#     print("It is a file")

# else:
#     print("It is a directory")
#     files=os.listdir(path)
#     print(files)
# Python program to read a file and convert each line into a list

# Specify the file name
# Python program to check if "subham" is present in a file



import openpyxl

# Load the workbook
wb = openpyxl.load_workbook("data_workbook.xlsx")

# Select the active sheet
sheet = wb.active

# Read and print the data
for row in sheet.iter_rows(min_row=1, max_row=3, values_only=True):
    print(row)



