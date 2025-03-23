import time
import requests
import threading

def baixar_arquivo(url, nome_arquivo):
    print(f"Baixando {nome_arquivo}...")
    resposta = requests.get(url)
    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(resposta.content)
    print(f"{nome_arquivo} baixado!")

if __name__ == '__main__':
    urls = [
        ("https://www.exemplo.com/arquivo1.zip", "arquivo1.zip"),
        ("https://www.exemplo.com/arquivo2.pdf", "arquivo2.pdf"),
        ("https://www.exemplo.com/arquivo3.jpg", "arquivo3.jpg"),
    ]

    inicio = time.time()
    threads = []
    for url, nome_arquivo in urls:
        thread = threading.Thread(target=baixar_arquivo, args=(url, nome_arquivo))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Aguarda todas as threads terminarem

    fim = time.time()

    print(f"Tempo de execução paralelo (threads): {fim - inicio:.2f} segundos")