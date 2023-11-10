user_input = input("Введите строку: ")
result = ""
for char in user_input:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char
print(result)
