#26) Write a Python program to check whether a number is Armstrong number or not.

sum = 0

num = int(input("Enter a number: "))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#27) Write a Python program to print all Armstrong numbers between 1 to n.

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):


    order = len(str(num))


    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)




#28) Write a Python program to print Fibonacci series up to n terms.

# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print n1
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1


#29) Write a Python program to print Pascal triangle upto n rows.



#30) Star pattern programs - Write a Python program to print the given star patterns.