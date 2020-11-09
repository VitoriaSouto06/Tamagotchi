from bichinhoVirtual import BichinhoVirtual

while True:
    print('\n Bem Vindo ao Tamagotchi')
    n = str(input('Insira um nome para seu Tamagotchi:'))
    bichinho = BichinhoVirtual(n)
    break


while True:
    print('''\n 
1 - Alimentar
2 - Aniversário
3 - Dar Remédio
4 - Trocar Nome
5 - Sair     
    ''')
    opcao = (int(input('Escolha uma das opções acima:\n')))

    if opcao == 1:
        if bichinho.fome >50:
            print(f'\033[1;32m {bichinho.nome} já esta alimentado...\033[m\n')
        else:
            bichinho.alimentar()
            print(f'\033[1;32m{bichinho.nome} foi alimentado\n\033[m')

    if opcao == 2:
        if bichinho.idade >50:
            print(f'\033[1;31m † † † {bichinho.nome} morreu  † † †\033[m\n')

        else:
            bichinho.envelhecer()
            bichinho.adoecer()
            print(f'\033[1;34m\o/ Feliz Aniversario \o/. {bichinho.nome} tem {bichinho.idade} anos.\033[m\n')

    if opcao == 3:
        if bichinho.saude <0:
            print(f'\033[1;31m † † † {bichinho.nome} morreu  † † †\033[m\n')

        else:
            bichinho.remedio()
            print(f'\033[1;93m {bichinho.nome} foi medicado.\033[m\n')

    if opcao == 4:
        n = str(input('Escolha o novo nome:'))
        bichinho.trocarNome(n)
        bichinho.nome

    if opcao == 5:
        exit()
