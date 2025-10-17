#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = abs(number) % 10
text = f"Last digit of {number} is {lastnum} and is"

if number < 0:
    print(f"Last digit of {number} is -{lastnum} and is less than 6 and not 0")
elif last > 5:
    print(text, "greater than 5")
elif last == 0:
    print(text, "0")
else:
    print(text, "less than 6 and not 0")
