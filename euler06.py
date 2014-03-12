# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum

def difference(x):
    #square of sum
    total = 0
    for counter in range(1,x + 1):
        total += counter ** 2    

    #sum of squares
    sum_total = 0
    for counter in range(1,x + 1):
        sum_total += counter
    total1 = sum_total ** 2

    return (total1 - total)
