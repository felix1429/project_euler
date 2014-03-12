x = 1
y = 2
total = 2
while True:
    z = x + y
    x = y
    y = z
    if z > 4000000:
        break
    if z % 2 == 0:
        total += z
print(total)


    
    
