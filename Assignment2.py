#6.Write a Python program to find sum of all natural numbers between 1 to n.

Number=int(raw_input("enter no"))
SumN=(Number*(Number+1)/2)
print SumN


#7.Write a Python program to find sum of all even numbers between 1 to n.
n=int(input('Enter the number:'))

print sum(range(2,n+1,2))


#8.Write a Python program to find sum of all odd numbers between 1 to n.
n=int(input('Enter the number:'))

print sum(range(1,n+1,2))

#9.Write a Python program to print multiplication table of any number.
num=12
n=int(input('Enter the number'))
for i in range(1, 11):
    print num,'x',i,'=',num*i

#10.Write a Python program to count number of digits in a number.

n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print "The number of digits in the number are:",count



