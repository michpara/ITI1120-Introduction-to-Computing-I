#Exercise 1
def is_eligible(age, citizenship, prison):
     '''(integer, string, string) -> (boolean)
     returns True if someone is 18 or over, a canadian citizen and has never been to prison'''
     if age >=18 and citizenship.lower().strip() in ['canadian', 'canada'] and prison.lower().strip() == 'no':
          return True
     else:
          return False
     
name=input("What is your name? ")
age= int(input("How old are you? "))
citizenship = input("What is your citizenship? ")
prison = input("Have you ever been to prison?: ")

if is_eligible(age, citizenship, prison):
     print(name, ", you are eligible to vote")
else:
     print(name, ", you are ineligible to vote")

#Exercise 2
def mess(phrase):
     '''(string) -> (string)
     capitalizes anything in (r, s, t, v, w, x, y, z) and add a '-' when there is a whitespace'''
    acc = ''
    for i in phrase:
        if i in ('r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
            acc += i.upper()
        elif i == ' ':
            acc += '-'
        else:
            acc += i
    return acc
