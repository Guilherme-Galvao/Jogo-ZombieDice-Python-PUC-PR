# 🧟 Jogo Zombie Dice em Python (Protótipo Semana 4)

Este projeto é uma implementação do popular jogo de dados **Zombie Dice** em Python, desenvolvido para a disciplina de Raciocínio Computacional da PUC-PR.

O objetivo é simular a jogabilidade básica do jogo de mesa, onde os jogadores competem para "comer" o máximo de cérebros possível, evitando ser atingidos por tiros.

## 🧠 Informações do Projeto

* **Autor:** Luiz Guilherme Galvão
* **Curso:** Inteligência Artificial Aplicada
* **Disciplina:** Raciocínio Computacional
* **Protótipo:** Semana 4 (Encontrado no arquivo `ZombieDice.py`)

---

## 🎲 Regras do Jogo e Objetivo

O jogo suporta **dois ou mais jogadores** e segue um sistema de turnos.

### Objetivo
O primeiro jogador a alcançar **13 cérebros** vence o jogo imediatamente.

### Dados e Faces
O jogo utiliza 13 dados de três cores, cada um com as seguintes faces:

| Face | Símbolo | Significado | Ação na Rodada |
| :--- | :---: | :--- | :--- |
| **Cérebro** | `C` | Ponto para o jogador. | Contabiliza na pontuação do turno. |
| **Passos** | `P` | Humano que escapou. | Dado guardado para o próximo lançamento do turno. |
| **Tiro** | `T` | Humano revidou. | Contabiliza na contagem de risco do turno. |

### Regras de Risco e Fim de Turno

1.  **Início de Turno:** O jogador da vez retira **3 dados** do "tubo" (o conjunto de 13 dados) para lançar.
2.  **Perda de Pontos (3 Tiros):** Se o jogador acumular **3 ou mais tiros** (`"T"`) em um único turno, ele perde todos os cérebros acumulados *neste turno*, e a vez passa para o próximo jogador.
3.  **Fim do Turno:** Ao final do lançamento, o jogador decide:
    * **Continuar (`s`):** Lançar novamente para tentar mais cérebros. Os dados com faces de 'Passos' (`P`) são guardados e reutilizados no próximo lançamento. Novos dados são tirados do tubo para totalizar 3 dados.
    * **Parar (`n`):** Salva os cérebros acumulados no turno para sua pontuação total e zera o contador de tiros. O turno passa para o próximo jogador.

---

## 💻 Estrutura do Código (`ZombieDice.py`)

| Bloco de Código | Linhas | Descrição |
| :--- | :---: | :--- |
| **Inicialização** | 1-26 | Imprime a identificação do aluno/curso e solicita a entrada dos nomes dos jogadores, garantindo um mínimo de 2. |
| **Definição dos Dados** | 32-48 | Define a lista `dados` com as faces dos 13 dados (6 verdes, 4 amarelos, 3 vermelhos). |
| **Estrutura de Pontos** | 51-59 | Inicializa o dicionário `pontos` para cada jogador, rastreando `"cerebros"` (pontuação total) e `"tiros"` (pontuação do turno). |
| **Loop Principal** | 62-129 | Contém a lógica do jogo: sorteio dos dados, lançamento das faces, cálculo de pontos/tiros e a decisão do jogador sobre continuar ou passar. |
| **Regras de Vitória/Derrota** | 96-106 | Contém as verificações de vitória (>= 13 cérebros) e perda de turno (>= 3 tiros). |
