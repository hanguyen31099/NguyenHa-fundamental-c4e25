n=int(input("Enter a number: "))
while n<0 :
    n=int(input("Return n (n>0) Enter n="))
for i in range(1,n+1):
    if i % 2 ==0:
        print(" *",end='')
    else:
        print(" x",end='')
