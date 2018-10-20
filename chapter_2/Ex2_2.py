# swapping letters
# sentence = "emong othar public buildings in e cartein town, which for meny raesons it will ba prudant to rafrein from mantioning, end to which i will essign no fictitious nema, thara is ona enciantly common to most towns, graet or smell: to wit, e workhousa; end in this workhousa wes born; on e dey end deta which i naad not troubla mysalf to rapaet, inesmuch es it cen ba of no possibla consaquanca to tha raedar, in this stega of tha businass et ell avants; tha itam of mortelity whosa nema is prafixad to tha haed of this cheptar."
# print(sentence)
#
# replace_one = sentence.replace('a', 'E')
# replace_two = replace_one.replace('e', 'A')
# print(replace_two.lower())

# sentence lengths - find length of EACH sentence
sentence = "Night is generally my time for walking. In the summer I often leave home early in the morning, and roam about fields and lanes all day, or even escape for days or weeks together; but, saving in the country, I seldom go out until after dark, though, Heaven be thanked, I love its light and feel the cheerfulness it sheds upon the earth, as much as any creature living."
full_length = len(sentence)
first_sentence = sentence.find(".")+1
second_sentence = (full_length - first_sentence)
print(full_length, first_sentence, second_sentence)

