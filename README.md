# 🪛 **Caesar Cipher Tool**

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge\&logo=python\&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-0A84FF?style=for-the-badge)
![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge&logo=windows11)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🧠 Overview

The **Caesar Cipher Tool** is a modern, dark-themed Windows desktop application built using **Python 3.14** and **CustomTkinter**.
It provides a clean and efficient interface for performing classical Caesar cipher operations, including:

* Encrypting plaintext by shifting characters
* Decrypting ciphertext by applying the inverse shift
* Brute-forcing all 26 shifts directly within the main window
* Copying or saving results
* Viewing real-time character and word counts

This tool is part of my cybersecurity & Python development portfolio — demonstrating GUI design, utility-tool aesthetics, and classical cryptography principles.

---

## 🖼️ GUI Preview

<p align="left">
  <img src="screenshots/Screenshot 2025-11-18 181539.png" width="500">
</p>

---

## 🧩 App Icon

<p align="left">
  <img src="screenshots/icon.ico" width="50">
  <img src="screenshots/icon.png" width="200">
</p>

---

## 🚀 Features

### ✔ **Encrypt Mode**

Shift plaintext forward or backward using any integer value.

### ✔ **Decrypt Mode**

Reverse-shifts ciphertext back into readable text.

### ✔ **Brute Force Mode**

Displays **all 26 possible shifts** inside the Result panel — ideal for CTFs and classical crypto challenges.

### ✔ **Clipboard Support**

Copy output directly with one click.

### ✔ **Save Output**

Export results to a `.txt` file.

### ✔ **Real-Time Character / Word Counts**

Perfect for analysis and text processing.

### ✔ **Fully Styled Modern GUI**

Windows utility–style theming for consistency across tools.

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
│   └── Screenshot 2025-11-18 173954.png
└── .venv/
```
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

The GUI launches immediately.

---

## 🔐 How the Cipher Works

The **Caesar cipher** works by shifting letters by a specified number of positions:

```
Shift 3:
A → D
B → E
C → F
...
```

The tool supports:

* uppercase letters
* lowercase letters
* negative and large shifts
* leaving non-alphabetic characters untouched

---

## 🧪 Brute Force Mode

Clicking **Brute** displays:

* every shift from **0 → 25**
* each version on its own line
* ideal for identifying readable plaintext

Useful for:

* cybersecurity students
* CTF competitions
* introductory forensics
* solving classical cipher problems

---

## 📜 License

This project is licensed under the **MIT License**.

---
