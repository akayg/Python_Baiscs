try:
    nums = [10, 20, 30]
    index = int(input("Enter index (0 to 2): "))
    print("Value:", nums[index])
except (IndexError, ValueError) as e:
    print("Caught Exception:", e)
