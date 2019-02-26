import random 
p = random.randint(1, 100) 
print("Input 1<=number<=100") 
m = int(input("input - ")) 
if m > 100 or m < 1: 
print("Error") 
i = 0 
while i < 200: 
if m > p: 
print("Input more low number") 
m = int(input("Input - ")) 
if m < p: 
print("Input more high number") 
m = int(input("Input - ")) 
if m == p: 
i = 200 
i += 1 
break 

print("GLORIOUS VICTORY")
