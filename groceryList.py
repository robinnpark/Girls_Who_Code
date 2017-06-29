groceryList = ["eggs", "milk", "fruits", "bread", "cereal"]

while True:
    print("Do you want to add an item to your list? (y/n)")
    answer = input()


    if answer == 'y':
        print("What would you like to add to your list?")
        addedItem = input()
        groceryList.append(addedItem)
        length = len(groceryList)
    print("Okay! Your grocery list is")

    for x in groceryList:
           print(x)
            
    if answer == 'n':
        #print("Okay! Your grocery list is")
        for x in groceryList:
            print(x)
        break
  
