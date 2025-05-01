import threading
import tkinter as tk
from tkinter import ttk
import cas1, cas2, cas3
import time

def toggle_entry_field():
    """Toggle visibility of the 'Number to write' field."""
    if operation_var.get() == "Write":
        entry_num.grid(row=3, column=1, padx=10, pady=5)
        number_label.grid(row=3, column=0, padx=10, pady=5)
    else:
        entry_num.grid_remove()
        number_label.grid_remove()


def execute_simulation():
    num = entry_num.get()
    selected_case = case_dropdown.get()
    operation = operation_var.get()

    def worker():
        for i in range(10):  # Change 5 to the number of iterations you want
            if selected_case == "Case 1: Reader Priority":
                if operation == "Write":
                    info = cas1.redacteur(num, selected_case)
                else:
                    info = cas1.lecteur(selected_case)

            elif selected_case == "Case 2: Conditional Reader Priority":
                if operation == "Write":
                    info = cas2.redacteur(num, selected_case)
                else:
                    info = cas2.lecteur(selected_case)

            elif selected_case == "Case 3: Writer Priority":
                print(operation)
                if operation == "Write":
                    info = cas3.redacteur(num, selected_case)
                else:
                    info = cas3.lecteur(selected_case)

            logs.insert(tk.END, f"Simulation {i + 1}...\n")
            logs.insert(tk.END, info )
            time.sleep(0.9)

    threading.Thread(target=worker).start()


# Main Window
root = tk.Tk()
root.title("Readers-Writers Problem Simulation")

# Dropdown to select the case
tk.Label(root, text="Select Case:").grid(row=0, column=0, padx=10, pady=5)
selected_value = tk.StringVar()
selected_value.set("Case 1: Reader Priority")
case_dropdown = ttk.Combobox(root, textvariable=selected_value,
                             values=["Case 1: Reader Priority", "Case 2: Conditional Reader Priority",
                                     "Case 3: Writer Priority"])
case_dropdown.grid(row=0, column=1, padx=10, pady=5)

# Radio buttons for operation selection
tk.Label(root, text="Select Operation:").grid(row=1, column=0, padx=10, pady=5)
operation_var = tk.StringVar(value="Read")
tk.Radiobutton(root, text="Read from Database", variable=operation_var, value="Read", command=toggle_entry_field).grid(
    row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Write to Database", variable=operation_var, value="Write", command=toggle_entry_field).grid(
    row=2, column=1, sticky="w")

# Label and Entry for number of processes
number_label = tk.Label(root, text="Enter Number to write:")
number_label.grid(row=3, column=0, padx=10, pady=5)
entry_num = tk.Entry(root)
entry_num.grid(row=3, column=1, padx=10, pady=5)

# Initially hide the field
toggle_entry_field()

# Execute button
execute_button = tk.Button(root, text="Execute", command=execute_simulation)
execute_button.grid(row=4, column=0, columnspan=2, pady=10)

# Logs output
tk.Label(root, text="Simulation Logs:").grid(row=5, column=0, columnspan=2, pady=5)
logs = tk.Text(root, height=10, width=50)
logs.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()
