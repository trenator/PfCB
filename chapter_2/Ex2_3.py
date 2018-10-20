# place names
# place name, part one -> extract from 19th to 28th character
# sentence = "Thirty years ago, Marseilles lay burning in the sun, one day."
# print(sentence[18:28])

# # place name, part two -> calc percent of the sentence made up of the name f the city.
# sentence = "Thirty years ago, Marseilles lay burning in the sun, one day."
# percent = 100*(len(sentence[18:28]) / len(sentence))
# print(percent)

# place name, part three -> write program that will print original sentence with with city name in uppercase
sentence = "Thirty years ago, Marseilles lay burning in the sun, one day."
print(sentence)

city = sentence[18:28]
new_sentence = sentence.replace(city, city.upper())
print(new_sentence)