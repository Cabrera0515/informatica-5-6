from datetime import datetime
day = datetime.now() .weekday()

days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
print(days[day])

months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print("these are the summer months:")
print(months[5])
print(months[6])
print(months[7])

month = 11 - months
print("It is", months[month-1])



print("what day is it")
day = int(input())
if day <= 4:
    print("It's a weekday")
    remaining = 5 - day
    print(remaining, "days until the weekend")
elif day == 4:
    print("It's Friday")
    print("Just a day left until the weekend")
else:
    print("It's the weekend!")
