palavras = ('estudar', 'trabalhar', 'viver', 'feliz', 'sobreviver')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
