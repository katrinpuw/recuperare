import math

# Lambda functions

salary = [2, 9, 9, 10, 9, 7, 9, 9]

print(list(map(lambda x: x*2, salary)))

# Lazy evaluation

lis = [x/2 for x in range(50)]
print(lis)

# or

print(list(map(lambda x: x/2, range(0, 50))))

# Supperior functions


def hypotenuse(a, c):
    return math.sqrt(c**2 - a**2)


def superior_area(function, a):
    return (a * function)/2


print("Area of triagle = ", superior_area(hypotenuse(3, 5), 3))
