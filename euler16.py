#What is the sum of the digits of the number 2 ** 1000

total = 0
x = str(2 ** 1000)
for count in range(len(x)):
    num = int(x[count])
    total += num
print(total)    
