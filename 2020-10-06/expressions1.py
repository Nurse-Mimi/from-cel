import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))
print(is_allowed_specific_char("erthjkk876543#$%^^$&"))
print(is_allowed_specific_char("1234567890"))
print(is_allowed_specific_char("asdfhkiu"))