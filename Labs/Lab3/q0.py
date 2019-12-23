
#Part 1
def info_day(today, weather, temperature):
    '''(string, string, number) -> (string)
    prints the weather'''
    print(today, "is a", weather, "day. The temperature is", temperature, "degrees Celsius.")
    s = today + " is a " + weather + " day. The temperature is " + str(temperature) + " degrees Celsius."
    print(s)

#Part 2
def letter_grade(grade):
    '''(string)-> (string)
    prints the letter grade'''
    print("Your grade is", grade)

#Part 3
def average_of_two(num1, num2):
    '''(number, number) -> (float)
    returns the average of two numbers'''
    return (num1 + num2)/2

#Exercise 1
def pay(hourly, hours):
     '''(int,int) -> (number)
     preconditons: hourly & hours > 0
     return wage for employee given hourly rate and hours worked.
     '''
     if hours <= 40:
          wage = hours * hourly
     elif 40 < hours <= 60:
          wage = hourly * (40 + (hours - 40)*1.5)
     else:
          wage = hourly * (40 + 20 * 1.5 + (hours - 60) * 2)
     return wage

#Exercise 2:
def rps(p1,p2):
    '''(string, string) -> (integer)
    returns 1 if p2 wins, -1 if p1 wins and 0 if it's a tie'''
    if(p1 == 'R'):
        if(p2 == 'P'):
            return 1
        if(p2 == 'S'):
            return -1
        else:
            return 0

    if(p1 == 'P'):
        if(p2 == 'S'):
            return 1
        if(p2 == 'R'):
            return -1
        else:
            return 0

    if(p1 == 'S'):
        if(p2 =='R'):
            return 1
        if(p2 == 'P'):
            return -1
        else:
            return 0
