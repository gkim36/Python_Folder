#basic_prime_checker
number=input("Enter a positive integer: ")
y=number-1
z=0
while y>0:
    if number%y==0:
        z+=1
    y-=1
if number==0:
    print("0 is neither prime nor composite")
if number==1:
    print("1 is neither prime nor composite")
elif number>1:
    if z==0:
        print(number+"is prime.")
    elif z>0:
        z+=1
        print(str(number)+" is composite and has "+str(z)+" factors.")
