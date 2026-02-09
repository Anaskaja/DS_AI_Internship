Filename=input("Enter the filename to open: ")
try:
    with open( Filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{Filename}' is missing. Please check the filename and try again.")