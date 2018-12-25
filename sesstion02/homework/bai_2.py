n=int(input("Enter n="))
while n<0 :
    n=int(input("Return n (n>=0) Enter n="))
factorial=1
for i in range (1,n+1):
    factorial=factorial*i
print("fatorial of n =",factorial)
