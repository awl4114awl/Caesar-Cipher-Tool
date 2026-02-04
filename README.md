# Caesar Cipher Tool

The Caesar Cipher Tool is a modern, dark-themed Windows desktop application built using Python 3.14 and CustomTkinter. Comes with a clean and efficient interface for performing classical Caesar cipher operations. This tool is part of my cybersecurity & Python development portfolio.

## Features

* Encrypt Mode: Shift plaintext forward or backward using any integer value.
* Decrypt Mode: Reverse-shifts ciphertext back into readable text.
* Brute Force Mode: Displays all 26 possible shifts inside the Result panel.
* Copy output directly with one click.
* Save Output: Export results to a `.txt` file.
* Real-Time Character / Word Counts

## Project Structure

```
Caesar-Cipher-Tool/
│
├── .idea/                      # PyCharm project settings (auto-generated)
│   ├── inspectionProfiles/
│   │   └── profiles_settings.xml
│   ├── modules.xml
│   └── vcs.xml
│
├── screenshots/                # App icons & screenshots
│   ├── icon.ico
│   ├── icon.png
│   └── Screenshot 2025-11-18 173954.png
│
├── .gitignore                  # Git ignore rules
├── LICENSE                     # MIT License
├── README.md                   # Project documentation
├── caesar_cipher_tool.py       # Main application code
└── requirements.txt            # Python dependencies
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Caesar-Cipher-Tool.git
cd Caesar-Cipher-Tool
```

2. Create a virtual environment (this is recommended)

```bash
python -m venv .venv
```

3. Activate the environment

Windows:

```bash
.\.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python caesar_cipher_tool.py
```

_The GUI launches immediately._

## How the Cipher Works

The Caesar cipher works by shifting letters by a specified number of positions:

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

## Brute Force Mode

Clicking Brute displays:

* every shift from 0 → 25
* each version on its own line
* ideal for identifying readable plaintext

Useful for:

* cybersecurity students
* CTF competitions
* introductory forensics
* solving classical cipher problems

## Output Overview — What You Can Expect to See

The Result panel displays clean, formatted cipher output depending on the selected mode.
Below is a quick comparison of how each mode behaves.

### Output Comparison Table

| Mode            | Input Example  | Output Example                                | What Happens                                                                |
| --------------- | -------------- | --------------------------------------------- | --------------------------------------------------------------------------- |
| Encrypt     | `Hello World!` | `Khoor Zruog!`                                | Each letter shifts forward by the chosen shift value.                       |
| Decrypt     | `Khoor Zruog!` | `Hello World!`                                | Letters shift backward by the given amount (or negative shift).             |
| Brute Force | `Gdkkn Vnqkc!` | `Shift  1: Hello World!` *(among 26 results)* | Shows all 26 shift possibilities so you can identify the correct plaintext. |

---

1. Encrypt / Decrypt Output

When encrypting or decrypting, the output pane displays:

* one clean result
* preserved spaces and punctuation
* unchanged non-alphabet characters
* readable blue-tinted output (Windows Utility theme)

Example:

```
Gdkkn Vnqkc!
```

---

2. Brute Force Output

Clicking Brute shows all shifts from 0 → 25:

```
Shift  0: Gdkkn Vnqkc!
Shift  1: Hello World!      ← correct plaintext
Shift  2: Ifmmp Xpsme!
...
Shift 25: Fcjjm Umpjb!
```

Useful for solving:

* CTF crypto challenges
* classical ciphers
* basic digital forensics
* unknown-shift messages

---

3. Copy & Save Output

* Copy → sends the output directly to your clipboard
* Save → exports the result as a `.txt` file

The status bar confirms each action.

## License

This project is released under the MIT License. See [`LICENSE`](LICENSE) for details.
