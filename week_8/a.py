from datetime import datetime, timedelta


date_1 = input()
date_2 = input()

d1 = datetime.strptime(date_1, "%Y-%m-%d")
d2 = datetime.strptime(date_2, "%Y-%m-%d")

result = d2 - d1 + timedelta( days=3)

print(abs(result.days))