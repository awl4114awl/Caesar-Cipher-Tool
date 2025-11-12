# caesar_tool/ui_app.py
import customtkinter as ctk
from tkinter import filedialog, font as tkfont, Toplevel
import configparser
import pyperclip
from .cipher import caesar, brute_force

APP_W, APP_H = 520, 840

class CaesarGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Caesar Cipher Tool")
        self.geometry(f"{APP_W}x{APP_H}")
        self.resizable(False, False)
        self.maxsize(APP_W, APP_H)
        self.minsize(APP_W, APP_H)

        # theme & config
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.default_font = self.config.get("Settings", "font", fallback="Consolas")
        ctk.set_appearance_mode(self.config.get("Settings", "theme", fallback="dark"))

        self._build_ui()
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    # ---------------- UI ----------------
    def _build_ui(self):
        pad = {"pady": 8}

        self.entry_text = ctk.CTkTextbox(self, width=440, height=160, font=(self.default_font, 12))
        self.entry_text.pack(**pad)

        self.entry_shift = ctk.CTkEntry(self, placeholder_text="Enter shift(s) (comma separated, 0-25)", width=440)
        self.entry_shift.pack(**pad)
        self.entry_shift.bind("<KeyRelease>", lambda e: self._validate_shift())

        # options
        self.mode_var = ctk.StringVar(value="encrypt")
        radios = ctk.CTkFrame(self)
        radios.pack(**pad)
        ctk.CTkRadioButton(radios, text="Encrypt", variable=self.mode_var, value="encrypt", width=210).grid(row=0, column=0, padx=6)
        ctk.CTkRadioButton(radios, text="Decrypt", variable=self.mode_var, value="decrypt", width=210).grid(row=0, column=1, padx=6)

        self.ignore_nonalpha = ctk.BooleanVar(value=True)
        self.advance_on_nonalpha = ctk.BooleanVar(value=False)
        toggles = ctk.CTkFrame(self)
        toggles.pack(**pad)
        ctk.CTkCheckBox(toggles, text="Ignore non-letters (don’t consume shift)", variable=self.ignore_nonalpha).grid(row=0, column=0, padx=6)
        ctk.CTkCheckBox(toggles, text="Advance shift on non-letters", variable=self.advance_on_nonalpha).grid(row=0, column=1, padx=6)

        # buttons
        buttons = ctk.CTkFrame(self)
        buttons.pack(**pad)
        ctk.CTkButton(buttons, text="Process", command=self._process, width=210).grid(row=0, column=0, padx=6, pady=6)
        ctk.CTkButton(buttons, text="ROT13", command=lambda: self._set_shift(13), width=210).grid(row=0, column=1, padx=6, pady=6)
        ctk.CTkButton(buttons, text="Brute Force (Decrypt)", command=self._brute_force, width=210).grid(row=1, column=0, padx=6, pady=6)
        ctk.CTkButton(buttons, text="Customize Font", command=self._open_font_customization, width=210).grid(row=1, column=1, padx=6, pady=6)
        ctk.CTkButton(buttons, text="Copy Result", command=self._copy, width=210).grid(row=2, column=0, padx=6, pady=6)
        ctk.CTkButton(buttons, text="Save Result", command=self._save, width=210).grid(row=2, column=1, padx=6, pady=6)
        ctk.CTkButton(buttons, text="Load Text", command=self._load, width=210).grid(row=3, column=0, padx=6, pady=6)
        ctk.CTkButton(buttons, text="About", command=self._about, width=210).grid(row=3, column=1, padx=6, pady=6)

        # warning + counts
        self.shift_warning = ctk.CTkLabel(self, text="", text_color="red")
        self.shift_warning.pack(**pad)

        self.count_label = ctk.CTkLabel(self, text="Characters: 0 | Words: 0", font=(self.default_font, 10))
        self.count_label.pack(**pad)

        # result area (read-only)
        self.result_text = ctk.CTkTextbox(self, width=440, height=280, font=(self.default_font, 12))
        self.result_text.insert("1.0", "(Results will appear here...)")
        self.result_text.configure(state="disabled", text_color="#cccccc")  # 🔒 read-only placeholder
        self.result_text.pack(pady=10)

        self.help_label = ctk.CTkLabel(self, text="Tip: Multiple shifts are cycled. Example: 1,3,5", wraplength=440)
        self.help_label.pack(pady=6)

        # live counts
        self.entry_text.bind("<KeyRelease>", lambda e: self._update_counts())
        self._update_counts()

    # ---------------- actions ----------------
    def _parse_shifts(self):
        raw = self.entry_shift.get().strip()
        if not raw:
            raise ValueError("Enter at least one shift (0–25).")
        shifts = []
        for part in raw.split(","):
            part = part.strip()
            if not part:
                continue
            val = int(part)
            if not (0 <= val <= 25):
                raise ValueError("All shift values must be between 0 and 25.")
            shifts.append(val)
        if not shifts:
            raise ValueError("No valid shifts provided.")
        return shifts

    def _process(self):
        try:
            text = self.entry_text.get("1.0", "end-1c")
            if not text.strip():
                self._set_result("(Please enter text above first.)", placeholder=True)
                return
            shifts = self._parse_shifts()
            mode = self.mode_var.get()
            out = caesar(
                text,
                shifts,
                encrypt=(mode == "encrypt"),
                ignore_nonalpha=self.ignore_nonalpha.get(),
                advance_on_nonalpha=self.advance_on_nonalpha.get(),
            )
            self._set_result(out)
        except Exception as e:
            self._set_result(f"[Error] {e}")

    def _brute_force(self):
        text = self.entry_text.get("1.0", "end-1c")
        if not text.strip():
            self._set_result("(Please enter text above first.)", placeholder=True)
            return
        results = brute_force(text)
        listing = "\n".join([f"Shift {k:2d}: {res}" for k, res in enumerate(results)])
        self._set_result(listing)

    def _set_result(self, s: str, placeholder=False):
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        color = "#cccccc" if placeholder else "#ffffff"
        self.result_text.insert("1.0", s)
        self.result_text.configure(state="disabled", text_color=color)

    def _copy(self):
        pyperclip.copy(self.result_text.get("1.0", "end-1c"))

    def _save(self):
        text = self.result_text.get("1.0", "end-1c")
        if not text or "(Results will appear here" in text:
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)

    def _load(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            with open(path, "r", encoding="utf-8") as f:
                self.entry_text.delete("1.0", "end")
                self.entry_text.insert("1.0", f.read())
            self._update_counts()

    def _open_font_customization(self):
        win = Toplevel(self)
        win.title("Customize Font")
        win.geometry("360x220")
        win.configure(bg="#1c1c1c")
        win.resizable(False, False)

        ctk.CTkLabel(win, text="Choose Font:", anchor="center").pack(pady=16)
        families = sorted(set(tkfont.families()))
        option = ctk.CTkOptionMenu(win, values=families, command=self._change_font)
        option.pack(pady=10)
        option.set(self.default_font)

    def _change_font(self, new_font: str):
        self.default_font = new_font
        self.entry_text.configure(font=(new_font, 12))
        self.result_text.configure(font=(new_font, 12))
        self.count_label.configure(font=(new_font, 10))

    def _about(self):
        win = Toplevel(self)
        win.title("About")
        win.geometry("360x240")
        win.configure(bg="#1c1c1c")
        win.resizable(False, False)
        text = (
            "Caesar Cipher Tool\n\n"
            "Version: 2.1\n"
            "Author: Jordan Calvert\n\n"
            "Encrypt/decrypt using Caesar cipher. Supports multiple shift values, "
            "brute-force decrypt, configurable handling of non-letters, and font customization."
        )
        ctk.CTkLabel(win, text=text, wraplength=320, anchor="center", justify="center").pack(pady=20)

    def _validate_shift(self):
        try:
            _ = self._parse_shifts()
            self.shift_warning.configure(text="")
        except Exception as e:
            self.shift_warning.configure(text=str(e))

    def _update_counts(self):
        text = self.entry_text.get("1.0", "end-1c")
        chars = len(text)
        words = len(text.split())
        self.count_label.configure(text=f"Characters: {chars} | Words: {words}")

    def _on_close(self):
        if "Settings" not in self.config:
            self.config["Settings"] = {}
        self.config["Settings"]["font"] = self.default_font
        self.config["Settings"]["theme"] = ctk.get_appearance_mode()
        with open("config.ini", "w", encoding="utf-8") as f:
            self.config.write(f)
        self.destroy()

def main():
    app = CaesarGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
