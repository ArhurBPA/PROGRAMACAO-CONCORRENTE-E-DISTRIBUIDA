import threading

b = threading.Barrier(3)

def Trabalho(ID):
    print (f"Thread {ID} iniciada.")
    threading.Event().wait(0)
    print(f"Thrad {ID} chegou na barreira.")
    b.wait()
    print(f"Thread {ID} passou pela barreira.")

threads = [threading.Thread(target= Trabalho, args=(i,)) for i in range(40)]
for t in threads:t.start()
for t in threads:t.join()