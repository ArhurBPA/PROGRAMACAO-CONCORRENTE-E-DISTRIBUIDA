import threading
import time

Contador = 0
L = threading.Lock()  # Corrigido, agora usa threading.Lock


def incrementar():
    global Contador
    for _ in range(1000):
        L.acquire()
        try:
            x = Contador
            time.sleep(0.001)
            x = x + 1
            Contador = x
        finally:
            L.release()


TA = threading.Thread(target=incrementar)
TB = threading.Thread(target=incrementar)
TC = threading.Thread(target=incrementar)

TA.start()
TB.start()
TC.start()

TA.join()
TB.join()
TC.join()

print(f'Contador: {Contador}')
