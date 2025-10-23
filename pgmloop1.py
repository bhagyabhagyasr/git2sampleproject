# Print all numbers divisible by 5 but not by 10, between 1 and 100.


i = 1
while i <= 100:
    if i % 5 == 0 and i % 10 != 0:
        print("add",i)
    i=i+1
