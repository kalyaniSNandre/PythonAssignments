#16. Write a Python program to enter a number and print its reverse.
Number = int(input("Please Enter any Number: "))
Reverse = 0
while (Number > 0):
    Reminder = Number % 10
    Reverse = (Reverse * 10) + Reminder
    Number = Number // 10

print("\n Reverse of entered number is = %d" % Reverse)

#17. Write a Python program to check whether a number is palindrome or not.

Number = int(input("Please Enter any Number: "))
Reverse = 0
while (Number > 0):
    Reminder = Number % 10
    Reverse = (Reverse * 10) + Reminder
    Number = Number // 10

if Number == Reverse:
    print "Number is palindrome"

#18. Write a Python program to find frequency of each digit in a given integer.

def frequencyDigits(n, d):

    c = 0;

    while (n > 0):

        if (n % 10 == d):
            c += 1;

        n = int(n / 10);

    return c;


N=int(input("Enter Number"))
D=int(input("Enter Number You want calculate frequency"))

print(frequencyDigits(N, D));


#19. Write a Python program to find power of a each number using for loop.
number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
power = 1

for i in range(1, exponent + 1):
    power = power * number

print("The Result of {0} Power {1} = {2}".format(number, exponent, power))

#20. Write a Python program to print all ASCII character with their values.

for i in range(1, 255):
    ch = chr(i);
    print(i, "=", ch);