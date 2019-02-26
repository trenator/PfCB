file_name = "curiosity_shop.txt"
input_file = open(file_name)
Long_Sentence = input_file.read().rstrip("\n")
#print(Long_Sentence)

first_sentence_length = Long_Sentence.find(".")+1

first_sentence = (Long_Sentence[:first_sentence_length])
second_sentence = (Long_Sentence[first_sentence_length+1:])

#print(first_sentence)
#print(second_sentence)
first_sentence_file = open("first_sentence.txt", "w")
first_sentence_file.write(first_sentence)
first_sentence_file.close()

second_sentence_file = open("second_sentence.txt", "w")
second_sentence_file.write(second_sentence)
second_sentence_file.close()






