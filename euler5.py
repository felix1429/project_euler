# smallest number divisible by 1 - 20

def divisible_by_all(x):
    for count in range(2, 20):
        if x % count != 0:
            return False
            break    

counter = 19
while True:
    if counter % 19 == 0 and counter % 17 ==0:
        if divisible_by_all(counter) != False:
            print(counter)
            break
        else:
            counter += 19
    else:
        counter += 19
