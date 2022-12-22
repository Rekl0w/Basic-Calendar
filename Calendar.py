import calendar
   
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
dd = int(input("Enter day: "))

def print_weekday(year , month , day):
    print("Weekday")
    print(calendar.weekday(year , month , day))

print_weekday(yy,mm,dd)