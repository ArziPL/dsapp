# O(2^n) - recursive "easiest to remember" fibonacci
# O(n) - iterate fibonacci
# O(2^n) - fibonacci with memoization : sequence operations are
# often repeated, therefore we save them in cache and every time we do
# calculations we check whether we have already made them, new calculations
# are saved into cache

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    elif num > 2:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci_iterate(num):
    result = [0, 1, 1]
    if num < 3:
        return result[num]
    else:
        for i in range(3, num+1):
            result.append(result[i - 1] + result[i - 2])
        return result[-1]


fibonacci_cache = {}


def fibonacci_memo(num):
    if num in fibonacci_cache:
        return fibonacci_cache[num]
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    elif num > 2:
        value = fibonacci_memo(num - 1) + fibonacci_memo(num - 2)
        fibonacci_cache[num] = value
        return value


print("Normal : ")
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6), end="\n\n\n")
# print(fibonacci(50)) - not achivable without memoization
# print(fibonacci(100))
# print(fibonacci(200))


print("Iterate : ")
print(fibonacci_iterate(0))
print(fibonacci_iterate(1))
print(fibonacci_iterate(2))
print(fibonacci_iterate(3))
print(fibonacci_iterate(4))
print(fibonacci_iterate(5))
print(fibonacci_iterate(6), end="\n\n\n")
# print(fibonacci(50)) - not achivable without memoization
# print(fibonacci(100))
# print(fibonacci(200))


print("Memo : ")
print(fibonacci_memo(0))
print(fibonacci_memo(1))
print(fibonacci_memo(2))
print(fibonacci_memo(3))
print(fibonacci_memo(4))
print(fibonacci_memo(5))
print(fibonacci_memo(6))
print(fibonacci_memo(50))
print(fibonacci_memo(100))
print(fibonacci_memo(200))
