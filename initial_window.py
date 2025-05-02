import tkinter as tk
from tkinter import ttk, messagebox
import threading
import queue
import random
import time
from datetime import datetime
import cas1, cas2, cas3


class ReaderWriterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulateur Lecteurs-Rédacteurs")
        self.root.geometry("800x600")
        # Variables de contrôle
        self.running = False
        self.threads = []
        self.log_queue = queue.Queue()
        self.case_module = cas1  # Par défaut

        # Configuration de l'interface
        self.setup_ui()

        # Démarrer la mise à jour des logs
        self.update_logs()

    def setup_ui(self):
        """Configure tous les éléments de l'interface"""
        # Frame principale
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Sélection du cas
        case_frame = ttk.LabelFrame(main_frame, text="Stratégie de synchronisation", padding="10")
        case_frame.pack(fill=tk.X, pady=5)

        self.case_var = tk.StringVar(value="cas1")

        cases = [
            ("Priorité absolue aux lecteurs", "cas1"),
            ("Priorité conditionnelle", "cas2"),
            ("Priorité aux rédacteurs", "cas3")
        ]

        for text, value in cases:
            ttk.Radiobutton(
                case_frame,
                text=text,
                variable=self.case_var,
                value=value
            ).pack(anchor=tk.W, pady=2)

        # Configuration de la simulation
        config_frame = ttk.LabelFrame(main_frame, text="Configuration", padding="10")
        config_frame.pack(fill=tk.X, pady=5)

        ttk.Label(config_frame, text="Nombre d'opérations:").pack(anchor=tk.W)
        self.op_count = ttk.Entry(config_frame)
        self.op_count.insert(0, "20")
        self.op_count.pack(fill=tk.X)

        ttk.Label(config_frame, text="Ratio lecteurs/rédacteurs:").pack(anchor=tk.W)
        self.ratio = ttk.Scale(config_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.ratio.set(60)  # 60% lecteurs
        self.ratio.pack(fill=tk.X)

        # Contrôles
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)

        self.start_btn = ttk.Button(
            control_frame,
            text="Démarrer la simulation",
            command=self.start_simulation
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = ttk.Button(
            control_frame,
            text="Arrêter",
            state=tk.DISABLED,
            command=self.stop_simulation
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        # Zone de logs
        log_frame = ttk.LabelFrame(main_frame, text="Journal des opérations", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True)

        self.log_text = tk.Text(log_frame, height=15, state=tk.DISABLED)
        self.log_text.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.log_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)

    def start_simulation(self):
        """Démarre la simulation avec les paramètres choisis"""
        if self.running:
            return

        self.running = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)

        # Chargement du module approprié
        case = self.case_var.get()
        self.case_module = {
            "cas1": cas1,
            "cas2": cas2,
            "cas3": cas3
        }.get(case, cas1)

        # Récupération des paramètres
        try:
            num_ops = int(self.op_count.get())
            reader_ratio = self.ratio.get() / 100
        except ValueError:
            messagebox.showerror("Erreur", "Valeurs invalides")
            return

        # Lancement des threads
        for i in range(num_ops):
            if not self.running:
                break

            if random.random() < reader_ratio:
                t = threading.Thread(
                    target=self.run_reader,
                    args=(i,),
                    daemon=True
                )
            else:
                t = threading.Thread(
                    target=self.run_writer,
                    args=(i,),
                    daemon=True
                )

            self.threads.append(t)
            t.start()
            time.sleep(random.uniform(0.1, 0.3))  # Délai aléatoire entre threads

    def run_reader(self, reader_id):
        info = self.case_module.lecteur(f"Reader-{reader_id}")
        self.log_queue.put(
            f"[{info[0]['start_time']}] Début | [{info[0]['end_time']}] Fin | "
            f"Lecteur {reader_id} a lu: {info[0]['value']} | Lecteurs actifs: {info[0]['total']}"
        )

    def run_writer(self, writer_id):
        value = random.randint(0, 100)
        info = self.case_module.redacteur(value, f"Writer-{writer_id}")
        self.log_queue.put(
            f"[{info[0]['start_time']}] Début | [{info[0]['end_time']}] Fin | "
            f"Rédacteur {writer_id} a écrit: {info[0]['value']}"
        )


    def stop_simulation(self):
        """Arrête proprement la simulation"""
        self.running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.log_queue.put("=== Simulation arrêtée ===")

    def update_logs(self):
        """Met à jour l'affichage des logs"""
        while not self.log_queue.empty():
            msg = self.log_queue.get()
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, msg + "\n")
            self.log_text.see(tk.END)
            self.log_text.config(state=tk.DISABLED)

        self.root.after(100, self.update_logs)


if __name__ == "__main__":
    root = tk.Tk()
    app = ReaderWriterApp(root)
    root.mainloop()
