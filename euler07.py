prime_counter = 0
for x in range(2,500000):
    value = 0
    for counter in range(2,int((x ** .5) + 1)):
        if x % counter == 0:
            value += 1
    if value == 0:
        prime_counter += 1
        if prime_counter == 10001:
            print(x)
            break

