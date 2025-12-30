#taking input
log = input("Enter the log: ")
pattern = input("Enter the pattern ")

req = {}
for char in pattern:
    if char in req:
        req[char] += 1
    else:
        req[char] = 1

min_length = len(log) + 1
res = ""

#loop
for i in range(len(log)):        
    for j in range(i, len(log)): 
        substring = log[i:j+1]  

        
        substring_count = {}
        for char in substring:
            if char in substring_count:
                substring_count[char] += 1
            else:
                substring_count[char] = 1

        
        valid = True
        for char in req:
            if substring_count.get(char, 0) < req[char]:
                valid = False
                break

        
        if valid and len(substring) < min_length:
            min_length = len(substring)
            res = substring

print(res)
