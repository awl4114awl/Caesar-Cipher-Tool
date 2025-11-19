"""
Caesar Cipher Tool
Dark Windows Utility Theme (matches Active Network & Fingerprint Scanner)
Python 3.14 + customtkinter
"""

import customtkinter as ctk
from tkinter import messagebox
import ctypes
import os


# ------------------------------------------------------------
#  Paths / Icon
# ------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_DIR, "screenshots", "icon.ico")


# ------------------------------------------------------------
#  Dark Windows Utility Theme (EXACT scanner app match)
# ------------------------------------------------------------
BG_MAIN        = "#1b1b1b"   # main window background
BG_PANEL       = "#242424"   # panel / frame background
BG_CONTROL     = "#1f1f1f"   # entries, buttons, textboxes
BG_CONTROL_HOV = "#2a2a2a"   # hover color
BORDER_COLOR   = "#5a5a5a"   # thin border identical to scanner
TEXT_MAIN      = "#f2f2f2"
TEXT_MUTED     = "#c0c0c0"


# ------------------------------------------------------------
#  Cipher Logic
# ------------------------------------------------------------
def caesar_shift(text: str, shift: int) -> str:
    result = []
    shift = shift % 26

    for ch in text:
        if "A" <= ch <= "Z":
            base = ord("A")
            result.append(chr(base + ((ord(ch) - base + shift) % 26)))
        elif "a" <= ch <= "z":
            base = ord("a")
            result.append(chr(base + ((ord(ch) - base + shift) % 26)))
        else:
            result.append(ch)

    return "".join(result)


