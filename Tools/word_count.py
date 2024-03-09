import os
import sys

# Function for establishing path to file
def definePath(pathInput):
    if os.path.exists(pathInput):
        fileInput = input("Enter file name: ")
        path = os.path.join(pathInput, fileInput)
    else:
        print("Error: Directory does not exist.")
        sys.exit()

    print("File to read: ", path, "\n")

    return path


# Reading and counting file content
def wordCount(path):
    try:
        with open(path, "r") as file:
            content = file.read()
    except:
        print("Error: File could not be read.")
        sys.exit()

    line_list = content.splitlines()
    word_list = content.split()

    line_count = str(len(line_list))
    word_count = str(len(word_list))
    char_count = str(len(content))

    output = {
        "lines": line_count,
        "words": word_count,
        "characters": char_count
    }

    return output


# Print a table of the output
def table(output):
    fill = " "
    for x, y in output.items():
        x = x + ": "
        while len(x + y) < 20:
            x += fill
        print("Number of " + x + y)
    print()

# Actions
pathInput = input("Enter file directory: ")
path = definePath(pathInput)
output = wordCount(path)
table(output)





