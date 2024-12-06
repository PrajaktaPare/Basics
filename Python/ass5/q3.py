import os

def open_file(fname, mode):
    return open(fname, mode)

def write_file(fname):
    with open_file(fname, 'w') as file:
        content = input("Enter content to write to the file: ")
        file.write(content)
        print("Content written successfully!")

def read_file(fname):
    with open_file(fname, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

def append_file(fname):
    with open_file(fname, 'a') as file:
        content = input("Enter content to append to the file: ")
        file.write(content + "\n")
        print("Content appended successfully!")

def rename_file(fname):
    new_name = input("Enter new file name: ")
    os.rename(fname, new_name)
    print(f"File renamed to {new_name}")

def menu():
    print("\nChoose an option:")
    print("1. Write to file")
    print("2. Read from file")
    print("3. Append to file")
    print("4. Rename file")
    print("5. Exit")

if __name__ == "__main__":
    fname = input("Enter the file name: ")
    
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            write_file(fname)
        elif choice == '2':
            read_file(fname)
        elif choice == '3':
            append_file(fname)
        elif choice == '4':
            rename_file(fname)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")
