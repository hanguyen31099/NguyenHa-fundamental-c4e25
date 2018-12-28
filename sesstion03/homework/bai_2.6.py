size = [ 5 ,7,300 , 90 ,24,50,75]

print("Hello , my name is hiep and these are my sheep size :")
print(size)

n= int(input("Enter the number of Month, You want to know size of my flock "))
for i in range(n):
    print("MONTH",i+1,":")
    for j in range(len(size)):
        size[j]+=50  
    print("One month has passed, now here in my flock")
    print(size)
    print("Now my biggest ship has size",max(size)-50,"let's chear it")
    k=max(size)
    h=0
    for i in range(len(size)):
        if size[i] == k:
            size[i] = 8
            h=i
    size[h]+=50
    print("After here in my flock :")
    print(size)
  
sum =0
for i in range(len(size)):
    sum+=size[i]
print("My flock is total",sum)
money = sum * 2
print("I would get",sum ,"* 2$ =",money,"$" )    


