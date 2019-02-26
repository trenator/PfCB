# my_file_name = "first_line.txt"
# my_file: TextIO = open(my_file_name)
# my_file_contents = my_file.read()

# open the file
my_file = open("first_line.txt")

# read the contents
# sentence = my_file.read()
# remove the newline from the end of the file contents
sentence = my_file.read().rstrip("\n") # 2 steps in 1

# calculate the length
length = len(sentence)

# print the output
print("sentence is "+ sentence+" and length is " + str(length))
