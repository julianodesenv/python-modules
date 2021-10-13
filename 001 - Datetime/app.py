#https://docs.python.org/2/library/datetime.html
from datetime import datetime, timedelta

# criar data
data = datetime(2021, 10, 12, 14, 10, 20)

#  data e hora atual com formado
print(data.strftime('%d/%m/%Y %H:%M:%S'))

#  converter formato
data = data.strptime('20/04/2019', '%d/%m/%Y')
print(data)

# converter timestamp para date
print(data.timestamp())
data = data.fromtimestamp(data.timestamp())
print(data)

# add dias em datas
data = data.strptime('20/04/2019 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=5, seconds=25)
print(data.strftime('%d/%m/%Y %H:%M:%S'))