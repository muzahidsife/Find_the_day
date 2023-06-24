import datetime


datex = input("Enter a date (YYYY-MM-DD): ")

date = datetime.datetime.strptime(datex, '%Y-%m-%d').date()

day = date.strftime('%A')

print("The day on", datex, "is", day)
