import threading
from  datetime import datetime
import threading
from datetime import datetime

mutex = threading.Semaphore(1)
database_access = threading.Semaphore(1)
readtry = threading.Semaphore(1)
def lecture(reader_id):
    print(f"Lecteur {reader_id} est entrain de lire  " + datetime.now())
    #lecture mel database
    print(f"Lecteur {reader_id} a fini de lire."+ datetime.now())

def ecriture(writer_id):
    print(f"Redacteur {writer_id} est entrain d'ecrire "+datetime.now())
    #ecriture mel database
    print(f"Redacteur {writer_id} a fini d'écrire "+datetime.now())
def lecteur(lect_id):
    global  readcount
    mutex.acquire()
    readcount+=1
    if(readcount ==1):
        database_access.acquire()
    mutex.release()
    lecture(lect_id)
    mutex.acquire()
    readcount-=1
    if(readcount==0):
        database_access.release()
    mutex.release()
def redacteur(redc_id):
    database_access.acquire()
    ecriture(redc_id)
    database_access.release()
    mutex.acquire()
