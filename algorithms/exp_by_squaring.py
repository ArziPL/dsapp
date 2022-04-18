# O(log n) - but i don't know really why

# 2^100 = 2^50 * 2^50 so we can calculate x = 2^50 and then x * x = 2^50 * 2^50 = 2^100 so we don't have to calculate powers
# from 2^50 to 2^100

# 2^101 = 2^1 * 2^100 = 2^1 * (2^50 * 2^50) - we subtract 1 from odd exponents, we get even exponent, do the trick \
# for that even exponent and multiply by base^1 which just was subtracted

def exp_by_squaring(a, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            x = exp_by_squaring(a, n//2)
            return x*x
        else:
            return a * exp_by_squaring(a, n - 1)


print("17^1 = ", exp_by_squaring(17, 0))
print("17^1 = ", exp_by_squaring(17, 1))
print("2^2 = ", exp_by_squaring(2, 2))
print("2^3 = ", exp_by_squaring(2, 3))
print("2^4 = ", exp_by_squaring(2, 4))
print("2^5 = ", exp_by_squaring(2, 5))
print("3^2 = ", exp_by_squaring(3, 2))
print("3^3 = ", exp_by_squaring(3, 3))
print("5^2 = ", exp_by_squaring(5, 2))
print("5^3 = ", exp_by_squaring(5, 3))
print("10^2 = ", exp_by_squaring(10, 2))
print("10^3 = ", exp_by_squaring(10, 3))
print("1000^5 = ", exp_by_squaring(1000, 3))
print("Performance test")
exp_by_squaring(9230286038352, 9325)
print("Performance test done")
