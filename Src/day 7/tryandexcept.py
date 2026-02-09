try:
    with open("missing.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file is missing. Please check the filename.")
     
     