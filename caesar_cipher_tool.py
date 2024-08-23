import customtkinter as ctk
from tkinter import filedialog, font, Toplevel
import pyperclip
import configparser

# Caesar Cipher Function
def caesar_cipher(text, shifts, direction='encrypt'):
    result = ""
    shifts = [shift if direction == 'encrypt' else -shift for shift in shifts]
    shift_index = 0
    
    for char in text:
        if char.isalpha() or not ignore_non_alpha.get():
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                shift = shifts[shift_index % len(shifts)]
                result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
                shift_index += 1
            else:
                result += char
        else:
            result += char
    
    return result

# Process Cipher Operation
def process_cipher():
    try:
        text = entry_text.get("1.0", "end-1c")  # Retrieve the entire text from the text widget
        shifts = list(map(int, entry_shift.get().split(',')))
        if any(not (0 <= shift <= 25) for shift in shifts):
            raise ValueError("All shift values must be between 0 and 25")
        direction = "encrypt" if var.get() == 1 else "decrypt"
        result = caesar_cipher(text, shifts, direction)
        result_label.configure(text=result)
        update_counts()
    except ValueError as e:
        result_label.configure(text=f"Error: {e}")

# Copy to Clipboard
def copy_to_clipboard():
    text = result_label.cget("text")
    pyperclip.copy(text)

# Save to File
def save_to_file():
    text = result_label.cget("text")
    if text:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text)

# Load from File
def load_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            entry_text.delete("1.0", 'end')
            entry_text.insert("1.0", file.read())

# Change Font
def change_font(new_font):
    entry_text.configure(font=(new_font, 12))
    result_label.configure(font=(new_font, 12))
    count_label.configure(font=(new_font, 10))

# Open Font Customization Window
def open_font_customization():
    font_window = Toplevel(app)
    font_window.title("Customize Font")
    font_window.geometry("300x200")
    font_window.configure(bg='#1c1c1c')
    font_window.resizable(False, False)  # Disable window resizing
    font_window.maxsize(300, 200)  # Set the max size equal to the initial size
    font_window.minsize(300, 200)  # Set the min size equal to the initial size

    font_label = ctk.CTkLabel(font_window, text="Choose Font:", anchor='center', justify='center')
    font_label.pack(pady=20)

    font_option_menu = ctk.CTkOptionMenu(
        font_window,
        values=font.families(),
        command=change_font
    )
    font_option_menu.pack(pady=10)

    font_option_menu.set(default_font)

# Preset Shift Values
def set_shift(value):
    entry_shift.delete(0, 'end')
    entry_shift.insert(0, str(value))

# Validate Shift Input
def validate_shift(*args):
    try:
        shifts = list(map(int, entry_shift.get().split(',')))
        if any(not (0 <= shift <= 25) for shift in shifts):
            shift_warning.configure(text="Invalid shift value! Must be 0-25.")
        else:
            shift_warning.configure(text="")
    except ValueError:
        shift_warning.configure(text="Shift value must be an integer.")

# Update Character and Word Counts
def update_counts():
    text = entry_text.get("1.0", "end-1c")
    char_count = len(text)
    word_count = len(text.split())
    count_label.configure(text=f"Characters: {char_count} | Words: {word_count}")

# Show About Window
def show_about():
    about_window = Toplevel(app)
    about_window.title("About")
    about_window.geometry("300x200")
    about_window.configure(bg='#1c1c1c')  # Dark background
    about_window.resizable(False, False)  # Disable window resizing
    about_window.maxsize(300, 200)  # Set the max size equal to the initial size
    about_window.minsize(300, 200)  # Set the min size equal to the initial size

    about_label = ctk.CTkLabel(
        about_window,
        text="Caesar Cipher Tool\n\nVersion: 1.0\nAuthor: Jordan Calvert\n\nThis tool allows you to encrypt and decrypt text using the Caesar Cipher technique. It includes additional features like saving, loading, and copying results.",
        wraplength=280,
        anchor='center',
        justify='center'
    )
    about_label.pack(pady=20)

