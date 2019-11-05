s = str(input('Введите слово '))
for number in range(1, len(s), 2):
    if (s[number] != 'п')and(s[number] != 'и')and(s[number] != 'о'):
        print(s[number])
for number in range(0, len(s), 2):
    if (s[number] != 'п')and(s[number] != 'и')and(s[number] != 'о'):
        print(s[number])
input()
