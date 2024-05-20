# Sem07_IA_Trabalho1
Membros da Equipe: _Lila Maria, Lince Sena, Det Teixeira_

O trabalho de Inteligência Artificial do Semestre de 2024.1 consiste na utilização dos algoritmos Breadth First Search, Depth First Search com busca iterativa, A* com heurística de peças erradas, e A* com heurística de Manhattan para a solução de um N-Puzzle.

O código foi feito utilizando Orientação a Objetos com Python e Pygame

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

**Falta Implementar:**
- A versão terminal do jogo

Também é necessário fazer um relatório com as instâncias testadas, e contendo:
- Quantidade de passos de sua solução;
- Total de tempo gasto para achar a solução (se encontrar);
- Quantidade máxima de memória utilizada (pode ser usado a estrutura de fila/pilha
para mensurar);
- Quantidade de nós expandidos;
- Fator de ramificação média (quantidade média de filhos dos nós internos da árvore
de busca).
