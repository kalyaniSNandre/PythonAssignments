#26) Write a Python program to check whether a number is Armstrong number or not.
from macpath import sep

import end as end

sum = 0

num = int(input("Enter a number: "))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10


if num == sum:
   print num,"is an Armstrong number"
else:
   print num,"is not an Armstrong number"

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

nterms = 10

n1 = 0
n2 = 1
count = 0

if nterms <= 0:
   print "Please enter a positive integer"
elif nterms == 1:
   print "Fibonacci sequence upto", nterms, ":"
   print(n1)
else:
   print "Fibonacci sequence upto", nterms, ":"
   while count < nterms:
       print n1
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1


#29) Write a Python program to print Pascal triangle upto n rows.
n = int(input("Enter number of rows"))
a = []
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
        if n!=0:
            a[i].append(1)

for i in range(n):
        print "" *(n-i),end,sep
        for j in range(0,i+1):
            print '{0,6}'.format(a[i][j]), end, sep
            print

#30) Star pattern programs - Write a Python program to print the given star patterns.
i = 0
while i <= 3:
    j = 3
    while j >= 0:
        print '*'*(2*j)
        j = j-1
    i = i+1


