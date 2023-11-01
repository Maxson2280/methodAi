# task 8
import re

regex = r'\b\d{2}\.\d{2}\.\d{4}\b'
dates = ["12.03.2016", "02.05.1928", "12/03/2016", "12-03-2016", "2016.03.12", "2016 03 12", "5.3.2016"]

for date in dates:
    if re.search(regex, date):
        print(f"{date} - корректная дата")
    else:
        print(f"{date} - некорректная дата")
