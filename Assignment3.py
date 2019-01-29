#11. Write a Python program to find first and last digit of a number.
def firstDigit(n):
    while n >= 10:
        n = n / 10;
    return int(n)

def lastDigit(n):
    return (n % 10)


n=int(input("Enter the number:"))
print "First Digit :%d"%(firstDigit(n))
print "Last Digit :%d"%(lastDigit(n))



#12. Write a Python program to find sum of first and last digit of a number.

def firstDigit(n):
    while n >= 10:
        n = n / 10;
    return int(n)

def lastDigit(n):
    return (n % 10)


n=int(input("Enter the number:"))
print "Sum of first and last digit is :%d"%(firstDigit(n)+lastDigit(n))

#13. Write a Python program to swap first and last digits of a number.
n=str(input("Enter the number"))
print n[-1:] + n[1:-1] + n[:1] if n[1:-1] else n[::-1]


#14. Write a Python program to calculate sum of digits of a number.

Number = int(input("Please Enter any Number: "))
Sum = 0
while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number /10
print("\n Sum of the digits of Given Number = %d" % Sum)


#15. Write a Python program to calculate product of digits of a number.
Number = str(input("Please Enter any Number: "))
l= str(Number)
ls= list(Number)
product = 1
for i in l:
    product = product * int(i)
print product
