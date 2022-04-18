# Euclidean algorithm
# Greatest common divisor

# gcd - if one of numbers (y) is 0, gcd should be second number (x), we check the second number recursively in else statement
# x%y returns the rest of the division, so we do that alternately on every number until one of them is 0, then back to step 1
# gdc_extended - Subtract smaller number from bigger until one of them get to 0, last number should be gcd


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def gcd_extended(x, y):
    while x != 0 and y != 0:
        if x >= y:
            x -= y
        else:
            y -= x
    return x + y


print(gcd(99, 18))
# 99 18
# 18 9
# 9 0
# 9

print(gcd_extended(99, 18))
# 99 18
# 81 18
# 63 18
# 45 18
# 27 18
# 9 18
# 9 9
# 9