# ------------------------------------------------------------
#  GUI Application
# ------------------------------------------------------------
class CaesarCipherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Proper Windows taskbar icon
        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                "CaesarCipherTool.DarkUtility"
            )
        except Exception:
            pass

        self.title("Caesar Cipher Tool")

        if os.path.exists(ICON_PATH):
            try:
                self.iconbitmap(ICON_PATH)
            except:
                pass

        self.geometry("650x440")
        self.resizable(False, False)

        # customtkinter global settings
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.configure(fg_color=BG_MAIN)
        self._font_label = ("Segoe UI", 11)
        self._font_mono = ("Consolas", 12)

        # Grid setup
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(2, weight=1)

        self._build_header()
        self._build_controls()
        self._build_text_areas()
        self._build_footer()


    # --------------------------------------------------------
    #  Header (scanner-style)
    # --------------------------------------------------------
    def _build_header(self):
        frame = ctk.CTkFrame(
            self, fg_color=BG_PANEL,
            border_color=BORDER_COLOR,
            border_width=1,
            corner_radius=0
        )
        frame.grid(row=0, column=0, columnspan=2,
                   padx=8, pady=(8, 4), sticky="ew")

        title = ctk.CTkLabel(
            frame,
            text="Caesar Cipher Tool",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT_MAIN
        )
        title.grid(row=0, column=0, sticky="w", padx=10, pady=(6, 0))

        subtitle = ctk.CTkLabel(
            frame,
            text="Encrypt / Decrypt • Brute Force • Windows Utility UI",
            font=("Segoe UI", 10),
            text_color=TEXT_MUTED
        )
        subtitle.grid(row=1, column=0, sticky="w", padx=10, pady=(0, 6))


    # --------------------------------------------------------
    #  Mode selector + Shift (scanner-style)
    # --------------------------------------------------------
    def _build_controls(self):
        frame = ctk.CTkFrame(
            self, fg_color=BG_PANEL,
            border_color=BORDER_COLOR,
            border_width=1,
            corner_radius=0
        )
        frame.grid(row=1, column=0, columnspan=2,
                   padx=8, pady=(0, 4), sticky="ew")

        frame.grid_columnconfigure((0,1,2,3), weight=1)

        # Mode label
        mode_label = ctk.CTkLabel(
            frame,
            text="Mode:",
            font=self._font_label,
            text_color=TEXT_MUTED
        )
        mode_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.mode_var = ctk.StringVar(value="Encrypt")

        # Tab-style mode buttons (EXACT scanner style)
        def tab_style(selected):
            return dict(
                fg_color=("#2a2a2a" if selected else BG_CONTROL),
                hover_color=BG_CONTROL_HOV,
                border_color=BORDER_COLOR,
                border_width=1,
                corner_radius=3,
                text_color=TEXT_MAIN,
                font=("Segoe UI", 10),
                width=75
            )

        self.enc_btn = ctk.CTkButton(
            frame,
            text="Encrypt",
            command=lambda: self._set_mode("Encrypt"),
            **tab_style(True)
        )
        self.enc_btn.grid(row=0, column=1, padx=4)

        self.dec_btn = ctk.CTkButton(
            frame,
            text="Decrypt",
            command=lambda: self._set_mode("Decrypt"),
            **tab_style(False)
        )
        self.dec_btn.grid(row=0, column=2, padx=4)

        # Shift label
        shift_label = ctk.CTkLabel(
            frame,
            text="Shift:",
            font=self._font_label,
            text_color=TEXT_MUTED
        )
        shift_label.grid(row=0, column=3, sticky="e", padx=(0, 6))

        # Shift entry
        self.shift_entry = ctk.CTkEntry(
            frame,
            width=70,
            fg_color=BG_CONTROL,
            border_color=BORDER_COLOR,
            border_width=1,
            corner_radius=3,
            text_color=TEXT_MAIN,
            font=self._font_mono,
            justify="center"
        )
        self.shift_entry.insert(0, "3")
        self.shift_entry.grid(row=0, column=4, sticky="w", padx=(0, 10))


    def _set_mode(self, mode):
        self.mode_var.set(mode)

        # Update tab appearance
        self.enc_btn.configure(
            fg_color="#2a2a2a" if mode == "Encrypt" else BG_CONTROL
        )
        self.dec_btn.configure(
            fg_color="#2a2a2a" if mode == "Decrypt" else BG_CONTROL
        )


    # --------------------------------------------------------
    #  Text Areas (scanner-style textboxes)
    # --------------------------------------------------------
    def _build_text_areas(self):
        frame = ctk.CTkFrame(
            self, fg_color=BG_PANEL,
            border_color=BORDER_COLOR,
            border_width=1,
            corner_radius=0
        )
        frame.grid(row=2, column=0, columnspan=2,
                   padx=8, pady=(0, 4), sticky="nsew")

        frame.grid_columnconfigure((0, 1), weight=1)
        frame.grid_rowconfigure(1, weight=1)

        in_label = ctk.CTkLabel(
            frame,
            text="Plaintext / Ciphertext",
            text_color=TEXT_MUTED,
            font=self._font_label
        )
        in_label.grid(row=0, column=0, sticky="w", padx=10, pady=(6,2))

        out_label = ctk.CTkLabel(
            frame,
            text="Result",
            text_color=TEXT_MUTED,
            font=self._font_label
        )
        out_label.grid(row=0, column=1, sticky="w", padx=10, pady=(6,2))

        # Input textbox
        self.input_box = ctk.CTkTextbox(
            frame,
            fg_color=BG_CONTROL,
            border_color=BORDER_COLOR,
            border_width=1,
            corner_radius=3,
            text_color=TEXT_MAIN,
            font=self._font_mono,
            wrap="word",
            height=160
        )
        self.input_box.grid(row=1, column=0,
                            padx=(10, 4), pady=(2, 8), sticky="nsew")
        self.input_box.bind("<KeyRelease>", self.update_counts)

        # Output textbox (read-only)
        self.output_box = ctk.CTkTextbox(
            frame,
            fg_color=BG_CONTROL,
            border_color=BORDER_COLOR,
            border_width=1,
            corner_radius=3,
            text_color="#8bbcff",      # scanner-style highlight color
            font=self._font_mono,
            wrap="word",
            height=160
        )
        self.output_box.grid(row=1, column=1,
                             padx=(4, 10), pady=(2, 8), sticky="nsew")
        self.output_box.configure(state="disabled")


    # --------------------------------------------------------
    #  Footer Buttons (EXACT scanner style)
    # --------------------------------------------------------
    def _build_footer(self):
        frame = ctk.CTkFrame(
            self, fg_color=BG_PANEL,
            border_color=BORDER_COLOR,
            border_width=1,
            corner_radius=0
        )
        frame.grid(row=3, column=0, columnspan=2,
                   padx=8, pady=(0, 8), sticky="ew")

        frame.grid_columnconfigure(0, weight=1)

        # Status label
        self.status_label = ctk.CTkLabel(
            frame,
            text="ready",
            font=("Segoe UI", 10),
            text_color=TEXT_MUTED,
            anchor="w"
        )
        self.status_label.grid(row=0, column=0, sticky="w", padx=10, pady=6)

        # Button style (EXACT scanner style)
        btn_cfg = dict(
            fg_color=BG_CONTROL,
            hover_color=BG_CONTROL_HOV,
            border_color=BORDER_COLOR,
            border_width=1,
            corner_radius=3,
            text_color=TEXT_MAIN,
            font=("Segoe UI", 10),
            width=90,
            height=32
        )

        ctk.CTkButton(frame, text="Run", command=self.run_cipher, **btn_cfg)\
            .grid(row=0, column=1, padx=4)

        ctk.CTkButton(frame, text="Brute", command=self.brute_force_view, **btn_cfg)\
            .grid(row=0, column=2, padx=4)

        ctk.CTkButton(frame, text="Clear", command=self.clear_all, **btn_cfg)\
            .grid(row=0, column=3, padx=4)

        ctk.CTkButton(frame, text="Copy", command=self.copy_result, **btn_cfg)\
            .grid(row=0, column=4, padx=4)

        ctk.CTkButton(frame, text="Save", command=self.save_result, **btn_cfg)\
            .grid(row=0, column=5, padx=(4, 10))


    # --------------------------------------------------------
    #  Logic / Handlers
    # --------------------------------------------------------
    def run_cipher(self):
        text = self.input_box.get("1.0", "end-1c")
        mode = self.mode_var.get()
        raw_shift = self.shift_entry.get().strip()

        if not raw_shift:
            messagebox.showwarning("Shift Required", "Please enter a shift value.")
            return

        try:
            shift = int(raw_shift)
        except ValueError:
            messagebox.showerror("Invalid Shift", "Shift must be an integer.")
            return

        if mode == "Decrypt":
            shift = -shift

        result = caesar_shift(text, shift)

        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", result)
        self.output_box.configure(state="disabled")

        self.status_label.configure(text=f"{mode.lower()}ed with shift {raw_shift}")


    def update_counts(self, _event=None):
        text = self.input_box.get("1.0", "end-1c")
        chars = len(text)
        words = len(text.split())
        self.status_label.configure(text=f"{chars} chars | {words} words")


    def clear_all(self):
        self.input_box.delete("1.0", "end")
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.configure(state="disabled")
        self.status_label.configure(text="cleared")


    def copy_result(self):
        output = self.output_box.get("1.0", "end-1c").strip()
        if not output:
            self.status_label.configure(text="nothing to copy")
            return

        try:
            import pyperclip
            pyperclip.copy(output)
            self.status_label.configure(text="copied to clipboard")
        except Exception:
            self.status_label.configure(text="copy failed (pyperclip missing?)")


    def save_result(self):
        from tkinter import filedialog
        result = self.output_box.get("1.0", "end-1c").strip()

        if not result:
            self.status_label.configure(text="nothing to save")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(result)
            self.status_label.configure(text=f"saved to {file_path}")


    def brute_force_view(self):
        text = self.input_box.get("1.0", "end-1c")

        if not text.strip():
            messagebox.showinfo("No Text", "Enter some ciphertext or plaintext to brute force.")
            return

        lines = [f"Shift {s:2d}: {caesar_shift(text, s)}" for s in range(26)]
        result_text = "\n".join(lines)

        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", result_text)
        self.output_box.configure(state="disabled")

        self.status_label.configure(text="brute-forced shifts 0–25")


# ------------------------------------------------------------
#  Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    app = CaesarCipherApp()
    app.mainloop()