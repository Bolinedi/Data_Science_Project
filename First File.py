while True:
    name = input("Enter your name: ")
    total = 0
    while True:
        print("Enter the Amount and Quantity")
        amount = float(input("Enter the amount: "))
        quantity = float(input("Enter the quantity: "))
        total += amount*quantity
        repeat = input("Do you want to repeat? (Y/N): ")
        if repeat == "N" or repeat == "n":
            break
    print("-" *40)
    print("Name:", name)
    print("Amount to be Paid:", total)
    print("-" *40)
    print("***** HAPPY SHOPPING *****")
    repeat1 = input("Do you want to continue to next customer (Y/N): ")
    if repeat1 == "N" or repeat1 == "n":
        break