from PIL import Image
from tkinter import Tk, filedialog
import threading

def converter_parte_imagem(imagem, imagem_preto_branco, inicio_altura, fim_altura):
    """Converte uma parte da imagem para preto e branco."""
    largura = imagem.width
    for x in range(largura):
        for y in range(inicio_altura, fim_altura):
            r, g, b = imagem.getpixel((x, y))
            luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_preto_branco.putpixel((x, y), luminancia)

def converter_para_preto_e_branco_threads(num_threads=4):  # Adicionado parâmetro para threads
    try:
        root = Tk()
        root.withdraw()

        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
        )
        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        imagem = Image.open(caminho_imagem).convert("RGB")
        largura, altura = imagem.size
        imagem_preto_branco = Image.new("L", (largura, altura))

        # Divisão da imagem para threads
        divisao_altura = altura // num_threads
        threads = []

        for i in range(num_threads):
            inicio_altura = i * divisao_altura
            fim_altura = (i + 1) * divisao_altura if i < num_threads - 1 else altura
            thread = threading.Thread(target=converter_parte_imagem, args=(imagem, imagem_preto_branco, inicio_altura, fim_altura))
            threads.append(thread)
            thread.start()

        # Esperar todas as threads terminarem
        for thread in threads:
            thread.join()

        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return

        imagem_preto_branco.save(caminho_saida)
        print(f"Imagem convertida com sucesso! Salva em: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    converter_para_preto_e_branco_threads(8) #alterado para 8 threads