# Largest palindrome from multiplying two three digit numbers

# 998001 is 999 * 999
# start at 998001 and iterate down until first palindrome
# then divide that palindrome by 999, 999 - 1, 999 - 2 etc until it
# divides evenly or runs out of numbers, in which case the next palindrome
# is moved to

def is_palindrome(number): #function that checks if number is a palindrome
    number = str(number)
    y = len(number)
    x = 0
    while True:
        if number[x] == number[y - 1]:
            pass
        else:
            return False
            break
        if x == y or y - x == 1:
            return True
            break
        y -= 1
        x += 1


done = False
for foo in range(998001,1,-1):
    if is_palindrome(foo) == True:
        the_number = foo
        for diviser in range(999,int(the_number ** .5),-1):
            if the_number % diviser == 0:
                other_diviser = the_number / diviser
                print(the_number)
                done = True
                break
    if done == True:
        break
            
