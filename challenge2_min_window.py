#CHALLENGE 1 ;
#TKING user input
n = int(input("Enter nO of team members: "))
contribution = []
for i in range(n):
    x = int(input(f"Enter contribution of member {i}: "))
    contribution.append(x)

left = [1] * n   
right = [1] * n  
impact = [0] * n 

#left
prod = 1
for i in range(n):
    left[i] = prod
    prod *= contribution[i]
#right
prod = 1
for i in range(n-1, -1, -1):
    right[i] = prod
    prod *= contribution[i]


for i in range(n):
    impact[i] = left[i] * right[i]


print(impact)
