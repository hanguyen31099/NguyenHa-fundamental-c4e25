
ques = [
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
]
total=0
for i in range(len(quiz)):
    print(quiz[i]["question"])
    for index,item in enumerate(quiz[i]["answer"]):
        print(index+1,item,sep=". ")
    guest=int(input("you choise :"))-1
    if quiz[i]["answer"][guest] == quiz[i]["correct"]:
        print("bingo")
        total+=1
    else :
        print(":(")
print("Your correctly answer", total, "out of 2 questions")
