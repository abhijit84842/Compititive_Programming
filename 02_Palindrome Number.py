i=int(input("enter the number : "))
rev=0
x=i
while (i>0):
    rev=(rev * 10) + i%10
    i =i//10
if(rev==x):
    print("Palindrome number")
else:
    print("Not Palindrome")