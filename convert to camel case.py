"""
This program uses a function that converts dash/underscore delimited words into camel casing.
The first word within the output is capitalized only if the original word was capitalized,
(known as Upper Camel Case, also often referred to as Pascal case).
The next words are always capitalized.
"""

def to_camel_case(text):
    t = text.replace("_", " ").replace("-", " ") # replace hyphens/underscores with whitespace
    t = t.split() # splits whitespace of the text with a comma/ allows us to manipulate words individually
    if len(text) == 0: # if there is no text, return empty string
        return f''
    return t[0] + ' '.join(t[1:]).title().replace(" ", "") # capitalize 2nd word to last word & remove whitespaces


print(to_camel_case("")) # should print empty string
print(to_camel_case("the_stealth_warrior")) # should print "theStealthWarrior"
print(to_camel_case("The-Stealth-Warrior")) # should print "TheStealthWarrior"
print(to_camel_case("A-B-C")) # should print "ABC"