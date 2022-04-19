# optimized_primality_test : O(sqrt(n)) - if x divide n then n/x = y which divides n as well, so we need to check only
# numbers from 1 to sqrt(n). sqrt(n) is border because sqrt(n) * sqrt(n) gives n, which then implies that values after
# sqrt(n) need to be multiplied by values lesser then sqrt(n) which we already checked

def primality_test(num):
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


print(primality_test(6793))