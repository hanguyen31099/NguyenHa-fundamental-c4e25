sentence = list(input("write a sentence:"))
letter_counts = {}
for letter in sentence:
    if letter !=" ":
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
letter_items = list(letter_counts.items())
letter_items.sort()
for char,count in letter_items:
      print(char,count)