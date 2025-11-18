"""
Caesar Cipher Tool (Dark Famicom Retro Theme)
Python 3.14 + customtkinter

- Encrypt / Decrypt text with a Caesar cipher
- Dark retro Nintendo-inspired theme
- Red + purple Famicom/SNES accents
- Copy, Save, Word/Char count, Brute Force
"""

import customtkinter as ctk
from tkinter import messagebox


# ---------------------- Retro Famicom Dark Theme ---------------------- #
APP_BG         = "#1b1a17"   # warm, deep charcoal
HEADER_BG      = "#252422"   # darker plastic console panel
PANEL_BG       = "#2b2a27"   # mid-dark warm paneling
TEXTBOX_BG     = "#2e2c29"   # slightly lighter box
BORDER_COLOR   = "#403d39"   # soft warm-gray border

ACCENT_RED     = "#d8352c"   # famicom red
ACCENT_RED_HOV = "#e14a41"   # lifted hover red

ACCENT_PURPLE     = "#6b6478"  # nes modifier purple
ACCENT_PURPLE_HOV = "#7b728c"  # hover

TEXT_MAIN      = "#e8e6df"   # off-white warm
TEXT_MUTED     = "#b8b5ad"   # muted warm-gray


# ---------------------- Cipher Logic ---------------------- #
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


