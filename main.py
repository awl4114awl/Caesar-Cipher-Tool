import tkinter as tk
from tkinter import messagebox
from caesar_cipher import caesar_cipher

# Function to handle encryption
def encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = caesar_cipher(text, shift)
    result_text.set(encrypted_text)

# Function to handle decryption
def decrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = caesar_cipher(text, shift, encrypt=False)
    result_text.set(decrypted_text)

# Setting up the main window with dark mode
window = tk.Tk()
window.title("Caesar Cipher Tool")

# Dark mode colors
bg_color = "#2E2E2E"
fg_color = "#F5F5F5"
entry_bg_color = "#3E3E3E"
button_bg_color = "#4E4E4E"
button_fg_color = "#F5F5F5"

window.configure(bg=bg_color)

# Input text field
tk.Label(window, text="Enter text:", bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10, pady=10)
entry_text = tk.Entry(window, width=40, bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
entry_text.grid(row=0, column=1, padx=10, pady=10)

# Input shift field
tk.Label(window, text="Enter shift:", bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=10, pady=10)
entry_shift = tk.Entry(window, width=40, bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
entry_shift.grid(row=1, column=1, padx=10, pady=10)

# Encrypt button
btn_encrypt = tk.Button(window, text="Encrypt", command=encrypt, bg=button_bg_color, fg=button_fg_color)
btn_encrypt.grid(row=2, column=0, padx=10, pady=10)

# Decrypt button
btn_decrypt = tk.Button(window, text="Decrypt", command=decrypt, bg=button_bg_color, fg=button_fg_color)
btn_decrypt.grid(row=2, column=1, padx=10, pady=10)

# Result label
result_text = tk.StringVar()
tk.Label(window, text="Result:", bg=bg_color, fg=fg_color).grid(row=3, column=0, padx=10, pady=10)
tk.Entry(window, textvariable=result_text, state="readonly", width=40, bg=entry_bg_color, fg=fg_color, readonlybackground=entry_bg_color).grid(row=3, column=1, padx=10, pady=10)

# Run the GUI loop
window.mainloop()
