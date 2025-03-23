import random
import time
# Função principal do QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot] # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot] # Elementos maiores que o pivô
    return quicksort(left) + [pivot] + quicksort(right)
# Função para gerar números aleatórios
def gerar_numeros_aleatorios(n=100, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]
# Função principal para testar o QuickSort
if __name__ == "__main__":
    tamanhos_listas = [1000, 10000, 100000, ]

    for tamanho in tamanhos_listas:
        tempo_inicio_seq = time.time()
        numeros_ordenados_seq = quicksort(numeros.copy())  # criar uma cópia para n alterar o original
        tempo_fim_seq = time.time()
        tempo_seq = tempo_fim_seq - tempo_inicio_seq