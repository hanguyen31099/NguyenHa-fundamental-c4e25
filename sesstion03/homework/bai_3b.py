from random import randint
word_list =("champion","meticulous","hexagon")
k = randint(0,len(word_list)-1)
letter=list(word_list[k])
for i in range(len(letter)):
    b = randint(0,len(letter)-1)
    sinle_word=letter[b]
    print(sinle_word,end=" ")
    letter.pop(b)
print()
while True:
    n = input("Your answer: ")
    if n == word_list[k]:
        print("Hura")
        break
    else:
        print(":(")
