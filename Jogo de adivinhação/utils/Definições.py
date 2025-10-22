from time import sleep
from random import randint

# Função para criar espaçamento visual no console
def espacamento():
    print("=" * 120)

#ftela inicial de saudação ao jogador
def saudacoes():
    print("Carregando tela inicial...")
    sleep(2)
    espacamento()
    print("Bem-vindo ao sistema de jogo de adivinhação!")
    espacamento()
    sleep(1)

# Função para coletar o nome e a idade do jogador com tratamento de erros
def player_input():
    while True:
        try:
            nome = str(input("Digite seu nome por favor: ")).strip().title()
            idade = int(input("Digite sua idade: "))
            print("Validando informações...")
            sleep(1)
            break
        except ValueError:
            print("Entrada inválida. Por favor, tente novamente.")
    return nome, idade
   

# Função principal do jogo de adivinhação
def jogar():
    nome, idade = player_input()
    print(f"\nOlá {nome}! Você tem 10 tentativas para adivinhar o número correto.")
    print("Escolha um número entre 1 e 100.") 
    numero_secreto = randint(1, 100)
    
    for tentativa_atual in range(10):
        try:
            tentativas_restantes = 10 - tentativa_atual
            print(f"\nVocê tem {tentativas_restantes} tentativa(s) restante(s).")
            palpite = int(input("Digite seu palpite: "))
            
            if palpite == numero_secreto:
                print(f"Parabéns, {nome}! Você adivinhou o número corretamente!")
                return  # Encerra o jogo com vitória
            elif palpite > numero_secreto:
                print("O número secreto é MENOR que seu palpite!")
            else:
                print("O número secreto é MAIOR que seu palpite!")
                
        except ValueError:
            print("Por favor, digite apenas números!")
            continue  
    
    print(f"Game Over, {nome}! Suas tentativas acabaram.")
    print(f"O número secreto era {numero_secreto}.")


#função de retornar pro game:
def retornar_ao_jogo():
    retornargame = input("Deseja jogar novamente? (sim/nao): ").strip().lower()
    if retornargame == "sim":
        return jogar()
    else:
        print("Obrigado por jogar! Até a próxima.")
        print("Fechando o jogo...")
        sleep(2)
        exit()

# Início do jogo
saudacoes()
jogar()
retornar_ao_jogo()

        

    