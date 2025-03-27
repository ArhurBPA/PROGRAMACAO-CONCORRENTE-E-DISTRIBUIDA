import threading
import time

L1 = threading.Lock()
L2 = threading.Lock()

def tarefa():
    print('T1: tentando adquirir lock1')
    L1.acquire()
    print('T2: adquiriu lock1, agora tentando adquirir lock2')
    time.sleep(1)
    L2.acquire()
    print('L1: lock2 adquirido')
    L2.release()
    L1.release()


ListaDeThreads = []

for _ in range(50):
    t = threading.Thread(target=incrementar)
    ListaDeThreads.append(t)
    t.start()

for t in ListaDeThreads:
    t.join()


print("Programa finalizado")
