def print_all_23n8(num):
    '''presumptions : non-negative integer num'''
    for i in range(num):
        if((i%2==0 or i%3 ==0) and i%8 != 0):
            print(i)

num = int(input("Enter a non-negative integer: "))
print_all_23n8(num)


def pyramid(num, char):
    for i in range(1, num+1):
        print(i*char)

def divisors(num):
    for i in range(1, num):
        if num%i == 0:
            print(i)

def prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if(num%i ==0):
                return False
        return True
num = int(input("Enter a positive integer :"))
divisors(num)
print("It is", str(prime(num)).lower(), "that the number you chose is prime")
