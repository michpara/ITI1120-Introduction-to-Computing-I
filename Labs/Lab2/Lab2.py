#Exercise 1
import math
def repeater(s1, s2, n):
    '''(string, string, integer) -> (string)
    returns s1 + s2, n times, with a trailing _ at the beginning and end'''
    trailing = "_"
    answer = trailing + n*(s1 + s2) + trailing
    return answer

#Exercise 2
def roots(a, b, c):
    '''(number, number, number) -> (float)
    presumptions : a is a non zero number, a, b and c are such that b**2-4ac is a positive number
    returns the positive and negative roots of ax**2+bx+c'''
    positiveX, negativeX = (-b+math.sqrt(b**2-(4*a*c)))/2*a, (-b-math.sqrt(b**2-(4*a*c)))/2*a
    print(f'''The quadratic equation with coefficients a = {a}, b = {b}, c = {c}
has the following solutions (i.e. roots):
{positiveX} and {negativeX}''')

#Exercise 3
def real_roots(a, b, c):
    '''(number, number, number) -> (bool)
    returns true if b**2-(4*a*c) is positive and false otherwise'''
    return (b**2-(4*a*c)) == abs(b**2-(4*a*c))

#Exercise 4
def reverse(x):
    '''(integer) -> (integer)
    presumptions : x is a two digit positive integer
    reverses x'''
    firstDigit = x//10
    secondDigit = x%10
    return secondDigit*10 + firstDigit
