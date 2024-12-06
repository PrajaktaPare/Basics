# Read the content from input.txt
with open('input.txt', 'r') as infile:
    content = infile.read()

# Reverse the content
reversed_content = content[::-1]

# Write the reversed content to reversed.txt
with open('reversed.txt', 'w') as outfile:
    outfile.write(reversed_content)

print("Reversed content has been written to reversed.txt.")
