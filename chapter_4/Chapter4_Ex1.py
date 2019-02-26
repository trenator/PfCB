file_name = "two_cities.txt"
input_file = open(file_name)
paragraph = input_file.read()
#print(paragraph)

removed_line = "it was the "
new_paragraph = paragraph.replace(removed_line, "")
#print(new_paragraph)
new_file =  open("edited_two_cities.txt", "w")
new_file.write(new_paragraph)
new_file.close()
input_file.close()
new_file.close()

new_file = open("edited_two_cities.txt")
new_para = new_file.read()
print(new_para)
