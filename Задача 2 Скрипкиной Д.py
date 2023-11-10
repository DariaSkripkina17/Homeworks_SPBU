s = input()
s2 = s.swapcase()#Заглавные буквы станут строчными, а строчные — заглавными: ОТРАЖЕНИЕ
s3 = s.casefold()#этот метод преобразует все символы строки в их нижний регистр
counter = 0
for i in range(len(s)):
    if s[i] != s2[i]:
        counter += 1
print(s2)
print(s3)