# ---------------------- GUI Class ---------------------- #
class CaesarCipherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Caesar Cipher Tool")
        self.title("Caesar Cipher Tool")
        self.iconbitmap("screenshots/icon.ico")
        self.geometry("640x430")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.configure(fg_color=APP_BG)
        self._mono_font = ("Consolas", 12)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self._build_controls()
        self._build_text_areas()
        self._build_footer()

    # ---------------- Header ---------------- #
    def _build_header(self):
        header_frame = ctk.CTkFrame(self, fg_color=HEADER_BG, corner_radius=10)
        header_frame.grid(row=0, column=0, columnspan=2,
                          padx=12, pady=(10, 6), sticky="nsew")

        header_frame.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            header_frame,
            text="🧩 Caesar Cipher",
            font=("Consolas", 16, "bold"),
            text_color=ACCENT_RED
        )
        title_label.grid(row=0, column=0, sticky="w", padx=10, pady=(6, 0))

        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Dark Famicom Retro Theme – Python 3.14",
            font=("Consolas", 11),
            text_color=TEXT_MUTED
        )
        subtitle_label.grid(row=1, column=0, sticky="w", padx=10, pady=(0, 6))

    # ---------------- Controls ---------------- #
    def _build_controls(self):
        controls_frame = ctk.CTkFrame(self, fg_color=PANEL_BG, corner_radius=10)
        controls_frame.grid(row=1, column=0, columnspan=2,
                            padx=12, pady=(0, 6), sticky="ew")

        controls_frame.grid_columnconfigure(0, weight=1)
        controls_frame.grid_columnconfigure(1, weight=1)
        controls_frame.grid_columnconfigure(2, weight=1)
        controls_frame.grid_columnconfigure(3, weight=1)

        # Mode Label
        mode_label = ctk.CTkLabel(
            controls_frame,
            text="Mode",
            font=self._mono_font,
            text_color=TEXT_MUTED
        )
        mode_label.grid(row=0, column=0, sticky="w", padx=(10, 4), pady=6)

        self.mode_var = ctk.StringVar(value="Encrypt")

        # Mode Switch
        self.mode_seg = ctk.CTkSegmentedButton(
            controls_frame,
            values=["Encrypt", "Decrypt"],
            variable=self.mode_var,
            fg_color=TEXTBOX_BG,
            selected_color=ACCENT_RED,
            selected_hover_color=ACCENT_RED_HOV,
            unselected_color=PANEL_BG,
            unselected_hover_color="#3a3835",
            font=("Consolas", 11),
            text_color=TEXT_MAIN
        )
        self.mode_seg.grid(row=0, column=1, sticky="w", padx=(0, 10), pady=6)

        # Shift Label
        shift_label = ctk.CTkLabel(
            controls_frame,
            text="Shift",
            font=self._mono_font,
            text_color=TEXT_MUTED
        )
        shift_label.grid(row=0, column=2, sticky="e", padx=(10, 4), pady=6)

        # Shift Entry
        self.shift_entry = ctk.CTkEntry(
            controls_frame,
            width=60,
            fg_color=TEXTBOX_BG,
            text_color=TEXT_MAIN,
            border_color=ACCENT_RED,
            border_width=1,
            font=self._mono_font,
            justify="center"
        )
        self.shift_entry.insert(0, "3")
        self.shift_entry.grid(row=0, column=3, sticky="w", padx=(0, 10), pady=6)

    # ---------------- Text Areas ---------------- #
    def _build_text_areas(self):
        text_frame = ctk.CTkFrame(self, fg_color=PANEL_BG, corner_radius=10)
        text_frame.grid(row=2, column=0, columnspan=2,
                        padx=12, pady=(0, 6), sticky="nsew")

        text_frame.grid_columnconfigure(0, weight=1)
        text_frame.grid_columnconfigure(1, weight=1)
        text_frame.grid_rowconfigure(1, weight=1)

        in_label = ctk.CTkLabel(
            text_frame,
            text="Plaintext / Ciphertext",
            font=self._mono_font,
            text_color=TEXT_MUTED
        )
        in_label.grid(row=0, column=0, sticky="w", padx=10, pady=(6, 2))

        out_label = ctk.CTkLabel(
            text_frame,
            text="Result",
            font=self._mono_font,
            text_color=TEXT_MUTED
        )
        out_label.grid(row=0, column=1, sticky="w", padx=10, pady=(6, 2))

        # Input box
        self.input_box = ctk.CTkTextbox(
            text_frame,
            fg_color=TEXTBOX_BG,
            text_color=TEXT_MAIN,
            border_color=BORDER_COLOR,
            border_width=1,
            font=self._mono_font,
            wrap="word",
            corner_radius=8,
            height=155
        )
        self.input_box.grid(row=1, column=0, padx=(10, 5), pady=(0, 8), sticky="nsew")
        self.input_box.bind("<KeyRelease>", self.update_counts)

        # Output box
        self.output_box = ctk.CTkTextbox(
            text_frame,
            fg_color=TEXTBOX_BG,
            text_color=ACCENT_RED,
            border_color=BORDER_COLOR,
            border_width=1,
            font=self._mono_font,
            wrap="word",
            corner_radius=8,
            height=155
        )
        self.output_box.grid(row=1, column=1, padx=(5, 10), pady=(0, 8), sticky="nsew")
        self.output_box.configure(state="disabled")

    # ---------------- Footer ---------------- #
    def _build_footer(self):
        footer_frame = ctk.CTkFrame(self, fg_color=PANEL_BG, corner_radius=10)
        footer_frame.grid(row=3, column=0, columnspan=2,
                          padx=12, pady=(0, 10), sticky="ew")

        footer_frame.grid_columnconfigure(0, weight=1)
        for i in range(1, 7):
            footer_frame.grid_columnconfigure(i, weight=0)

        self.status_label = ctk.CTkLabel(
            footer_frame,
            text="ready",
            font=("Consolas", 11),
            text_color=TEXT_MUTED,
            anchor="w",
            width=350
        )
        self.status_label.grid(row=0, column=0, sticky="w", padx=14, pady=6)

        # Buttons
        run_btn = ctk.CTkButton(
            footer_frame,
            text="Run",
            command=self.run_cipher,
            fg_color=ACCENT_RED,
            hover_color=ACCENT_RED_HOV,
            text_color="#ffffff",
            font=self._mono_font,
            width=75,
            corner_radius=8
        )
        run_btn.grid(row=0, column=1, padx=(0, 6), pady=6)

        brute_btn = ctk.CTkButton(
            footer_frame,
            text="Brute Force",
            command=self.brute_force_view,
            fg_color=ACCENT_PURPLE,
            hover_color=ACCENT_PURPLE_HOV,
            text_color="#ffffff",
            font=self._mono_font,
            width=95,
            corner_radius=8
        )
        brute_btn.grid(row=0, column=2, padx=(0, 6), pady=6)

        clear_btn = ctk.CTkButton(
            footer_frame,
            text="Clear",
            command=self.clear_all,
            fg_color=ACCENT_PURPLE,
            hover_color=ACCENT_PURPLE_HOV,
            text_color="#ffffff",
            font=self._mono_font,
            width=70,
            corner_radius=8
        )
        clear_btn.grid(row=0, column=3, padx=(0, 6), pady=6)

        copy_btn = ctk.CTkButton(
            footer_frame,
            text="Copy",
            command=self.copy_result,
            fg_color=ACCENT_PURPLE,
            hover_color=ACCENT_PURPLE_HOV,
            text_color="#ffffff",
            font=self._mono_font,
            width=70,
            corner_radius=8
        )
        copy_btn.grid(row=0, column=4, padx=(0, 6), pady=6)

        save_btn = ctk.CTkButton(
            footer_frame,
            text="Save",
            command=self.save_result,
            fg_color=ACCENT_PURPLE,
            hover_color=ACCENT_PURPLE_HOV,
            text_color="#ffffff",
            font=self._mono_font,
            width=70,
            corner_radius=8
        )
        save_btn.grid(row=0, column=5, padx=(0, 10), pady=6)

        self.bind("<Control-Return>", lambda _event: self.run_cipher())

    # ---------------- Copy to Clipboard ---------------- #
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
            self.status_label.configure(text="copy failed")

    # ---------------- Save to File ---------------- #
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

    # ---------------- Logic Callbacks ---------------- #
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

    def brute_force_view(self):
        """Show all 26 possible shifts directly in the output box."""
        text = self.input_box.get("1.0", "end-1c")

        if not text.strip():
            messagebox.showinfo("No Text", "Enter some ciphertext or plaintext to brute force.")
            return

        # Build brute-force list
        lines = []
        for s in range(26):
            lines.append(f"Shift {s:2d}: {caesar_shift(text, s)}")

        result_text = "\n".join(lines)

        # Display inside the main output box
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", result_text)
        self.output_box.configure(state="disabled")

        # Update status
        self.status_label.configure(text="brute-forced all shifts 0–25")


# ---------------- Entry Point ---------------- #
if __name__ == "__main__":
    app = CaesarCipherApp()
    app.mainloop()