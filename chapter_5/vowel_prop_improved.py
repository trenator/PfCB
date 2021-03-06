from __future__ import division

def get_vowel_prop(text):
    a_count = text.lower().count('a')
    e_count = text.lower().count('e')
    i_count = text.lower().count('i')
    o_count = text.lower().count('o')
    u_count = text.lower().count('u')
    prop = (a_count + e_count + i_count + o_count + u_count) / len(text)
    return round(prop, 2)

vowel_prop = get_vowel_prop("abcde")
print(vowel_prop)
print(get_vowel_prop("Great Expectations"))
