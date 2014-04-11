##If the numbers 1 to 5 are written out in words: one, two, three, four, five,
##then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
##If all the numbers from 1 to 1000 (one thousand) inclusive were written
##out in words, how many letters would be used?
##
##
##NOTE: Do not count spaces or hyphens.
##For example, 342(three hundred and forty-two) contains 24 letters
##and 115 (one hundred and fifteen) contains 20 letters.

def ones(x):
    if x == 0: return ""
    elif x == 1: return "one"
    elif x == 2: return "two"
    elif x == 3: return "three"
    elif x == 4: return "four"
    elif x == 5: return "five"
    elif x == 6: return "six"
    elif x == 7: return "seven"
    elif x == 8: return "eight"
    elif x == 9: return "nine"


def tens(x):
    if x < 20:
        if x == 10: return "ten"
        elif x == 11: return "eleven"
        elif x == 12: return "twelve"
        elif x == 13: return "thirteen"
        elif x == 14: return "fourteen"
        elif x == 15: return "fifteen"
        elif x == 16: return "sixteen"
        elif x == 17: return "seventeen"
        elif x == 18: return "eighteen"
        elif x == 19: return "nineteen"
    else:
        first_digit = int(str(x)[0])
        second_digit = int(str(x)[1])
        if first_digit ==  2: return "twenty" + ones(second_digit)
        elif first_digit == 3: return "thirty" + ones(second_digit)
        elif first_digit == 4: return "forty" + ones(second_digit)
        elif first_digit == 5: return "fifty" + ones(second_digit)
        elif first_digit == 6: return "sixty" + ones(second_digit)
        elif first_digit == 7: return "seventy" + ones(second_digit)
        elif first_digit == 8: return "eighty" + ones(second_digit)
        elif first_digit == 9: return "ninety" + ones(second_digit)

def hundreds(x):
    first_digit = int(str(x)[0])
    second_digit = int(str(x)[1])
    third_digit = int(str(x)[2])
    if second_digit == 0 and third_digit == 0:
        return ones(first_digit) + "hundred"
    elif second_digit == 0:
        return ones(first_digit) + "hundredand" + ones(third_digit)
    elif second_digit == 1:
        return ones(first_digit) + "hundredand" + tens(int("{0}{1}".format(second_digit, third_digit)))
    else:
        return ones(first_digit) + "hundredand" + tens(int("{0}{1}".format(second_digit, third_digit)))


total = 0
for num in range(1,1001):
    str_num = str(num)
    if len(str_num) == 1:
        word = ones(num)
        total += len(word)
    elif len(str_num) == 2:
        word = tens(num)
        total += len(word)
    elif len(str_num) == 3:
        word = hundreds(num)
        total += len(word)
    elif str_num == "1000":
        word = "onethousand"
        total += len(word)
print(total)
