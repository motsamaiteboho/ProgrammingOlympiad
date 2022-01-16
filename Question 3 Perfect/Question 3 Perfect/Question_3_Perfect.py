import math
Number = int(input("Positive integer: "))

Perfect = []

for i in range(1,Number):
    if Number % i == 0:
        Perfect.append(i)

if math.fsum(Perfect) > Number:
    print("abundreant")
elif math.fsum(Perfect) < Number:
    print("deficient")
else:
    print("Perfect")
    