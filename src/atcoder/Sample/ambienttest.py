
import ambient

am = ambient.Ambient(41407,"",
"ff3635ccf4d9eeac","ffba70b9b0ec210177")

data=am.read(n=100)
#data=am.read(date='2021-01-01')
#data=am.read(start='2021-01-01 00:00:00',end='2022-01-01 00:00:00')
print(data)