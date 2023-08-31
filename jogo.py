import os
import random
from colorama import Fore,Back,Style  # Importa o módulo colorama para estilização de texto

# Função para criar tela vazio
def criatela():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
# Função para Exibir o tela
def imprimetela(tela):
    # Limpa a tela do console
    os.system("cls")
    
    print("    1   2   3")  # Contagem das colunas começa em 1
    for i in range(3):
        print(f"{i+1}:  " + " | ".join(tela[i]))
        if i < 2:
            print("   -----------")
 

# Função que testa se é um nó terminal
# 0 -> não é terminal
# 1 -> vitória de min [o]
# 2 -> empate
# 3 -> vitória de max [x] 
def testeTerminal(tela):
    # testa diagonal 1
  if tela[0][0]==tela[1][1] and tela[1][1]==tela[2][2]:
    if(tela[0][0]=='x'):
      return 3
    elif(tela[0][0]=='o'):
      return 1
  # testa diagonal 2
  if tela[2][0]==tela[1][1] and tela[1][1]==tela[0][2]:
    if(tela[2][0]=='x'):
      return 3
    elif(tela[2][0]=='o'):
      return 1
  # testa linhas e colunas
  for i in range(3):
    # testa linhas
    if tela[i][0]==tela[i][1] and tela[i][1]==tela[i][2]:
      if(tela[i][0]=='x'):
        return 3
      elif(tela[i][0]=='o'):
        return 1
    # testa colunas
    if tela[0][i]==tela[1][i] and tela[1][i]==tela[2][i]:
      if(tela[0][i]=='x'):
        return 3
      elif(tela[0][i]=='o'):
        return 1
  # testa a ocorrência do empate
  empate = True
  for i in range(3):
    if(' ' in tela[i]):
      empate = False
  if(empate):
    return 2
  # não é terminal
  return 0


# Função para Max
def acaoMax(tela):
   # veritica se é terminal e, caso seja, retorna utilidade e estado terminal
  terminal = testeTerminal(tela)
  if(terminal):
    return [terminal, tela]
  # criação da lista de ações possíveis
  acoes = []
  for i in range(3):
    for j in range(3):
      if(tela[i][j]==' '):
        copia = [list(tela[0]),list(tela[1]), list(tela[2])]
        copia[i][j] = 'x'
        acoes.append([0, copia])
  # para cada acão "passa" jogada para min
  for i in range(len(acoes)):
    acoes[i][0] = acaoMin(acoes[i][1])[0] # usa utilidade retornada
  # retorna a melhor acão para max
  return max(acoes)
# Função para Min  
def acaoMin(tela):
    # veritica se é terminal e, caso seja, retorna utilidade e estado terminal
  terminal = testeTerminal(tela)
  if(terminal):
    return [terminal, tela]
  # criação da lista de ações possíveis
  acoes = []
  for i in range(3):
    for j in range(3):
      if(tela[i][j]==' '):
        copia = [list(tela[0]),list(tela[1]), list(tela[2])]
        copia[i][j] = 'o'
        acoes.append([0, copia])
  # para cada acão "passa" jogada para max
  for i in range(len(acoes)):
    acoes[i][0] = acaoMax(acoes[i][1])[0]
  # retorn a melhor ação para min
  return min(acoes)


# Função main
def main():
    nome = input('Digite o seu nome')
    cpuPrimeiro = True
    while True:
        print('bem Vindo ' + nome + Fore.RED)
        print('1-CPU 1 x CPU 2\n2-Jogador x CPU\n3-Jogador 1 x Jogador 2')
        op = int(input('4-Sair\nOpção: '))
        vezCPU = True
        if 1 <= op <= 3:
            while True:
                tela = criatela()
                imprimetela(tela)
                vezPrimeiro = True
                while not testeTerminal(tela):
                    if vezCPU and (op == 1 or op == 2):
                        if vezPrimeiro and cpuPrimeiro:
                            aux = acaoMax(tela)
                            tela = aux[1]
                        elif not vezPrimeiro:
                            aux = acaoMin(tela)
                            tela = aux[1]
                    if (op == 2 and not vezCPU) or op == 3:
                        while True:
                            if vezPrimeiro and (op == 3 or not cpuPrimeiro):
                               print('Jogador [x]: ')
                               
                               valor = 'x'
                            else:
                                print('Jogador [o]: ')
                                valor = 'o'
                            linha = int(input('linha: '))
                            coluna = int(input('coluna: '))
                            if 1 <= linha <= 3 and 1 <= coluna <= 3:
                                if tela[linha - 1][coluna - 1] == ' ':
                                    tela[linha - 1][coluna - 1] = valor
                                    break
                    if op == 2:
                        vezCPU = not vezCPU
                    imprimetela(tela)
                    vezPrimeiro = not vezPrimeiro
                if op == 2:
                    cpuPrimeiro = not cpuPrimeiro
                else:
                    cpuPrimeiro = True
                vezCPU = cpuPrimeiro

                resultado = testeTerminal(tela)
                if resultado == 1:
                    print(+ Fore.RESET + 'Vitória do [o]!' + Fore.GREEN)
                elif resultado == 3:
                    print('Vitória do [x]!'  + Fore.GREEN)
                else:
                    print('Empate!')
                while True:
                    saida = input('Jogar novamente?[y ou n]'  + Fore.BLUE)
                    saida = saida.lower()
                    if saida == 'y' or saida == 'n':
                        break
                if saida == 'n':
                    break

# Execução do programa
main()
