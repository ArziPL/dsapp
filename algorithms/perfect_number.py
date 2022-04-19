# optimized_perfect_number - O(sqrt(n)) - if x divide n then n/x = y which divides n as well, so we need to check only
# numbers from 1 to sqrt(n). sqrt(n) is border because sqrt(n) * sqrt(n) gives n, which then implies that values after
# sqrt(n) need to be multiplied by values lesser then sqrt(n) which we already checked

def perfect_number(num):
    sum = 1
    i = 2
    while i*i <= num:
        if num % i == 0:
            sum += i
            if i != num//i:
                sum += num//i
        i += 1

    if sum == num:
        return True
    else:
        return False

print(perfect_number(28))
