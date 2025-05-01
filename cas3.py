import threading
from datetime import datetime

# Sémaphores
mutex = threading.Semaphore(1)              # protège readcount
read_try = threading.Semaphore(1)           # priorité rédacteurs
database_access = threading.Semaphore(1)    # accès exclusif à la BDD

readcount = 0  # compteur des lecteurs


def lecture(reader_id):
    print(f"Lecteur {reader_id} est entrain de lire  " + datetime.now())
    #lecture mel database
    print(f"Lecteur {reader_id} a fini de lire."+ datetime.now())

def ecriture(writer_id):
    print(f"Redacteur {writer_id} est entrain d'ecrire "+datetime.now())
    #ecriture mel database
    print(f"Redacteur {writer_id} a fini d'écrire "+datetime.now())


def lecteur(reader_id):
    global readcount
    read_try.acquire()  #p(read_try)
    mutex.acquire()    #p(mutex)
    readcount += 1
    if readcount == 1:
        database_access.acquire() #p(database_access)
    mutex.release() #v(mutex)
    read_try.release() #v(release)
    lecture(reader_id)
    mutex.acquire() #p(mutex)
    readcount -= 1
    if readcount == 0:
        database_access.release()  # dernier lecteur libere la BDD
    mutex.release() #v(mutex)

def redacteur(writer_id):
    read_try.acquire()         # p(read_try)
    database_access.acquire()  # p(databse_access) pour acces exclusif
    ecriture(writer_id)
    database_access.release()  #v(database)
    read_try.release()  #v(read_try)

