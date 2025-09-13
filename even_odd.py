#This program is to print even and odd numbers

print("Here is the program block starts")
i = 3

while i <= 20:
    if i % 2 == 0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")
    i = i + 1
print("Here is the program block ends")