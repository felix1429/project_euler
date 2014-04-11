total = 0
for x in range(2,(2000001)):
    counter = 2
    value = 0
    for counter in range(2,int((x ** .5) + 1)):
        if x % counter == 0:
            value += 1
            break
    if value == 0:
        total += x
print(total)        

