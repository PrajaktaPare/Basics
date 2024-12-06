# Ask user for the file name
file_name = input("Enter the name of the text file: ")

# Read the content of the file
with open(file_name, 'r') as file:
    content = file.read()

# Convert content to lowercase to count words case-insensitively
content = content.lower()

# Split the content into words
words = content.split()

# Create a dictionary to store word frequencies
word_count = {}

# Count the frequency of each word
for word in words:
    word = word.strip('.,!?")(')  # Remove punctuation marks around words
    if word:
        word_count[word] = word_count.get(word, 0) + 1

# Sort the word frequency dictionary by value in descending order
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Display the word frequencies in descending order
print("\nWord frequencies in descending order:")
for word, count in sorted_word_count:
    print(f"{word}: {count}")
