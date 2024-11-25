# Assignment 1
file = open("myFile.txt", "r")
content = file.read()
print("Original Content: ")
print(content)


newFile = open("newfile.txt", "w")
modified_content = content + "/nThis is to add new content to the file."
newFile.write(modified_content)
print("content successfully written to 'newfile.txt'")

#Assignment 2
try:
    file = open("myfile.text", "r")
except FileNotFoundError:
    print("This file is not found")
finally:
    print("Thanks for joining us")