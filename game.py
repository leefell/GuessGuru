import random
import os

TENTATIVAS = 6
MAXIMO_RODADAS = TENTATIVAS - 1

MENSAGENS = {
    'DEFAULT': {
        'ENTRADA': 'Estou pensando em um número de 0 as 10. Tente Adivinhar!',
        'VITORIA': 'Parabéns! Era esse número mesmo',
        'DERROTA': 'Acabaram suas chances! Mais sorte na próxima',
        'TENTATIVA': 'Digite um número de 0 - 10: ',
        'NOVA_PARTIDA': 'Deseja jogar mais uma vez? (1 - Sim | 0 - Não): ',
        'DESPEDIDA': 'Tchau!'
    },
    'ERROS':{
        'TENTATIVA_INVALIDA': 'ERRO: São permitidos apenas números inteiros entre 0 e 10',
        'NOVA_PARTIDA_INVALIDA': 'ERRO: São permitidas apenas as opções: 1-Sim ou 0-Não',
    }
}

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('cls')

def jogar_novo_jogo():
    NUMERO = random.randint(0, 10)
    rodadas = MAXIMO_RODADAS

    print(MENSAGENS['DEFAULT']['ENTRADA'])

    for tentativa in range(TENTATIVAS):
        escolha = input(MENSAGENS['DEFAULT']['TENTATIVA'])

        if not escolha.isdigit() or int(escolha) < 0 or int(escolha) > 10:
            print(MENSAGENS['ERROS']['TENTATIVA_INVALIDA'])
            continue

        escolha = int(escolha)

        if escolha == NUMERO:
            print(MENSAGENS['DEFAULT']['VITORIA'])
            print(f"Você ainda tinha {rodadas} rodadas para tentar adivinhar o número.")
            break
        else:
            print("Tente novamente.")
            rodadas -= 1
    else:
        print(f"Você excedeu o número máximo de tentativas. O número era: {NUMERO}")

def main():
    while True:
        limpar_tela()
        jogar_novo_jogo()
        nova_partida = input(MENSAGENS['DEFAULT']['NOVA_PARTIDA'])
        if nova_partida == '0':
            print(MENSAGENS['DEFAULT']['DESPEDIDA'])
            break
        elif nova_partida != '1':
            print(MENSAGENS['ERROS']['NOVA_PARTIDA_INVALIDA'])
            continue

if __name__ == "__main__":
    main()