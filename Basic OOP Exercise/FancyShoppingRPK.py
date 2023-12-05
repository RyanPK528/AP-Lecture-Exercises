from ShoppingListRPK import ShoppingRPK

def listObjectsRPK():
    objectList = []
    num_items = int(input("How many items will you order today? "))
    while num_items < 1:
        print("Number of items must be at least 1.")
        num_items = int(input("How many items will you order today? "))

    for i in range(1, num_items + 1):
        print(f"Item #{i}-")
        food_name = input("Enter food: ")
        amount_ordered = float(input("Enter amount of pounds: "))
        while amount_ordered <= 0:
            print("Amount of pounds must be greater than 0.")
            amount_ordered = float(input("Enter amount of pounds: "))

        item = ShoppingRPK(food_name, amount_ordered)
        objectList.append(item)

    return objectList

def displayListRPK(item_list):
    for item in item_list:
        print(item)
        print()

def calculate_total_costRPK(item_list):
    total_cost = sum(item.get_orderPriceRPK() for item in item_list)
    return total_cost

def main():
    items = listObjectsRPK()
    print("\nHere's a summary of the items purchased:")
    displayListRPK(items)
    total_cost = calculate_total_costRPK(items)
    print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()