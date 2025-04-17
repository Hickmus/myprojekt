import random 

x = random.randint(1, 100)
y = random.randint(1, 100)
print(x)
print(y)
# Compare this snippet from style.py:
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")