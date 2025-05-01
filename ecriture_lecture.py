from datetime import datetime

from main import logs ,tk


def lecture(reader_id):
    logs.insert(tk.END, f"Lecteur {reader_id} est entrain de lire  " + datetime.now())
    #lecture mel database
    logs.insert(tk.END,f"Lecteur {reader_id} a fini de lire."+ datetime.now() )

def ecriture(writer_id):

    logs.insert(tk.END,f"Lecteur {writer_id} a fini de lire." + datetime.now())
    #ecriture mel databas
    logs.insert(tk.END,f"Redacteur {writer_id} a fini d'écrire "+datetime.now())