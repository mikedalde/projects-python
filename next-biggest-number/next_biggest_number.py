from itertools import permutations

# Prompt for input
number = input("Number:")

# Conversion Functions
def intasc(string):
    return int("".join(sorted([i for i in str(string)])))

def intdesc(string):
    return int("".join(sorted([i for i in str(string)], reverse=True)))

def intconv(string):
    return int("".join([i for i in string]))

def listconv(int):
    return [i for i in str(int)]

# Logic
if int(number) == intdesc(number):
    print(-1)
else:
    nextnum = ''
    exit = 0
    for i in reversed(number[:-1]):
        digit = number[-1]
        if digit > i and exit == 0:
            nextnum = (str(digit)+str(i))+nextnum
            exit = 1
        else:
            nextnum = str(i)+nextnum

    print("The next largest number is: " + nextnum)