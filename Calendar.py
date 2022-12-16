import calendar
   
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  

def print_full_calendar_from_year(year):
    print("Full Calendar")
    print(calendar.calendar(year))

def print_month_calendar_from_year(year, month):
    print("Month Calendar")
    print(calendar.month(year, month))

def print_month_calendar_from_year_and_weekday(year, month):
    print("Month Calendar with Weekday")
    print(calendar.monthcalendar(year, month))


