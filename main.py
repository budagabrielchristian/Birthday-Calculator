import datetime

year = input("Enter a year: ")
month = input("Enter on what month your birthday is: \n")
day = input("Enter on what day your birthday is: \n")

today = datetime.date.today()
birthday = datetime.date(int(year), int(month), int(day))
till_birthday = birthday-today

equal_dates = today == birthday

if equal_dates:
    print("Your birthday is today! Happy birthday :)")
elif today<=birthday:
    print("Your birthday will be in ",till_birthday.days, " days")
    print("Your birthday is on a ",birthday.strftime("%A"))
elif today > birthday:
    print("Your birthday was ",int(abs(till_birthday.days))," days ago")
    print("Your birthday was on a ",birthday.strftime("%A"))