# Save Configuration Settings
def save_settings():
    config["Settings"] = {"font": default_font, "theme": ctk.get_appearance_mode()}
    with open("config.ini", "w") as configfile:
        config.write(configfile)

# Set up the customtkinter appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Initialize the main application window with fixed width
app = ctk.CTk()
app.title("Caesar Cipher Tool")
app.geometry("480x800")  # Fixed width of 480 pixels and height of 800 pixels
app.resizable(False, False)  # Disable window resizing
app.maxsize(480, 800)  # Set the max size equal to the initial size
app.minsize(480, 800)  # Set the min size equal to the initial size

# Load Configuration
config = configparser.ConfigParser()
config.read("config.ini")
default_font = config.get("Settings", "font", fallback="Consolas")
ctk.set_appearance_mode(config.get("Settings", "theme", fallback="dark"))

# Create UI elements with fixed width
entry_text = ctk.CTkTextbox(app, width=400, height=150, font=(default_font, 12))  # Slightly less than window width
entry_text.pack(pady=10)

entry_shift = ctk.CTkEntry(app, placeholder_text="Enter shift(s) (comma separated, 0-25)", width=400)
entry_shift.pack(pady=10)
entry_shift.bind("<KeyRelease>", validate_shift)

var = ctk.IntVar(value=1)
encrypt_radio = ctk.CTkRadioButton(app, text="Encrypt", variable=var, value=1, width=400)
decrypt_radio = ctk.CTkRadioButton(app, text="Decrypt", variable=var, value=2, width=400)
encrypt_radio.pack(pady=5)
decrypt_radio.pack(pady=5)

ignore_non_alpha = ctk.BooleanVar(value=False)
ignore_check = ctk.CTkCheckBox(app, text="Ignore Non-Alphabet Characters", variable=ignore_non_alpha, width=400)
ignore_check.pack(pady=5)

# Button Layout
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

process_button = ctk.CTkButton(button_frame, text="Process", command=process_cipher, width=190)
process_button.grid(row=0, column=0, padx=5, pady=5)

font_button = ctk.CTkButton(button_frame, text="Customize Font", command=open_font_customization, width=190)
font_button.grid(row=0, column=1, padx=5, pady=5)

copy_button = ctk.CTkButton(button_frame, text="Copy to Clipboard", command=copy_to_clipboard, width=190)
copy_button.grid(row=1, column=0, padx=5, pady=5)

rot13_button = ctk.CTkButton(button_frame, text="ROT13 (Shift 13)", command=lambda: set_shift(13), width=190)
rot13_button.grid(row=1, column=1, padx=5, pady=5)

save_button = ctk.CTkButton(button_frame, text="Save to File", command=save_to_file, width=190)
save_button.grid(row=2, column=0, padx=5, pady=5)

about_button = ctk.CTkButton(button_frame, text="About", command=show_about, width=190)
about_button.grid(row=2, column=1, padx=5, pady=5)

load_button = ctk.CTkButton(button_frame, text="Load from File", command=load_from_file, width=190)
load_button.grid(row=3, column=0, padx=5, pady=5)

# Empty space to align with previous button layout
empty_space = ctk.CTkLabel(button_frame, text="", width=190)
empty_space.grid(row=3, column=1, padx=5, pady=5)

# Scrollable frame for the result
result_frame = ctk.CTkScrollableFrame(app, width=400, height=200)
result_frame.pack(pady=10)

result_label = ctk.CTkLabel(result_frame, text="", wraplength=400, anchor='w', justify='left', font=(default_font, 12))
result_label.pack()

count_label = ctk.CTkLabel(app, text="Characters: 0 | Words: 0", font=(default_font, 10))
count_label.pack(pady=5)

shift_warning = ctk.CTkLabel(app, text="", text_color="red")
shift_warning.pack(pady=5)

help_label = ctk.CTkLabel(app, text="", justify='left', wraplength=400, font=(default_font, 10))
help_label.pack(pady=10)

# Save settings before closing
app.protocol("WM_DELETE_WINDOW", lambda: [save_settings(), app.destroy()])

# Run the application
app.mainloop()
