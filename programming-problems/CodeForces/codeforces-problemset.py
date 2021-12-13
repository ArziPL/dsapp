# CodeForces problemset Python
# Submitted in PyPy 3.7 (7.3.0) or PyPy 3.7 (7.3.5, 64bit)
# [PROBLEM CODE] [PROBLEM NAME]

# 133A HQ9+

p = input()

for i in p:
    if i == "H" or i == "Q" or i == "9":
        print("YES")
        exit()
print("NO")


# 160A Twins

n = int(input())
a = input().split()
a = [int(x) for x in a]
a.sort()

myCoins = 0
hisCoins = sum(a)
ansFromSmallest = 0
while myCoins <= hisCoins:
    myCoins += a[0 + ansFromSmallest]
    hisCoins -= a[0 + ansFromSmallest]
    ansFromSmallest+=1

myCoins = 0
hisCoins = sum(a)
ansFromBiggest = 0
while myCoins <= hisCoins:
    myCoins += a[len(a)-1 - ansFromBiggest]
    hisCoins -= a[len(a)-1 - ansFromBiggest]
    ansFromBiggest+=1

print(min(ansFromSmallest,ansFromBiggest))

# 1607A Linear Keyboard

t = int(input())
keyboard = ""
word = ""
ans = [0] * t
for t in range(t):
    keyboard = input()
    word = input()
    for count in range(1,len(word)):
        ans[t] += abs(keyboard.find(word[count-1]) - keyboard.find(word[count]))
    
for i in ans:
    print(i)


# 122A Lucky Division
# Forced solution, easy to hacked
# Despite that, all tests passed

n = input()
checkList = list(n)
num = int(n)
selfLucky = True

notLucky = ["1","2","3","5","6","8","9","0"]
for i in notLucky:
    if i in checkList:
        selfLucky = False

if selfLucky == True:
    print("YES") 
elif num%4 == 0 or num%7 == 0 or num%47 == 0 or num%74 == 0:
    print("YES")
else:
    print("NO")


# 58A Chat room

s = list(input())
h = "hello"
i = 0
for j in range(len(s)):
    if s[j] == h[i]:
        i+=1
        if i == len(h):
            break

print("YES") if i == len(h) else print("NO")

# 96A Football

n = input()
oneCount = 0
zeroCount = 0

if n.find("1111111") != -1 or n.find("0000000") != -1:
    print("YES")
else:
    print("NO")

# 69A Young Physicist

n = int(input())
a = [0] * 3
for i in range(n):
    b = [int(x) for x in input().split()]
    for j in range(3):
        a[j] += b[j]

ans = [x for x in a if x == 0]
print('YES' if len(ans) == 3 else 'NO')


# 118A String Task

n = list(input().lower())
ans = []
for i,item in enumerate(n):
    if item in ["a","o","y","e","u","i"]:
        n[i] = ''

for i in range(0,n.count('')):
    n.remove('')


for i in range(0,len(n)):
    ans.append('.')
    ans.append(n[i])

print(''.join(ans))

# 1A Theatre Square

import math;

fInput = input()
fInput = fInput.split()
n = int(fInput[0])
m = int(fInput[1])
a = int(fInput[2])

print((math.floor((m+a-1)/a))*(math.floor((n+a-1)/a)))


# 677A Vanya and Fence

fInput = input()
sInput = input()
fInput = fInput.split()
sInput = sInput.split()

n = fInput[0]
h = fInput[1]
a = sInput
ans = 0

for i in a:
    if int(i) > int(h):
        ans += 2
    else :
        ans += 1
print(ans)

# 271A Beautiful Year

y = int(input())
y = y + 1
ansFound = False

while not ansFound:
    if len(set(list(str(y)))) >= 4:
        ansFound = True
        print(y)
    else :
        y = y + 1


# 734A Anton and Danik

n = input()
s = list(input())
aCount = s.count("A")
dCount = s.count("D")

if aCount > dCount:
    print("Anton")
elif dCount > aCount:
    print("Danik")
else:
    print("Friendship")



# 41A Translation

s = list(input())
t = list(input())
t.reverse()

if s == t:
    print("YES")
else:
    print("NO")



# 110A Nearly Lucky Number

n = list(input())
ans = 0

for i in n:
	if(i == "4" or i == "7"):
		ans += 1

print("YES") if (ans == 4 or ans == 7) else print("NO")


# 266B Queue at the School

n,t = map(int,input().split())
s=input()

while t:
	s=s.replace("BG","GB")
	t-=1
print (s)


# 116A Tram

n = int(input())
raw_inputs = []

