import threading
import time

def tarefa():
    print('Início...')
    time.sleep(5)
    print('Fim...')

t0 = time.time()
TA = threading.Thread(target = tarefa)
TB = threading.Thread(target = tarefa)

t0 = time.time()
TA.start()
TA.join()
TB.start()
TB.join()

tf = time.time()
deltat = tf - t0
print(f'Tempo gasto: {deltat}')
print('Thread principal finalizada')