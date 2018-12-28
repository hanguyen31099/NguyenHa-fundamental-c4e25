items = [ "t-shirt","Sweater"]
while True:
    n= input("welcome to our shop , what do you want ( C , R , U , D )?")
    k=n.upper()
    while k!="C" and k!="R" and k!="U" and k!="D" :
        n=input("Enter again, These isn't have in my shop:")
        k=n.upper()
    if k=="C":
        y=str(input("create new item : "))
        items.append(y)
        for i in range(len(items)):
            if i==(len(items)-1):
                print(items[i])
            else:
                print(items[i],", ",end='')
    elif  k=="R":
        for i in range(len(items)):
            if i==(len(items)-1):
                print(items[i])
            else:
                print(items[i],", ",end='')
    elif k=="U":
        x = int(input("Update position ?"))
        y = str(input(" new item ? "))
        items[x-1]= y
        for i in range(len(items)):
            if i==(len(items)-1):
                print(items[i])
            else:
                print(items[i],", ",end='')
    elif k=="D":
        z = int(input(" delete position ? "))
        items.pop(z-1)
        for i in range(len(items)):
            if i==(len(items)-1):
                print(items[i])
            else:
                print(items[i],", ",end='')
