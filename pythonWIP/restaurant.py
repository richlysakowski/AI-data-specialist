

foods = ["Pizza", "Burger", "Pasta", "Sandwich", "French Fries"]
prices = [7, 5.5, 6, 3.5, 2.5]

total_cost = 0
total_Pizza = 0
total_Burger = 0
total_Pasta = 0
total_Sandwich = 0
total_French_Fries = 0

print("\n\nSelect from the next menu:\n\n")
for i in range(len(foods)):
  print("\t\t{}. {} costs {}".format(i+1, foods[i], prices[i]))
print ()
print ()

choice =int(input("Please choose from the menu or type 0 to finish the order:"))
while choice != 0:
  choice = int(input ("Enter your choice: "))  
  if choice not in range(0,6):
    print("Invalid choice")
    continue
  else:
    total_cost += prices[choice-1]
    if foods[choice-1] == "Pizza":
      total_Pizza += 1
    elif foods[choice-1] == "Burger":
      total_Burger += 1
    elif foods[choice-1] == "Pasta":
      total_Pasta += 1
    elif foods[choice-1] == "Sandwich":
      total_Sandwich += 1
    elif foods[choice-1] == "French Fries":
      total_French_Fries += 1

if total_Pizza > 0:
    print("Total Pizza: ", total_Pizza)
if total_Burger > 0:
    print("Total Burger: ", total_Burger)
if total_Pasta > 0:
    print("Total Pasta: ", total_Pasta)
if total_Sandwich > 0:
    print("Total Sandwich: ", total_Sandwich) 
if total_French_Fries > 0:
    print("Total French Fries: ", total_French_Fries)
        
print("Total cost is: ", total_cost)