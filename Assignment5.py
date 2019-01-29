#21)
num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#22) Write a Python program to find HCF (GCD) of two numbers.

def computeHCF(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1, "and", num2, "is", computeHCF(num1, num2))



#23) Write a Python program to find LCM of two numbers.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#24) Write a Python program to check whether a number is Prime number or not.

# Python program to check if the input number is prime or not
num = int(input("Enter a number: "))
if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")


#25) Write a Python program to print all Prime numbers between 1 to n.
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
