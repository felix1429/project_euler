#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find a * b * c

for x in range(50, 1000):
    for y in range(x + 1, 1000):
        for z in range(y + 1, 1000):
            if z * z == (x * x) + (y * y):
                if x + y + z == 1000:
                    print(x * y * z)
