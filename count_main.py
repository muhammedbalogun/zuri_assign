# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        # read the file
         lines = f.read()

         # convert the character in line to lowercase to avoid missmatch
         lines = lines.lower()

         # remove the puntution mark from the text
         lines = lines.translate(str.maketrans('', '', string.punctuation))
    
    return lines


def count_words():
    text = read_file_content("./story.txt")
    words = text.split()
    # [assignment] Add your code here

# create an empty dictionary
word_count = {}
    for word in words:

        # confirm if word is already in the dictionary
        if word in word_count:
            word_count[word] = word_count[word] + 1

        # if words is not in the dic, add to it
        else:
            word_count[word] = 1

    return word_count

count_words()