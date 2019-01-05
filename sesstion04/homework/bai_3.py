result=[36,40,41,44]
loop=True
while loop:
    print("If x = 8, then what is the value of 4(x+3)? ")
    no=1
    for i in result:
        print(no, i, sep=". ")
        no+=1
    ques=int(input("Your choice: "))
    if ques == 4:
        print("Bingo")
        loop=False
    else:
        loop=True

