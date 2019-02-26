file_name = "great_expectations.txt"
control_name = "speech.txt"
input_file = open(file_name)
control_file = open(control_name)

paragraph = input_file.read()
print(paragraph)
control = control_file.read()

new_file_name = "edited_great_expectations.txt"