while n > 0:
    arr_list = list(map(int,input().split()))
    raw_inputs.append(arr_list)
    n = n - 1

inputs = []
for e in raw_inputs:
    inputs += e

passengers = 0
maxpassangers = 0
loopcounter = 1

for i in inputs:
    if loopcounter%2==0:
        passengers += i
        loopcounter += 1
    else:
        passengers -= i
        loopcounter += 1

    if passengers > maxpassangers:
        maxpassangers = passengers

print(maxpassangers)

# 59A Word

s = input()
upperCount = 0
lowerCount = 0

for c in s:
    if c.isupper():
        upperCount += 1
    else:
        lowerCount += 1

if upperCount > lowerCount:
    print(s.upper())
elif lowerCount >= upperCount:
    print(s.lower())

# 617A Elephant

x = int(input())
step = 5
ans = 0

while x > 0:
    if(x - step > 0):
        x -= step
        ans += 1
    else:
        while(x - step < 0):
             step -= 1
    x -= step
    ans += 1

print(ans)



# 977A Wrong Subtraction

inputs = list(map(int,input().split()))
n = inputs[0]
k = inputs[1]

while k > 0:
    num_to_string = str(int(n))
    if(num_to_string[-1] == '0'):
        n = n / 10
    else:
        n -= 1

    k -= 1

print(int(n))



# 791A Bear and Big Brother

inputs = list(map(int,input().split()))
firstBear = inputs[0]
secondBear = inputs[1]
ans = 0
while True:
    ans += 1
    firstBear = firstBear * 3
    secondBear = secondBear * 2
    if firstBear>secondBear:
        print(ans)
        break



# 546A Soldier and Bananas

inputs = list(map(int,input().split()))
k = inputs[0]
n = inputs[1]
w = inputs[2]
res = 0

for i in range(w+1):
    res += k*i
    
if(res<n):
    print(0)
else:
    print(res-n)



#236A Boy or Girl

s = input()
res = "".join(set(s))

if len(res)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")



# 266A Stones on the Table

n = int(input())
s = input()

red = 0
green = 0
blue = 0

for i in range(1, n):

    if(s[i-1] == s[i]):

        if(s[i] == "R"):

            red = red + 1

        elif (s[i] == "G"):

            green = green + 1

        else:

            blue = blue + 1 

print(red+green+blue)



# 281A Word Capitalization

s = input()
s_list = list(s)
s_list[0] = s_list[0].upper()
print("".join(s_list))



# 339A Helpful Maths

s = input()
res = s.split('+')
res.sort()
res = '+'.join(res)
print(res)




# 263A Beautiful Matrix

matrix = list()
for i in range(0,5):
    matrix.append(input().replace(" ",""))


for i in range(0,5):
    if "1" in matrix[i]:
        num_pos_x = i
        num_pos_y = int(matrix[i].find("1"))

print(abs(2-num_pos_x) + abs(2-num_pos_y))



# 112A Petya and Strings

first = input().lower()
second = input().lower()

if first < second:
    print(-1)
elif first > second:
    print(1)
else:
    print(0)



# 282A Bit++

n = int(input())
inputs = list()
ans = 0

for x in range(0,n):
    inputs.append(input())
    inp = inputs[x]
    if(inp[1] == "+"):
        ans+=1
    elif(inp[1]=="-"):
        ans-=1

print(ans)



# 50A Domino piling

import math

inputs = list(map(int,input().split()))
m = inputs[0]
n = inputs[1]

print(math.floor(m*n/2))



# 158A Next Round

x = list(map(int, input().split()))

user_count = x[0]
k_place = x[1]
ans = 0

inputs = input().split()
min_to_pass = int(inputs[k_place-1])

if int(inputs[0]) < min_to_pass:
    min_to_pass = int(inputs[0])


for i in inputs:
    if int(i) == 0:
        pass
    elif int(i) >= min_to_pass:
        ans+=1

print(ans)



# 231A Team

n = int(input())
ans = 0
for x in range(0,n):
    inp = input()
    if "1 1" in inp:
        ans += 1
    elif "1 0 1" in inp:
        ans += 1
print(ans)



# 71A Way Too Long Words

n = int(input())
inputs = list()
for x in range(0,n):
    inputs.append(input())

for x in range(0,n):
    temp = inputs[x]
    if len(temp) > 10:
        print(temp[0] + str(len(temp)-2) + temp[-1])
    else:
        print(temp)        



# 4A Watermelon

w = int(input())

if w%2!=0 or w==2:
    print("NO")
else:
    print("YES")