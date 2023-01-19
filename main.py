from sys import maxsize
from itertools import permutations

def tsp(graph, s):
    # Inicializa uma lista vazia "vértice" e a preenche com todos os bairros exceto o bairro inicial
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)
    # Inicializa o peso mínimo do caminho com o valor máximo possível
    min_path = maxsize
    # Gera todas as permutações possíveis da lista de vértices
    next_permutation=permutations(vertex)
    for i in next_permutation:
		# Calcule o peso do caminho atual iterando através da permutação e adicionando o peso correspondente do gráfico
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
		# Atualize o peso mínimo do caminho se o peso do caminho atual for menor que o peso mínimo do caminho existente
        min_path = min(min_path, current_pathweight)
    # Retorne o peso mínimo do caminho
    return min_path

if __name__ == "__main__":
	# Gráfico de amostra com o bairro inicial como 0
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(tsp(graph, s))
