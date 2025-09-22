###Create a file. Set text into file with numbers and words. Read numbers from the file and calculate the sum of them###
#f = open("PythonCore.txt", "x") - created file first
with open("PythonCore.txt", "w") as f:
    f.write("I`ve read 5 books, 3 articles and listened to 1 podcast")
with open("PythonCore.txt") as f:
    text = f.read()
    print(text)

numbers = [int(x) for x in text.split() if x.isdigit()]
sum_numbers = sum(numbers)
print(sum_numbers)

# -----------------------------------------------------------------------------------------------------------------------#

###Find the longest word in the file###
with open("PythonCore.txt") as f:
    text = f.read()
    print(text)
words = text.split()
print(words)
long_word = max(words, key=len)
print(long_word, len(long_word))

# -----------------------------------------------------------------------------------------------------------------------#

###Close the file using function and using context manager###
f = open("PythonCore.txt", "r") #using function
text = f.read()
print(text)
f.close()

with open("PythonCore.txt", "r") as f: #using contex manager(auto closing)
    text = f.read()
    print(text)

# -----------------------------------------------------------------------------------------------------------------------#

with open("Python_love.txt", "w") as f:
    f.write("This tutorial introduces the reader informally to the basic concepts and features of the Python language and system\n")
    f.write("Be aware that it expects you to have a basic understanding of programming in general.\n")
    f.write("It helps to have a Python interpreter handy for hands-on experience,\n")
    f.write("but all examples are self-contained, so the tutorial can be read off-line as well.\n")
with open("Python_love.txt", "r") as f: #print the result
    text = f.read()
    print(text)

with open("Python_love.txt", "r") as source: #read all lines to the list
    lines = source.readlines()

copy_lines = lines[1:-1] #exclude 1st and last line
with open("Python_love_copy.txt", "w") as target: #write the lines to the new file
    target.writelines(copy_lines)

with open("Python_love_copy.txt", "r") as f: #print the result
    text = f.read()
    print(text)

# -----------------------------------------------------------------------------------------------------------------------#

with open("Python_love.txt", "r") as f1, open ("Python_love_copy.txt", "r") as f2, open("combo_text.txt", "w") as out:
    for l1, l2 in zip(f1, f2):
        combo_text = l1.strip() + "" + l2.strip() + "\n"
        out.write(combo_text)
        print(combo_text, end="")