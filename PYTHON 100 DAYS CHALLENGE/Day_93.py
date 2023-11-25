# Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions


import re
text = "the cat is playing with rat inside hat"
pattern = "[a-z]+at" # this is just a simple pattern as an example. you can make very complex patterns using regular expressions

match = re.search(pattern,text) # it only gives the first match of pattern from text as an match object.
print(match)


matches = re.findall(pattern,text) # it gives all occurences of pattern in text as a list
print(matches)


pattern2 = "cat"
new_text = re.sub(pattern2,"dog",text) # re.sub() will replace all the patterns inside text with the word provided inside re.sub()
                                       # and store the whole text with replaced pattern inside new_text here
print(new_text)


# Metacharacters in regular expressions
# [] -  Represent a character class
# ^  -  Matches the beginning
# $  -  Matches the end
# .  -  Matches any character except newline
# ?  -  Matches zero or one occurrence.
# |  -  Means OR (Matches with any of the characters
#    -  separated by it.
# *  -  Any number of occurrences (including 0 occurrences)
# +  -  One or more occurrences
# {} -  Indicate number of occurrences of a preceding RE 
#       to match.
# () -  Enclose a group of REs

