import random
import threading
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def gerar_numeros_aleatorios(n=100, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]


def quicksort_thread(arr, resultado):
    """Ordena uma sublista usando QuickSort e armazena o resultado."""
    resultado.extend(quicksort(arr))


def quicksort_paralelo(arr, num_threads):
    """Ordena a lista em paralelo usando threads."""
    sublistas = dividir_lista(arr, num_threads)
    threads = []
    resultados = [[] for _ in range(num_threads)]  # Lista de listas para os resultados

    for i in range(num_threads):
        thread = threading.Thread(target=quicksort_thread, args=(sublistas[i], resultados[i]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Combinar resultados ordenados
    lista_ordenada = []
    for resultado in resultados:
        lista_ordenada.extend(resultado)

    return sorted(lista_ordenada)  # garantir a ordem correta


def dividir_lista(arr, num_threads):
    """Divide a lista em sublistas para processamento paralelo."""
    tamanho_sublista = len(arr) // num_threads
    sublistas = []
    for i in range(num_threads):
        inicio = i * tamanho_sublista
        fim = (i + 1) * tamanho_sublista if i < num_threads - 1 else len(arr)
        sublistas.append(arr[inicio:fim])
    return sublistas

if __name__ == "__main__":
    tamanhos_listas = [1000, 10000, 100000, ]  # Diferentes tamanhos para listas de teste
    num_threads = 4  # Ajuste o número de threads conforme necessário

    for tamanho in tamanhos_listas:
        numeros = gerar_numeros_aleatorios(tamanho)

        print(f"\nOrdenando lista com {tamanho} elementos:")

        # Ordenação paralela
        tempo_inicio_par = time.time()
        numeros_ordenados_par = quicksort_paralelo(numeros.copy(), num_threads)
        tempo_fim_par = time.time()
        tempo_par = tempo_fim_par - tempo_inicio_par

        print(f"Tempo Paralelo: {tempo_par:.4f} segundos")