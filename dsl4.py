'''Write a Python program to store names and mobile numbers of your friends
in sorted order on names. Search your friend from list using binary search
(recursive and non- recursive). Insert friend if not present in phonebook
b) Write a Python program to store names and mobile numbers of your friends in
sorted order on names. Search your'''
def Binary_R(arr,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if(arr[mid]==target):
        return mid
    elif (arr[mid]<target):
        return Binary_R(arr,target,mid+1,high)
    else:
        mid=mid-1
        return Binary_R(arr,target,low,mid-1)

def Binary_I(arr,target):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)/2
        if (arr[mid]==target):
            return mid
        elif (arr[mid]<target):
            low=mid+1
        else:
            high=mid-1
    return -1

print("Phonebook")
phonebook={ }
contact=int(input("Enter number of contact to be inserted "))
for i in range (contact):
    key=input("Enter name : ")
    value=int(input("Enter contact no . "))
    phonebook[key]=value
my_list=list(phonebook.keys())
names=sorted(my_list)
n=len(names)
print("Contact of phonebook : ",phonebook)

flag=1
while(flag==1):
    print("1.Binary recursive search : ")
    print("2.Binary non-recursive search : ")
    print("3.inserted new contact in phonebook : ")
    print("4. Exit ")

    ch=int(input("Enter choice : "))

    if(ch==1):
        target=input("Enter the target to be inserted : ")
        result=Binary_R(names,target,0,n-1)
        print(result)
        if (result!= -1):
            print(f"Contact found:{target}-Phone number :{phonebook.get(target)}")
        else:
            print("Contact not found")

    elif(ch==2):
        target=input("Enter the target to be inserted : ")
        result=Binary_I(names,target)
        print(result)
        if (result!= -1):
            print(f"Contact found:{target}-Phone number :{phonebook.get(target)}")
        else:
            print("Contact not found")
        
    elif(ch==3):
        new=int(input("No. of contacts to be inserted "))
        for i in range (new):
            key=input("Enter name : ")
            value=int(input("Enter contact no . "))
            phonebook[key]=value
        lst=list(phonebook.keys())
        lst2=sorted(lst)
        n=len(lst2)
        print("Phonebook after inserting contacts :",phonebook)

    else:
        print("Plz enter valid choice : ")
        flag=0