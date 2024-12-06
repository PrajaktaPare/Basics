# Ask user for the names of source and destination files
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

# Open the source file and read its content
with open(source_file, 'r') as src:
    content = src.read()

# Open the destination file and write the content
with open(destination_file, 'w') as dest:
    dest.write(content)

print(f"Content from '{source_file}' has been copied to '{destination_file}'.")
