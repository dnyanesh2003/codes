'''Write a Python program to store first year percentage of students in array. Write
function forsorting array of floating point numbers in ascending order using quick
sort and display top five scores.'''

def quickS(arr):
    if(len(arr)<=1):
        return arr
    else:
        pivot=arr[len(arr)//2]
        mid=[x for x in arr if x==pivot]
        left=[x for x in arr if x<pivot]
        right=[x for x in arr if x>pivot]
        return quickS(left)+mid+quickS(right)
    
def display(arr):
    if(len(arr)<=6):
        print(*arr[::-1])
    else:
        print(*arr[:len(arr)-6:-1])

lst=[]
n=int(input("Enter no.of students whos marks to be inserted : "))
for i in range(n):
    m=int(input("Enter marks : "))
    lst.append(m)

#Quick sort
a=quickS(lst)
print("sorted array:",a)
b=display(a)
print("toppers:",b)