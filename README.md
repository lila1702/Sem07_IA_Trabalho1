# Sem07_IA_Trabalho1
Membros da Equipe: _Lila Maria, Lince Sena, Det Teixeira_

O trabalho de Inteligência Artificial do Semestre de 2024.1 consiste na utilização dos algoritmos Breadth First Search, Depth First Search com busca iterativa, A* com heurística de peças erradas, e A* com heurística de Manhattan para a solução de um N-Puzzle.

O código foi feito utilizando Orientação a Objetos com Python e Pygame
Também possui uma versão que utiliza apenas o terminal

**Funcionalidades:**
- Selecionar a dificuldade do puzzle (o n do n-puzzle) através dos _settings.py_
- Embaralhar o estado inicial do puzzle com base no estado ideal (para garantir que haja uma solução)
- Cronometragem para gerar o tempo de solução
- Contagem de quantos movimentos foram realizados até chegar na solução
- Registro em _Soluções.txt_ qual foi o Solver utilizado (Humano, BFS, DPSi, A* heurística peças erradas, A* heurística manhattan) e suas respectivas contagens de tempo e movimentos
- Algoritmo BFS
- DFSi
- Algoritmo A* com heurística de peças erradas (H1)
- Algoritmo A* com heurística de Manhattan (H2)
- Versão em Terminal do Jogo, para uma eficiência maior, pois o Pygame para de responder enquanto espera os algoritmos

Também é necessário fazer um relatório com as instâncias testadas, e contendo:
- Quantidade de passos de sua solução;
- Total de tempo gasto para achar a solução (se encontrar);
- Quantidade máxima de memória utilizada (pode ser usado a estrutura de fila/pilha
para mensurar);
- Quantidade de nós expandidos;
- Fator de ramificação média (quantidade média de filhos dos nós internos da árvore
de busca).

**Para executar o código:**
É necessário ter:
- [Python](https://www.python.org/downloads/)
- Pygame `pip install pygame`

Você pode executar o jogo através da sua versão pygame ou através da sua versão de terminal
`py main.py`
ou
`py main_terminal_edition.py`
Para modificar o n do n-puzzle (padrão 3), você deve modificar o _settings.py_ em GAMESIZE para o que deseja.

O jogo automaticamente irá criar o tabuleiro e uma versão embaralhada dele com soluções possíveis (ele cria a partir do estado finalizado).
