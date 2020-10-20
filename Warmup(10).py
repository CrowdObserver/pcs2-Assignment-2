# Exercise Solve Me First

def solveMeFirst(a,b):
    return a + b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

# Exercise A very big sum

def aVeryBigSum(ar):
    s = 0
    for _ in ar:
        s += int(_)
    return s

# Exercise Simple Array Sum

def simpleArraySum(ar):
    s = 0
    for _ in ar:
        s += int(_)
    return s

# Exercise Compare the triplets

def compareTriplets(a, b):
    ar = 0
    br = 0
    for _ in range(len(a)):
        if a[_] > b[_]:
            ar += 1
        elif a[_] < b[_]:
            br += 1
    return ar, br

# Exercise Diagonal Difference

def diagonalDifference(arr):
    p = 0
    s = 0
    for _ in range(n):
        p += arr[_][_]
        s += arr[_][-_ - 1]
    return abs(p - s)

# Exercise Plus Minus

def plusMinus(arr):
    p = 0
    ng = 0
    z = 0
    for _ in arr:
        if _ < 0:
            ng += 1
        elif _ > 0:
            p += 1
        else:
            z += 1
    print(p/n)
    print(ng/n)
    print(z/n)

# Exercise Staircase

def staircase(n):
    for _ in range(1, n + 1):
        s = "#" * _
        print(s.rjust(n))

# Exercise Mini-Max Sum

def miniMaxSum(arr):
    l = []
    for _ in arr:
        f = _
        i = arr.index(_)
        arr.remove(_)
        l.append(sum(arr))
        arr.insert(i, f)
    print(min(l), max(l))

# Exercise Birthday Cake Candles

def birthdayCakeCandles(candles):
    f = max(candles)
    r = 0
    for _ in candles:
        if int(_) == f:
            r += 1
    return r

# Exercise Time Convertion

def timeConversion(s):
    if s[0:2] == "12" and s[-2:] == "AM":
        return "00" + s[2:-2]
    elif s[0:2] == "12" and s[-2:] == "PM":
        return "12" + s[2:-2]
    elif int(s[0:2]) < 12 and s[-2:] == "AM":
        return s[:-2]
    else:
        return str(int(s[0:2])+12) + s[2:-2]

