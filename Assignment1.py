
# 1. Write a Python program to print all natural numbers from 1 to n.
num=int(raw_input("enter natural number"))
i=1
while i<=num:
    print i
    i=i+1


# 2.Write a Python program to print all natural numbers in reverse (from n to 1).

num=int(raw_input("enter natural number"))
i=num
while i>=1:
    print i
    i=i-1

# 3.Write a Python program to print all alphabets from a to z.

for one in range(97, 123):
    print chr(one)


#4.Write a Python program to print all even numbers between 1 to 100.

for even in range(1,100):
    if even%2==0:
        print even

#5.Write a Python program to print all even numbers between 1 to 100.

for odd in range(1,100):
    if odd%2!=0:
        print odd




