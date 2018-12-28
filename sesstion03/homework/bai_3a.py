from random import randint
word_list =("champion")
letter=list(word_list)
for i in range(len(letter)):
    b = randint(0,len(letter)-1)
    sinle_word=letter[b]
    print(sinle_word,end=" ")
    letter.pop(b)
print()
n= input("Your answer:")
while True:
    
    if n=="champion":
        print("Hura")
    else:
        print(":(")