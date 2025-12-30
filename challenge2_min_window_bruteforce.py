#practice 

n=int(input("Enter the no of team members: "))
contribution=[]
for i in range(n):
    x=input("Enter contribution; ")
    contribution.append(x)
print(contribution)
impact=[]
for i in range(n):
    for j in range(n):
       y= x*contribution
       impact.append(y)
print(impact)




