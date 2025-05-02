import threading
import time
import random


def case1():
    w = threading.Semaphore(1)
    mutex1 = threading.Semaphore(1)
    mutex2 = threading.Semaphore(1)
    nl = 0

    def lecteur(id):
        nonlocal nl
        print(f"Lecteur {id} veut lire")
        mutex1.acquire()
        nl += 1
        if nl == 1:
            w.acquire()
        mutex1.release()

        print(f"Lecteur {id} lit (nl={nl})")
        time.sleep(random.uniform(0.5, 1.5))

        mutex1.acquire()
        nl -= 1
        if nl == 0:
            w.release()
        mutex1.release()
        print(f"Lecteur {id} a fini de lire")

    def redacteur(id):
        print(f"Rédacteur {id} veut écrire")
        mutex2.acquire()
        w.acquire()
        print(f"Rédacteur {id} écrit")
        time.sleep(random.uniform(1, 2))
        w.release()
        mutex2.release()
        print(f"Rédacteur {id} a fini d'écrire")

    threads = []
    for i in range(5):
        if random.random() < 0.6:
            threads.append(threading.Thread(target=lecteur, args=(i,)))
        else:
            threads.append(threading.Thread(target=redacteur, args=(i,)))

    for t in threads:
        t.start()
        time.sleep(random.uniform(0.1, 0.5))

    for t in threads:
        t.join()


# Cas 2: Priorité aux lecteurs seulement si un lecteur est déjà actif
def case2():
    w = threading.Semaphore(1)
    mutex1 = threading.Semaphore(1)
    nl = 0

    def lecteur(id):
        nonlocal nl
        print(f"Lecteur {id} veut lire")
        mutex1.acquire()
        nl += 1
        if nl == 1:
            w.acquire()
        mutex1.release()

        print(f"Lecteur {id} lit (nl={nl})")
        time.sleep(random.uniform(0.5, 1.5))

        mutex1.acquire()
        nl -= 1
        if nl == 0:
            w.release()
        mutex1.release()
        print(f"Lecteur {id} a fini de lire")

    def redacteur(id):
        print(f"Rédacteur {id} veut écrire")
        w.acquire()
        print(f"Rédacteur {id} écrit")
        time.sleep(random.uniform(1, 2))
        w.release()
        print(f"Rédacteur {id} a fini d'écrire")

    threads = []
    for i in range(5):
        if random.random() < 0.6:
            threads.append(threading.Thread(target=lecteur, args=(i,)))
        else:
            threads.append(threading.Thread(target=redacteur, args=(i,)))

    for t in threads:
        t.start()
        time.sleep(random.uniform(0.1, 0.5))

    for t in threads:
        t.join()


# Cas 3: Priorité aux rédacteurs
def case3():
    w = threading.Semaphore(1)
    r = threading.Semaphore(1)
    mutex1 = threading.Semaphore(1)
    mutex2 = threading.Semaphore(1)
    nl = 0
    nr = 0

    def lecteur(id):
        nonlocal nl
        print(f"Lecteur {id} veut lire")
        r.acquire()
        mutex1.acquire()
        nl += 1
        if nl == 1:
            w.acquire()
        mutex1.release()
        r.release()

        print(f"Lecteur {id} lit (nl={nl})")
        time.sleep(random.uniform(0.5, 1.5))

        mutex1.acquire()
        nl -= 1
        if nl == 0:
            w.release()
        mutex1.release()
        print(f"Lecteur {id} a fini de lire")

    def redacteur(id):
        nonlocal nr
        print(f"Rédacteur {id} veut écrire")
        mutex2.acquire()
        nr += 1
        if nr == 1:
            r.acquire()
        mutex2.release()

        w.acquire()
        print(f"Rédacteur {id} écrit")
        time.sleep(random.uniform(1, 2))
        w.release()

        mutex2.acquire()
        nr -= 1
        if nr == 0:
            r.release()
        mutex2.release()
        print(f"Rédacteur {id} a fini d'écrire")

    threads = []
    for i in range(5):
        if random.random() < 0.6:
            threads.append(threading.Thread(target=lecteur, args=(i,)))
        else:
            threads.append(threading.Thread(target=redacteur, args=(i,)))

    for t in threads:
        t.start()
        time.sleep(random.uniform(0.1, 0.5))

    for t in threads:
        t.join()


print("Cas 1: Priorité absolue aux lecteurs")
case1()
print("\nCas 2: Priorité aux lecteurs seulement si un lecteur est déjà actif")
case2()
print("\nCas 3: Priorité aux rédacteurs")
case3()