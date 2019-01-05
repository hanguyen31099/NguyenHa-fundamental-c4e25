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
    total+=prices[fruit]*stock[fruit]
print("total :",total)
