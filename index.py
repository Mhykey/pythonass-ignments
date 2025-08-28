def modify_file():
    try:
        filename = input("Enter the filename to read: ")

        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        with open("output.txt", "w") as file:
            file.write(modified_content)

        print("Modified file saved as output.txt")

    except FileNotFoundError:
        print("Error: File does not exist.")
    except PermissionError:
        print("Error: No permission to read this file.")
    except Exception as e:
        print("Unexpected error:", e)


modify_file()
