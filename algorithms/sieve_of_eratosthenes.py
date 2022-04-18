# O(n*log(log(n)))

# https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn/ - ??? xD

#https://en.wikipedia.org/wiki/File:Sieve_of_Eratosthenes_animation.gif

# I highly recommend to look for explanation in internet because mechanism behind it is tricky

def sieve_of_eratosthenes(num):
    prime_numbers = [True for i in range(num+1)]
    for i in range(2, num):
        k = i
        if prime_numbers[i]:
            while i*k <= num:
                prime_numbers[i*k] = False
                k += 1

    prime_numbers[0] = False
    prime_numbers[1] = False
    return prime_numbers


for inx, i in enumerate(sieve_of_eratosthenes(20)):
    print(inx, i)
