import threading
import time

Contador = 0
L = threading.Lock()

def incrementar():
    global Contador
    for _ in range(5000):
        L.acquire()
        x = Contador
        time.sleep(0.0001)
        x = x + 1
        Contador = x
        L.release()


ListaDeThreads = []

for _ in range(50):
    t = threading.Thread(target=incrementar)
    ListaDeThreads.append(t)
    t.start()

for t in ListaDeThreads:
    t.join()

print(f'Contador: {Contador}')