print("TO DO LIST\n")

class Queue(object):
    def __init__(self):
        self.storage = []

    def enqueue(self, new_element):
        self.storage.append([new_element])

    def display_all(self):
        return self.storage

    def display_one(self):
        return self.storage[-1]

    def dequeue(self):
        return self.storage.pop(0)

    def delete_all(self):
        return self.storage.clear()

    def append(self):
        add = str(input("Add: "))
        self.storage.append([add])

q = Queue()
q.enqueue("Breakfast")
q.enqueue("Go to work")
q.enqueue("Lunch")

print(q.display_all())

drink_coffee = "Drink Coffee"
buy_chocolate = "Buy Chocolate"
drink_milk_tea = "Drink Milk Tea"
go_to_run = "Go To Run"
clear_list = "Empty the list"
show_list = "Check your list"
add_own_item = "Add your Own Item"

print("")
print("0: " + show_list)
print("1: " + drink_coffee)
print("2: " + buy_chocolate)
print("3: " + drink_milk_tea)
print("4: " + go_to_run)
print("5: " + clear_list)
print("9: " + add_own_item)

while True:
    choice = int(input("\nChoose one thing to add to the 'to do list': "))
    if choice == 1:
        q.enqueue(drink_coffee)
        print(f"{q.display_one()}, Added to the list.")
    elif choice == 2:
        q.enqueue(buy_chocolate)
        print(f"{q.display_one()}, Added to the list.")
    elif choice == 3:
        q.enqueue(drink_milk_tea)
        print(f"{q.display_one()}, Added to the list.")
    elif choice == 4:
        q.enqueue(go_to_run)
        print(f"{q.display_one()}, Added to the list.")
    elif choice == 5:
        q.delete_all()
    elif choice == 0:
        print(q.display_all())
    elif choice == 9:
        q.append()