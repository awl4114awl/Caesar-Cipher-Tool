# 🧩 Caesar Cipher Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![customtkinter](https://img.shields.io/badge/GUI-customtkinter-00A0E0?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

---

## 🧠 Overview

The **Caesar Cipher Tool** is a Python-based GUI application that allows users to **encrypt and decrypt text** using the classic Caesar cipher algorithm.  
It’s designed for learning, experimentation, and simple encryption tasks — built with a modern dark-themed interface using **CustomTkinter**.

This version includes:
- 🔒 Read-only result display  
- 🎨 Font customization  
- 💾 Save and load files  
- 📋 Copy to clipboard  
- 🔁 Brute force decryption  
- 🔢 Live character and word counts  
- 🧱 Configuration persistence (`config.ini`)  

---

## ⚙️ Features

| Category | Description |
|-----------|-------------|
| **Encryption & Decryption** | Shift letters by one or more numeric values (0–25). Supports multiple comma-separated shifts. |
| **ROT13 Shortcut** | One-click button to apply a fixed shift of 13. |
| **Brute Force Mode** | Decrypt text by automatically trying all 26 possible shift values. |
| **Custom Font** | Choose any installed system font (opens in its own window). |
| **Clipboard Support** | Copy the result with a single click. |
| **File Integration** | Save encrypted/decrypted results or load text files directly. |
| **Smart Validation** | Inline feedback for invalid shifts or missing input. |
| **Config Persistence** | Remembers your font and theme preferences using a local config file. |

---

## 🖥️ Screenshots

<p align="left">
  <img src="screenshots/Screenshot 2025-11-12 134110.png" width="300">
  <img src="screenshots/Screenshot 2025-11-12 134110.png" width="300">
  <img src="screenshots/Screenshot 2025-11-12 134110.png" width="300">
</p>

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/awl4114awl/Caesar-Cipher-Tool.git
cd Caesar-Cipher-Tool
````

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the GUI

```bash
python caesar_cipher_tool.py
```

or if using the modular structure:

```bash
python -m caesar_tool.ui_app
```

---

## 🧪 Usage

1. Enter or paste your text into the **top box**.
2. Enter one or more shift values (e.g. `3` or `1,3,5`).
3. Choose **Encrypt** or **Decrypt**.
4. Click **Process** to run the cipher.
5. The **result box** will display your output (read-only).
6. Optional:

   * Click **ROT13** to apply a shift of 13.
   * Click **Brute Force (Decrypt)** to try all possible shifts.
   * Use **Customize Font** to change the text font.
   * Use **Copy**, **Save**, or **Load** buttons for convenience.

---

## 🧩 Example

**Input:**

```
Hello World
Shift: 3
Mode: Encrypt
```

**Output:**

```
Khoor Zruog
```

---

## 🧰 Tech Stack

* **Language:** Python 3.x
* **GUI Framework:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **Clipboard Utility:** [Pyperclip](https://pypi.org/project/pyperclip/)
* **Config Handling:** Python’s built-in `configparser`

---

## 🪄 File Structure

```
Caesar-Cipher-Tool/
├─ caesar_tool/
│  ├─ __init__.py
│  ├─ cipher.py          # pure, testable logic
│  ├─ ui_app.py          # GUI app (customtkinter)
│  └─ cli.py             # command-line interface
├─ tests/
│  └─ test_cipher.py     # pytest unit tests
├─ README.md
├─ requirements.txt
├─ .gitignore
└─ pyproject.toml        # optional 
```

---

## 🧩 Educational Note

> ⚠️ The Caesar cipher is **not secure** and should never be used for real encryption.
> This app is for **learning purposes only**, to understand substitution ciphers and how encryption/decryption logic works.

---

## 🏁 Version & Author

**Version:** 2.1 Stable
**Author:** Jordan Calvert
**License:** [MIT](LICENSE)

---

## 💡 Future Enhancements (Optional)

* 🔐 Add support for other ciphers (Vigenère, Atbash, etc.)
* 🌗 Add light/dark mode toggle
* ⌨️ Keyboard shortcuts for quick actions
* 🧾 Export logs or histories of processed text

---

## ⭐ Support

If you enjoy this project, consider giving it a ⭐ on GitHub!
Feedback and pull requests are always welcome.

---
