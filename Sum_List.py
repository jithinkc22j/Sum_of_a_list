m=int(input("Enter the limt:"))
numlist=[]
print("Enter the elements:")
for i in range(0,m):
    n=int(input())
    numlist.append(n)
# Calculate sum of list
print("The List L=",numlist)
numsum=0
for i in numlist:
    numsum+=i
print('Sum of List: ',numsum)