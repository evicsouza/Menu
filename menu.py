from time import sleep
opcao = 0
while opcao != 5:
    print('''    [1] Voar
    [2] Ler Mentes
    [3] Ficar Invisível
    [4] Teletransporte
    [5] Sair''')
    opcao = int(input('O que você deseja fazer?'))
    if opcao == 1:
        print ('Agora você pode voar :)')
    elif opcao == 2:
            print ('Agora você pode ler mentes :)')
    elif opcao == 3:
            print ('Agora você pode ficar invisível :)')
    elif opcao == 4:
            print ('Agora você pode se teletransportar :)')
    elif opcao == 5:
            print ('Até logo :D')
    else:    
            print ('Opção inválida :( Tente novamente')
    print ('*'*15)
    sleep(1)
print('Finalizado com sucesso!')
