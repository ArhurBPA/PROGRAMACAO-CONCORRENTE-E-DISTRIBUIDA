import threading

s = threading.Semaphore(3)

def trabalho(ID):
    print(f"Thread {ID} iniciou.")
    with s:
        print(f"Thread {ID} passou pelo semaforo.")
        threading.Event().wait(1)
    print(f"Thread {ID} finalizou")

threads = [threading.Thread(target = trabalho, args = (i,)) for i in range(5)]
    
for t in threads: t.start()
for t in threads: t.join()