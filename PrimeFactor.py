import math as m

Num = int(input("Enter the number to find it's prime factors : "))

print(f"Prime factors of the given number {Num} are")

# Even number divisible
while (Num % 2 == 0):
    print(2)
    Num = Num/2

# number become odd
for i in range(3, int(m.sqrt(Num))+1,2):

    while (Num % i == 0):
        print(i)
        Num = Num/ i

if Num > 2:
    print(Num)
