
power_of_two = int(input("Enter the number to get power of two "))

print("i   2 ^ i")
if (0<= power_of_two < 31):
    for i in range(power_of_two): # Iterating till the entered range.
        print(i,"   ",pow(2,i))
else:
    print("Enter the proper range")
