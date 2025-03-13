import threading
import time

def Saudacao(nome, tempo):
    print(f'Olá, {nome}!')
    time.sleep(tempo)
    print(f'Tchau, {nome}!')

TA = threading.Thread(target=Saudacao, args = ('Arthur',5))
TB = threading.Thread(target=Saudacao, args = ('Brunna',2))

t0 = time.time()

TA.start()
TB.start()
TA.join()
TB.join()
print('FIm da execução do código')