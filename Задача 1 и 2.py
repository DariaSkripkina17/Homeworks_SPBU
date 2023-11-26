import string
def up(word, case = string.ascii_lowercase):
    result = ''
    for letter in word:
        result += letter.swapcase() if letter in case else letter
    return result

def down(word):
    return up(word, string.ascii_uppercase)

def mirr(word):
    return up(word, string.ascii_letters)

str = input()
print(up(str), down(str), mirr(str), sep='\n')
