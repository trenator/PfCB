file_name = "file_name.txt"
# file_name = input("Enter the input file name\n")
input_file = open(file_name)
input_file_content = input_file.read()
# do something withe the file contents

name = input("What is  your name?\n")
input_file = open("file_name.txt", "a")
input_file.write("Name: "+ name + "\n")
input_file.close()