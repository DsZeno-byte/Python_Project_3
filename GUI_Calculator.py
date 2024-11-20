import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widget
entry = tk.Entry(root, width=25, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons dynamically
row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), command=calculate)
    elif button == "C":
        btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), command=clear)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), command=lambda b=button: button_click(b))
    
    btn.grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid to expand with window resize
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
