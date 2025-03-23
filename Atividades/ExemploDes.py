import time
import requests

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
    for url, nome_arquivo in urls:
        baixar_arquivo(url, nome_arquivo)
    fim = time.time()

    print(f"Tempo de execução sequencial: {fim - inicio:.2f} segundos")