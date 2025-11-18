# 🧩 **Caesar Cipher Tool**

### *Dark Famicom Retro Theme – Python 3.14*

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge\&logo=python\&logoColor=white)
![customtkinter](https://img.shields.io/badge/GUI-CustomTkinter-5A5A5A?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-3b82f6?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🎮 Overview

The **Caesar Cipher Tool** is a retro-styled, modern dark-mode GUI application built with **Python 3.14** and **CustomTkinter**.
It allows users to:

* Encrypt text using Caesar shift
* Decrypt ciphertext
* Automatically brute-force all 26 possible shifts inside the main window
* Copy results
* Save results
* Enjoy a clean, compact, Famicom-inspired retro interface

This tool was built as part of my cybersecurity/python portfolio — demonstrating GUI development, clean UI design, and classical cryptography concepts.

---

## 🎨 Retro Theme (Dark Famicom)

The entire GUI is styled after classic Nintendo hardware colors:

* dark charcoal shell
* muted warm accents
* red function buttons
* soft round corners
* console-style icon in the title bar

This gives the tool a unique “retro hardware utility” vibe while remaining clean and modern.

---

## 🖼️ GUI Preview


<p align="left">
  <img src="screenshots/Screenshot 2025-11-18 114400.png" width="500">
  <img src="screenshots/Screenshot 2025-11-18 123907.png" width="500">
</p>

---

## 🧩 App Icon

<p align="left">
  <img src="screenshots/icon.ico" width="50">
  <img src="screenshots/icon.png" width="200">
</p>

---

## 🚀 Features

### **✔ Encrypt Mode**

Shift plaintext by any positive or negative integer.

### **✔ Decrypt Mode**

Reverse-shifts ciphertext back to readable text.

### **✔ Brute Force Mode**

Displays **all 26 shift possibilities** directly inside the main Result panel.

### **✔ Clipboard Support**

Quickly copy output via the `Copy` button.

### **✔ Save Output**

Export the Result panel to a `.txt` file.

### **✔ Real-Time Character/Word Count**

Helpful when analyzing text samples or cryptography puzzles.

### **✔ Fully Resizable Text Panels**

Dark, minimal, retro-themed UI.

### **✔ Custom App Icon**

Matching retro Famicom-inspired icon included.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Caesar-Cipher-Tool.git
cd Caesar-Cipher-Tool
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows:**

```bash
.\.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python caesar_cipher_tool.py
```

The GUI will launch immediately.

---

## 🔐 How the Cipher Works

The **Caesar cipher** shifts each letter by a given amount:

```
Shift 3:
A → D
B → E
C → F
...
```

The app supports:

* uppercase
* lowercase
* negative shifts
* brute-forcing unknown ciphertext

Non-alphabet characters remain unchanged.

---

## 🧪 Brute Force Mode

When you click **Brute Force**, the tool runs:

* all shifts from **0 to 25**
* displays them inline in the Result panel
* highlights recognition patterns manually

This is extremely useful for:

* cybersecurity students
* CTF challenges
* forensics
* solving classical cipher puzzles

---

## 📁 Project Structure

```
Caesar-Cipher-Tool/
│
├── .gitignore
├── requirements.txt
├── caesar_cipher_tool.py
├── screenshots/
│   ├── icon.ico
│   ├── icon.png
│   └── screenshot.png
└── .venv/
```

---

## 🛠️ Technologies Used

* **Python 3.14**
* **CustomTkinter** (modern themed Tkinter widgets)
* **Pillow** (for app icon)
* **Pyperclip** (clipboard support)

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Acknowledgments

* Inspired by classic retro consoles (Famicom/Super Famicom)
* Built to enhance my **cybersecurity + Python GUI portfolio**
* Designed fully custom: color theme, window layout, and icon

---