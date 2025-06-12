import tkinter as tk
import math

def click(event):
    entry.insert(tk.END, event.widget["text"])

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(num ** 2))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.sqrt(num)))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# --- Setup Window ---
root = tk.Tk()
root.title("Calculator")
root.geometry("330x450")
root.configure(bg="#f0f4f7")
root.resizable(False, False)

# --- Entry Field ---
entry_frame = tk.Frame(root, bg="#f0f4f7", padx=10, pady=10)
entry_frame.pack(fill="x")

entry = tk.Entry(entry_frame, font=("Segoe UI", 20), bd=2, relief="ridge", justify="right", bg="white")
entry.pack(fill="x", ipady=10)

# --- Clear Button on Top Right ---
clear_frame = tk.Frame(root, bg="#f0f4f7", padx=10, pady=5)
clear_frame.pack(fill="x")

tk.Button(clear_frame, text="Clear", font=("Segoe UI", 14), bg="#f27c7c", fg="white",
          command=clear, relief="flat", padx=10, pady=5).pack(anchor="e")

# --- Button Layout ---
button_font = ("Segoe UI", 14)
btn_padx = 10
btn_pady = 8

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '+', '.', '=']
]

for row in buttons:
    row_frame = tk.Frame(root, bg="#f0f4f7", padx=10, pady=2)
    row_frame.pack(fill="x")
    for char in row:
        btn = tk.Button(row_frame, text=char, font=button_font, bg="#e2e8f0", relief="flat",
                        padx=btn_padx, pady=btn_pady, width=4)
        btn.pack(side="left", expand=True, padx=5, pady=2)
        if char == '=':
            btn.bind("<Button-1>", lambda e: calculate())
        else:
            btn.bind("<Button-1>", click)

# --- Extra Operations ---
extras = tk.Frame(root, bg="#f0f4f7", padx=10, pady=10)
extras.pack(fill="x")

tk.Button(extras, text="x²", font=button_font, bg="#d1fae5", relief="flat",
          command=square).pack(side="left", expand=True, padx=5, pady=2)

tk.Button(extras, text="√", font=button_font, bg="#c7d2fe", relief="flat",
          command=square_root).pack(side="left", expand=True, padx=5, pady=2)

# --- Start App ---
root.mainloop()
