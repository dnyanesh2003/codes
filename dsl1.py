# In second year computer engineering class, group A student’s play cricket, group B
# studentsplay badminton and group C students play football.
# Write a Python program using functions to compute following: -
# a) List of students who play both cricket and badminton
# b) List of students who play either cricket or badminton but not both
# c) Number of students who play neither cricket nor badminton
# d) Number of students who play cricket and football but not badminton.
# (Note- While realizing the group, duplicate entries should be avoided, Do not use
# SET built-in functions)
def intersection(l1, l2):
    res=[]
    for student in l1:
        if student in l2:
            res.append(student)
    return res

def union(l1, l2):
    res= l2.copy()
     
    for student in l1:
        if not student in l2:
            res.append(student)

    return res 

def diff(l1, l2):
    res= []
     
    for student in l1:
        if not student in l2:
            res.append(student)

    return res 
a=[1,2,3,4,5,6,7] #jersy no of cricket players
b=[2,3,6,7,10] #jersy no of badminton players
c=[2,4,6,8,10,12] #jersy no of football players

print(intersection(a,b)) #student play cricket and badminton
print(diff(union(a,b),intersection(a,b))) #student play either cricket or Badminton
print(diff(c,union(a,b))) #student play neither cricket nor Badminton
print(diff(union(a,c),b)) #student play cricket and football but not Badminton
