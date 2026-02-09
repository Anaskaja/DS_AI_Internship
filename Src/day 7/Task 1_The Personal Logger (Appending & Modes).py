name = input("Enter your name: ")
goal = input("What is your goal for today? ")
with open("journal.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Goal: {goal}\n")
print("Your entry has been added to the journal.")