inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 

def displayInventory(items):
    print('Inventory:')
    for key in items.keys():
        print(str(items[key]) + ' ' + key)
    print('Total number of items: ' + str(sum(items.values())))
        
        
        
def addToInventory(items, addedItems):
    for value in addedItems:
        if value in items.keys():
            items[value] += 1
        else:
            items.setdefault(value, 1)
    return items

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


inv = addToInventory(inventory, dragonLoot)
displayInventory(inv)
    