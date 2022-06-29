palavra = list(input('\033[32mDigite a palavra secreta: \033[m').strip().lower())
print('\n' * 100)
palpites = []
erro = 0
acerto = 0

while True:
    if erro >= 1:
        print('\033[31m__________')
        print('|        |')
        print('|        O')
    if erro >= 2:
        print('|       /', end='')
    if erro >= 3:
        print('|', end='')
    if erro >= 4:
        print('\\')
    if erro >= 5:
        print('|        |')
    if erro >= 6:
        print('|       / ', end='')
    if erro == 7:
        print('\\')
        print()
        print('ENFORCADO!!!\033[m')
        break

    print()

    for i in palavra:
        if i in palpites:
            print(f'\033[34m{i}\033[m', end='')
        else:
            print('\033[33m_\033[m', end='')
    print()

    if acerto == len(palavra):
        print('\033[35mVocê acertou!!! Parabéns!!!\033[m')
        break

    while True:
        tentativa = input('\033[32mQual é o seu palpite? \033[m').strip().lower()
        if len(tentativa) > 1:
            print('\033[31mVocê só pode tentar uma letra por vez!\033[m')
            continue
        else:
            break
    if tentativa not in palavra:
        print('\033[31mVocê não acertou desta vez! Tente mais uma vez...\033[m')
        erro += 1
    elif tentativa in palpites:
        print('\033[31mVocê já tentou essa! Tente outra...\033[m')
        continue
    else:
        palpites.append(tentativa)
        acerto += 1
