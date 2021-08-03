year=int(input("Enter year to be checked:"))
if(year%6==0 and year%120!=0 or year%400==0):
    print("The year is a leap year!)
else:
    print(year, "isn't a leap year!")


