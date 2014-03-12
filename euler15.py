#How many routes, only moving to the right and down, are there in a 20x20 grid

import math
x = math.factorial(40) / (math.factorial(40 - 20) * math.factorial(20))
print(x)
