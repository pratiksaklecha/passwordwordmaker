# random password genereter app
print('Welcome to password genererator\nEnter required length')
length = int(input())

print("if you want upper case then type 1 else 0")
u = int(input())
print("if you want lower case  then 1 else 0")
l = int(input())
print("if you want numbers then type 1 else 0")
n = int(input())
print("if you want punctuations then type 1 else 0")
p = int(input())
import random
import string
# 1 p
if u == 0 and l == 0 and n == 0 and p == 1:
    characters = string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 2
elif u == 1 and l == 0 and n == 0 and p == 0:
    characters = string.ascii_uppercase
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 3
elif u == 0 and l == 1 and n == 0 and p == 0:
    characters = string.ascii_lowercase
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 4
elif u == 0 and l == 0 and n == 1 and p == 0:
    characters = string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 5
elif u == 1 and l == 0 and n == 0 and p == 1:
    characters = string.punctuation+ string.ascii_uppercase
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 6
elif u == 0 and l == 1 and n == 0 and p == 1:
    characters = string.punctuation+ string.ascii_lowercase
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 7
elif u == 0 and l == 0 and n == 1 and p == 1:
    characters = string.punctuation + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 8
elif u == 1 and l == 1 and n == 0 and p == 0:
    characters = string.ascii_uppercase + string.ascii_lowercase
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 9
elif u == 1 and l == 0 and n == 1 and p == 0:
    characters = string.ascii_uppercase + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 10
elif u == 0 and l == 1 and n == 1 and p == 0:
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 11 pul
elif u == 1 and l == 1 and n == 0 and p == 1:
    characters = string.punctuation + string.ascii_lowercase + string.ascii_uppercase
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 12 pud
elif u == 1 and l == 0 and n == 1 and p == 1:
    characters = string.punctuation + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 13 pld
elif u == 0 and l == 1 and n == 1 and p == 1:
    characters = string.punctuation + string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 14 uld
elif u == 1 and l == 1 and n == 1 and p == 0:
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
# 15 0000
elif u == 0 and l == 0 and n == 0 and p == 0:
    print('invalid input')
    print('Please select atleast one type')
# 16 puld
elif u == 1 and l == 1 and n == 1 and p == 1:
    characters = string.punctuation + string.digits + string.ascii_uppercase + string.ascii_lowercase
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)
