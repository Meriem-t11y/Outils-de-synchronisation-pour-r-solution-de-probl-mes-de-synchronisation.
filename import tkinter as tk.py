import tkinter as tk
from tkinter import ttk

def execute_simulation():
    num_processes = entry_num_processes.get()
    selected_case = case_dropdown.get()
    operation = operation_var.get()
    
    logs.insert(tk.END, f"Number of Processes: {num_processes}\n")
    logs.insert(tk.END, f"Selected Case: {selected_case}\n")
    logs.insert(tk.END, f"Operation: {operation}\n")
    logs.insert(tk.END, "Starting simulation...\n")
    # Here, you would call the appropriate Python logic for each case

# Main Window
root = tk.Tk()
root.title("Readers-Writers Problem Simulation")

# Input for number of processes
tk.Label(root, text="Enter Number of Processes:").grid(row=0, column=0, padx=10, pady=5)
entry_num_processes = tk.Entry(root)
entry_num_processes.grid(row=0, column=1, padx=10, pady=5)

# Dropdown to select the case
tk.Label(root, text="Select Case:").grid(row=1, column=0, padx=10, pady=5)
case_dropdown = ttk.Combobox(root, values=["Case 1: Reader Priority", "Case 2: Conditional Reader Priority", "Case 3: Writer Priority"])
case_dropdown.grid(row=1, column=1, padx=10, pady=5)

# Radio buttons for operation selection
tk.Label(root, text="Select Operation:").grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar(value="Read")
tk.Radiobutton(root, text="Read from Database", variable=operation_var, value="Read").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Write to Database", variable=operation_var, value="Write").grid(row=3, column=1, sticky="w")

# Execute button
execute_button = tk.Button(root, text="Execute", command=execute_simulation)
execute_button.grid(row=4, column=0, columnspan=2, pady=10)

# Logs output
tk.Label(root, text="Simulation Logs:").grid(row=5, column=0, columnspan=2, pady=5)
logs = tk.Text(root, height=10, width=50)
logs.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()
