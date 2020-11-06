# Exercise Caesar Cipher

def caesarCipher(s, k):
    while k > 26:
        k -=26
    l = list(s.split("-"))
    abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    l1 = []
    for _ in l:
        s = ""
        for i in _:
            if i.islower() and i in abc:
                s += abc[abc.index(i.lower())+k]
            elif i.isupper() and i.lower() in abc:
                s += abc[abc.index(i.lower())+k].upper()
            else:
                s += i
        l1.append(s)
    res = ""
    for _ in l1:
        res += _ + "-"
    return res[:-1]

# Exercise Strong password

def minimumNumber(n, password):
    d = 0
    u = 0
    l = 0
    s = 0
    for _ in password:
        if _.isdigit() and d == 0:
            d += 1
        elif _.isupper() and u == 0:
            u += 1
        elif _.islower() and l == 0:
            l += 1
        elif _ in "!@#$%^&*()-+" and s == 0:
            s += 1
    if n >= 6:
        return 4 - (d + u + l + s)
    else:
        if 4 - (d + u + l + s) > 6 - n:
            return 4 - (d + u + l + s)
        else:
            return 6 - n

# Exercise Mars Exploration

def marsExploration(s):
    tmp = ["S","O","S"]
    count = 0
    for _ in range(0, len(s), 3):
        for i in range(3):
                if s[_:_+3][i] != tmp[i]:
                    count += 1
                else:
                    continue
    return count

# Exercise CamelCase

def camelcase(s):
    count = 1
    for _ in s:
        if _.isupper():
            count += 1
    return count

# Exercise HackerRank in a string

def hackerrankInString(s):
    f = "hackerrank"
    f1 = ""
    k = "hackerrank"
    for _ in s:
        if k != "":
            if _ == k[0]:
                f1 = f1 + _
                k = k[1:]
    if f1 == f:
        return "YES"
    else:
        return "NO"
