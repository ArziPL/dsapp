# primality_test - O(n) check every number apart from 1 and number itself,
# if number%any from (2,itself) gives 0 then number is not prime

# optimized_primality_test : O(sqrt(n)) - if x divide n then n/x = y which divides n as well, so we need to check only
# numbers from 1 to sqrt(n). sqrt(n) is border because sqrt(n) * sqrt(n) gives n, which then implies that values after 
# sqrt(n) need to be multiplied by values lesser then sqrt(n) which we already checked


def primality_test(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True


print(primality_test(6793))


def optimized_primality_test(num):
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


print(optimized_primality_test(6793))
