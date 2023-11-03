# Write a program to print the maximum and minimum value from the list.

n=int(input())
l=[]
for i in range(0,n):
    x=int(input())
    l.append(x)
max=0
for i in l:
        if i>max:
           max=i
print("The maximum number is:",max)
min=l[0]
for i in l:
    if i<min:
        min=i
print("The minimun number is:",min)
    

        
