inventory = {
    'gold' : [500],
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocketo']=['seashell', 'strange berry','lint']
del inventory['backpack'][1]
inventory['gold'].append(50)
print(inventory)