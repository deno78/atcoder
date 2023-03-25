abc = input('').split()
a=int(abc[0])
b=int(abc[1])
c=int(abc[2])

print(max(c-(a-b),0))

# 容器Aに入る量はa-b
# 容器Bに入っている量はc
# なので、 c - (a-b) で、Bに残る量が分かる。
# ただし、a-bが十分に大きい場合、cがマイナスになることはないので、
# 0 or c-(a-b) の大きい方、になる
