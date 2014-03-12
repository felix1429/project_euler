#The following iterative sequence is defined for the set of positive integers:

#n  n/2 (n is even)
#n  3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13  40  20  10  5  16  8  4  2  1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains
#10 terms. Although it has not been proved yet (Collatz Problem),
#it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?
'''
largest_count = 0
for starting_num in range(100,1000000):
    if starting_num % 2 == 0:
        running_total = starting_num / 2
    else:
        running_total = (starting_num * 3) + 1
    count = 1
    while True:
        if running_total == 1:
            if count > largest_count:
                largest_count = count
                longest_count = starting_num
            break
        elif running_total % 2 == 0:
            running_total = running_total / 2
            count += 1
        else:
            running_total = (running_total * 3) + 1
            count += 1
    print(starting_num)
print(longest_count, largest_count)
'''
largest_count = 0
longest_count = 0
running_total = 0
for starting_num in range(100, 1000000):
    running_total = starting_num
    count = 1
    while running_total != 1:
        if running_total % 2 == 0:
            running_total = running_total / 2
            count += 1
        else:
            running_total = (running_total * 3) + 1
            count += 1
    largest_count = count
    longest_count = starting_num
    print(starting_num)
    
        
    

