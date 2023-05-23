# Quick practice script to read in a text file, parse the lines and
# look for the word "practice"

# This will be the static version
# Plan to build a dynamic version that can accept text files and
# user input for the word being searched

# Open the text file to be read
practice_txt_file = open("C:/Users/Tristan Kelly/Desktop/practice_txt.txt")

# Create empty variables for the word count and word list
word_count = 0
word_list = []

# Split the lines of the text file, clean the words and put them in a list
for lines in practice_txt_file:
    line = lines.split()
    for words in line:
        word_list.append(words.strip('"').lower())

# Go through the word list looking for 'practice'
for values in word_list:
    if values == 'practice':
        word_count = word_count + 1

# Return word_count
print(f'In the text file there were {word_count} times "practice" appears')