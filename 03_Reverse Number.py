i=int(input("enter the number : "))
rev=0

while(i>0):
    rev=(rev*10) + i %10
    i=i//10
print(f"Reversed number is {rev}")