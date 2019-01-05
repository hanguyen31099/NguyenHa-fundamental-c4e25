from random import randint
quiz = [
     {
    "question": "If x = 8, then what is the value of 4(x + 3)?",
    "answer": [35, 36, 40, 44],
    "correct": 44
    },
    {
    "question": "jack scored in 5 math test: 49, 81, 72, 66 and 52. What is this mean",
    "answer": ["About 55", "About 65", "About 75", "About 85"],
    "correct": "About 65"
    }
    , 
    {
    "question": "If x = 8, then what is the value of 5(x + 3)?",
    "answer": [55, 35, 42, 1],
    "correct": 55
    },
    {
    "question": "If x = 8, then what is the value of 10(x + 3)?",
    "answer": [880, 770, 990, 488],
    "correct": 880
    }
]
total=0
result=0
loop=True
while loop:
    result+=1
    if result==len(quiz):
        loop=False
    i=randint(0,len(quiz)-1)
    print(quiz[i]["question"])
    for index,item in enumerate(quiz[i]["answer"]):
        print(index+1,item,sep=". ")
    guest=int(input("you choise :"))-1
    while guest !=0 and guest !=1 and guest !=2 and guest !=3:
        guest=int(input("Enter again you choise it have'nt in my answer:"))-1
    if quiz[i]["answer"][guest] == quiz[i]["correct"]:
        print("bingo")
        total+=1
    else :
        print(":(")

print("Your correctly answer", total, "out of ",result," questions")
