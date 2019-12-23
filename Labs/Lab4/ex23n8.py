#Exercise 3
def print_all_23n8(num):
    '''(integer)->(integer)
    presumptions : non-negative integer num
    prints all integer up to num that are divisible by 2 or 3 but not by 8'''
    for i in range(num):
        if((i%2==0 or i%3 ==0) and i%8 != 0):
            print(i)

#Exercise 4
def pyramid(num, char):
    '''(integer, string) -> (string)
    returns a half pyramid of size num using elements char'''
    for i in range(1, num+1):
        print(i*char)

#Exercise 5
def divisors(num):
    '''(integer) - > (integer)
    returns all the divisors of num'''
    for i in range(1, num):
        if num%i == 0:
            print(i)

#Exercise 6
def prime(num):
    '''(integer) -> (boolean)
    returns if num is prime'''
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
