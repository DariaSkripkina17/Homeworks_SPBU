#Используя наборы символов из пакета string написать функцию,
# которая получает на вход строку и возвращает строку,
# в которой все буквы латинского алфавита из исходной строки преобразованы в заглавные символы.
# Использовать функции стандартной библиотеки upper() и find() нельзя.
#Добавить к предыдущему заданию функцию с преобразованием всех символов в прописные
# и функцию с отражением (все заглавные становятся прописными и наоборот), минимально дублируя код.
# Использовать функции стандартной библиотеки lower() и find() нельзя.
import string
def up(word, case = string.ascii_lowercase):#word необходимо преобразовать в верхний регистр, а case определяет символы которые строчные
    result = ''
    for letter in word: #цикл перебирает каждый символ в слове и проверяет находится ли он в case
        result += letter.swapcase() if letter in case else letter
    return result
def down(word):
    return up(word, string.ascii_uppercase)

def mirr(word):
    return up(word, string.ascii_letters)

str = input()
print(up(str), down(str), mirr(str), sep='\n')