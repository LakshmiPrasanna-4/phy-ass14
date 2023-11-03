# Write a program to merge two list and find the minimum value from the list.

n=int(input())
ar1=list(map(int,input().split()))
m=int(input())
ar2=list(map(int,input().split()))
ar1.extend(ar2)
min=ar1[0]
for i in ar1:
    if i<min:
        min=i
print(min)
