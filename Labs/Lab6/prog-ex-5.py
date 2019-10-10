from random import randrange

n = int(input("Enter a positive integer: "))

a = [0]*n
print(a)

b = [None]*n
for i in range(0, n):
      b[i] = randrange(1,101)

c = b[:]

for i in range(0, int(len(c)/2)):
    c[i] = 0

print(b)
print(c)

d = b[:]
print(d)

e = [0]*int(n/2)
j = 1
for i in range(0, int(n/2)):
    e[i] = b[j]
    j+=2
print(e)
