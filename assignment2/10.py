from datetime import date
from datetime import datetime

# today = date.today()
# # print("Today's date:", today)

# d = today.strftime("%d-%m-%Y")
# print("Today's date : ", d)

now = datetime.now()

t = now.strftime("%d-%m-%Y %H:%M%p")
print("date and time = ",t)