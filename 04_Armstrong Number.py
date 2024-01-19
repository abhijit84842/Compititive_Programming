i=int(input("Enter the number : "))
orginal=i
sum=0
while(i>0):
    sum =sum+(i%10)*(i%10)*(i%10)
    i=i//10

if (orginal==sum):
    print("Number is Amstrong")
else:
    print("Number is not Amstrong..")
