yes = 'yes'
while(yes == 'yes'):
    print("Enter two integers: ")
    x, y = map(int, input().split())
    print(x+y)
    yes = input("Would you like to perform the operation again?: ")
    
