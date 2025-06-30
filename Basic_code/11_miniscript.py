# A simple text-based adventure game

def start_adventure():
    print("Welcome to the Adventure Game!")
    print("You find yourself at a crossroad. Where do you want to go?")
    print("1. Left")
    print("2. Right")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        print("You walk down a dark path and find a treasure chest!")
        print("Congratulations, you found the treasure!")
    elif choice == "2":
        print("You walk into a forest and encounter a wild bear!")
        print("Oh no, the bear chases you away. Better luck next time!")
    else:
        print("Invalid choice. The adventure ends here.")

if __name__ == "__main__":
    start_adventure()