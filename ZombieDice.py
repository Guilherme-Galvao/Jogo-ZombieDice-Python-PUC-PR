print("Aluno: Luiz Guilherme Galvão")
print("Curso: Inteligência Artificial Aplicada.")
print("Raciocinio Computacional - Protótipo semana 4!")

print("Bem vindo ao jogo Zombie Dice!")

jogadores = []
opcao = True
while opcao:
  jogadores.append(input("Digite o nome do jogador: "))
  if len(jogadores) < 2:
    print("O jogo deve ter mínimo 2 participantes! Adicione mais uma pessoa: ")


  else:
    op = print("Que se iniciem os jogos!!!")
    if len(jogadores) == 2:
        opcao = False
        continue


import random

sair_do_jogo = False

contador_turno = 1
index_jogador = 1

# 6 Dados verdes: “CPCTPC”
# 4 Dados amarelos: “TPCTPC”
# 3 Dados vermelhos: “TPTCPT”

dados = [
    ["C", "P", "C", "T", "P", "C"],  # Verde
    ["C", "P", "C", "T", "P", "C"],  # Verde
    ["C", "P", "C", "T", "P", "C"],  # Verde
    ["C", "P", "C", "T", "P", "C"],  # Verde
    ["C", "P", "C", "T", "P", "C"],  # Verde
    ["C", "P", "C", "T", "P", "C"],  # Verde

    ["T", "P", "C", "T", "P", "C"],  # Amarelo
    ["T", "P", "C", "T", "P", "C"],  # Amarelo
    ["T", "P", "C", "T", "P", "C"],  # Amarelo
    ["T", "P", "C", "T", "P", "C"],  # Amarelo

    ["T", "P", "T", "C", "P", "T"],  # Vermelho
    ["T", "P", "T", "C", "P", "T"],  # Vermelho
    ["T", "P", "T", "C", "P", "T"],  # Vermelho
]


pontos = {}

pontos[jogadores[0]] = {
    "cerebros": 0,
    "tiros": 0
}

pontos[jogadores[1]] = {
    "cerebros": 0,
    "tiros": 0
}


while not sair_do_jogo:
    jogador_da_vez = jogadores[index_jogador]
    print(f"Turno {contador_turno}")
    print(f"{jogador_da_vez} jogou os dados")

    # Pega 3 dados do tubo
    dado1 = random.choice(dados)
    dado2 = random.choice(dados)
    dado3 = random.choice(dados)

    # Lança os dados
    valor1 = random.choice(dado1)
    valor2 = random.choice(dado2)
    valor3 = random.choice(dado3)

    print("  os valores são {},{},{}".format(valor1, valor2, valor3))
    if valor1 == "C":
        pontos[jogador_da_vez]["cerebros"] += 1

    if valor2 == "C":
        pontos[jogador_da_vez]["cerebros"] += 1

    if valor3 == "C":
        pontos[jogador_da_vez]["cerebros"] += 1

    if valor1 == "T":
        pontos[jogador_da_vez]["tiros"] += 1

    if valor2 == "T":
        pontos[jogador_da_vez]["tiros"] += 1

    if valor3 == "T":
        pontos[jogador_da_vez]["tiros"] += 1

    if pontos[jogador_da_vez]["cerebros"] >= 13:
        print(f"Parabens {jogador_da_vez} voce devorou mais cerebros e ganhou!!")
        sair_do_jogo = True
        continue
    if pontos[jogador_da_vez]["cerebros"] >= 9:
        print('Falta pouco!')
    if pontos[jogador_da_vez]["tiros"] == 2:
            print("Cuidado mais um tiro e você perde todos os pontos!")
    elif pontos[jogador_da_vez]["tiros"] >= 3:
        print("Que azar! {} levou muitos tiros e zerou os pontos".format(jogador_da_vez))
        pontos[jogador_da_vez]["cerebros"] = 0
        pontos[jogador_da_vez]["tiros"] = 0
        index_jogador += 1

        if index_jogador >= len(jogadores):
            index_jogador = 0
        continue

    print("Atualmente os pontos são")
    print(pontos)

    passar = input("Gostaria de continuar? s ou n \n")
    if passar != "s":
        pontos[jogador_da_vez]["tiros"] = 0
        index_jogador += 1

        if index_jogador >= len(jogadores):
            index_jogador = 0

    contador_turno += 1

print("Fim de jogo")