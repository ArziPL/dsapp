# primality_test - O(n) check every number apart from 1 and number itself,
# if number%any from (2,itself) gives 0 then number is not prime

# optimized_primality_test : if we will take any number from 1 to sqrt(n) then that number need to be multiplied by something more
# then sqrt(n) to get us n, this way we don't have to check any number bigger then sqrt(n) because numbers kinda "mirrors" themselves,
# if 4*6 gives 24 and we check 4 then there's no point to check 6

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
