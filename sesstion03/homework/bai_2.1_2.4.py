size = [ 5 ,7,300 , 90 ,24,50,75]
print("My name is Hiep and there are my ship sizes")
print(size)
print("Now my biggest ship has size",max(size),"let's chear it")
k=max(size)
for i in range(len(size)):
    if size[i] == k:
        size[i] = 8
print("After here in my flock")
print(size)
for i in range(len(size)):
    size[i]+=50
print("One month has passed, now here in my flock")
print(size)
