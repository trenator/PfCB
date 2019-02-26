file_name = "works.csv"
file = open(file_name)
table = file.read()
#print(table)
new_table1 = table.replace("_", " ")
new_table2 = new_table1.replace("NOVEL", "novel")
#print(new_table2)

new_works_file = open("new_works.csv", "w")
new_works_file.write(new_table2)
new_works_file.close()
