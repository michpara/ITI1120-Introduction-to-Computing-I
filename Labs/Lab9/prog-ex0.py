def get_year():
    flag = True
    answer = 0
    while(flag):
        year = input("Please enter a 4 digit integer: ")
        if not year.isdigit():
            raise RuntimeError("The number must use digits")

        if int(year)/1000 < 1 or int(year)/1000 > 9.999:
            raise RuntimeError("The number must be 4 digits")

        else:
            answer = int(year)
            flag = False
    return answer
