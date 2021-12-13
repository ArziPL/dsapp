# Number Spiral

from sys import stdin, stdout 

t = int(input())
for i in range(t):
    inp = stdin.readline().split()
    inp = list(map(int,inp))
    x = inp[0]
    y = inp[1]
    whichIteration = max(y,x)
    result = 0 + pow(whichIteration-1,2)
    if whichIteration%2==0:
        if y == x:
            result+=y
        if x < y:
            result+=x
        elif x>y:
            result+=x+x-y
    else:
        if y == x:
                result+=y
        elif x>y:
                result+=y
        elif x<y:
                result+=y+y-x
    stdout.write(str(result) + "\n")


# Scheme
# 1 1 = 1
# 1 2
# 2 2 = 3
# 2 1 = 4

# 3 1 = 5
# 3 2
# 3 3 = 7
# 2 3 = 8
# 1 3 = 9


# 1 4
# 2 4 = 11
# 3 4
# 4 4 = 13
# 4 3
# 4 2 = 15
# 4 1 = 16

# 5 1
# 5 2 = 18
# 5 3 
# 5 4 = 20
# 5 5 = 21
# 4 5
# 3 5
# 2 5 = 24
# 1 5 = 25


# 1 6
# 2 6 = 27
# 3 6
# 4 6
# 5 6 = 30
# 6 6 = 31
# 6 5
# 6 4 = 33
# 6 3
# 6 2 = 35
# 6 1 = 36



# Permutations

def result():
    for i in range(1,n+1):
        if i%2==0:
            print(i,end=" ")
    for i in range(1,n+1):
        if i%2!=0:
            print(i,end=" ")

n = int(input())
if(n%2==0 and n-1-2>=1):
    result()
elif(n%2!=0 and n-2>1):
    result()
elif(n==1):
    print(1)
elif(n-3<1 or n-2<=1):
    print("NO SOLUTION")

# Repetitions 

n = input()
ans = 0
count = 1
for i in range(len(n)-1):
    if n[i] == n[i+1]:
        count = count + 1
    else :
        ans = max(ans,count)
        count = 1


ans = max(ans,count)
print(ans)


# Missing Number

n = int(input())
inp = input().split()
fullSum = 0
inpSum = 0
forRange = n - 1
for i in range(forRange):
    fullSum = fullSum + n
    inpSum = inpSum + int(inp[i])
    n = n - 1

print(fullSum + n - inpSum)


# Weird Algorithm

n = int(input())
print(int(n), end=" ")

while n != 1:
    if n%2==0:
        n/=2
        print(int(n), end=" ")
    else:
        n = n * 3 + 1
        print(int(n), end=" ")