prices = {
    "banana": 4 ,
    "apple" : 2 ,
    "orange": 1.5 ,
    "peal" : 3 ,
}
stock ={
    "banana": 6 ,
    "apple" : 0 ,
    "orange": 32 ,
    "peal" : 15 ,
}

total = 0
for fruit in prices:
    print(fruit)
    print("princes",prices[fruit])
    print("stock",stock[fruit])
    total+=prices[fruit]*stock[fruit]
    print()
print("total :",total)
