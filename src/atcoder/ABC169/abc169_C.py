import decimal
ab = input('')
a = decimal.Decimal(ab.split(' ')[0])
b = decimal.Decimal(ab.split(' ')[1])
result =  a*b
import math
result = math.floor(result)
print(result)

