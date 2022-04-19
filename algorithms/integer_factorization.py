# O(sqrt(n)) - if x divide n then n/x = y which divides n as well, so we need to check only
# numbers from 1 to sqrt(n). sqrt(n) is border because sqrt(n) * sqrt(n) gives n, which then implies that values after
# sqrt(n) need to be multiplied by values lesser then sqrt(n) which we already checked

# Integer factorization - take samllest number i>=2 which divide number, if it's divisor 
# then divide num, check again, if not then add 1 to i and check again until i is
# bigger or equal to num

def integer_factorization(num):
    result = []
    i = 2
    while i*i <= num:
        if num%i==0:
            result.append(i)
            num = num//i
        else:
            i+=1
    
    if num > 1:
        result.append(num)
    return result

print(integer_factorization(315))
