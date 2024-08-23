# Caesar Cipher Tool

## Overview

The Caesar Cipher Tool is a versatile and user-friendly application designed to perform encryption and decryption using the Caesar Cipher technique. The tool allows you to easily transform text by shifting its letters by a specified number of positions. This application also provides several features, such as saving and loading text files, copying results to the clipboard, and customizing the font used in the UI. The tool is built using `customtkinter`, a modern, customizable GUI library for Python.

## Features

- **Caesar Cipher Encryption/Decryption**: Encrypt or decrypt text by shifting letters according to specified shift values.
- **Customizable Shifts**: Specify one or more shift values (comma-separated) to customize the transformation.
- **Ignore Non-Alphabet Characters**: Option to ignore non-alphabet characters (e.g., numbers, punctuation) during encryption/decryption.
- **Clipboard Integration**: Copy the encrypted or decrypted text directly to your clipboard.
- **Save and Load Text Files**: Save the result to a text file or load text from a file for encryption/decryption.
- **Font Customization**: Customize the font used in the text areas through a simple UI.
- **Dark Mode UI**: The application features a sleek, dark-themed user interface.
- **Non-Resizable Windows**: The main application window, About window, and font customization window are fixed in size, preventing resizing for a consistent UI experience.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Ensure `pip` is installed to manage Python packages.

### Clone the Repository

Clone the repository from GitHub using the following command:

```bash
git clone https://github.com/awl4114awl/Caesar-Cipher-Tool.git
cd Caesar-Cipher-Tool
```

### Install Required Packages

Install the required Python packages using `pip`:

```bash
pip install customtkinter pyperclip
```

These packages are required for the GUI and clipboard functionalities.

## Usage

### Running the Application

After installing the necessary packages, you can run the application using the following command:

```bash
python caesar_cipher_tool.py
```

### Interface Overview

- **Text Entry**: Enter the text you wish to encrypt or decrypt.
- **Shift Values**: Enter one or more shift values (comma-separated) for the Caesar Cipher.
- **Encrypt/Decrypt Options**: Choose whether to encrypt or decrypt the input text.
- **Process Button**: Click to apply the Caesar Cipher transformation.
- **Copy to Clipboard**: Copy the resulting text to your clipboard for easy pasting.
- **Save to File**: Save the encrypted or decrypted text to a `.txt` file.
- **Load from File**: Load text from a `.txt` file for encryption or decryption.
- **Customize Font**: Open a window to choose a custom font for the text areas.
- **About**: Learn more about the application and its author.

### Example Usage

1. **Encrypting Text**:
   - Enter the text in the text entry field.
   - Specify the shift value (e.g., `3`).
   - Choose "Encrypt" and click "Process".
   - The result will be displayed in the output area.

2. **Decrypting Text**:
   - Enter the encrypted text in the text entry field.
   - Specify the shift value used for encryption.
   - Choose "Decrypt" and click "Process".
   - The decrypted text will be displayed.

3. **Customizing Font**:
   - Click "Customize Font" to open the font selection window.
   - Choose your preferred font from the dropdown menu.

4. **Saving/Loading Files**:
   - Use "Save to File" to save the result to a text file.
   - Use "Load from File" to load text from a file for encryption or decryption.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, feel free to open an issue or submit a pull request. Please make sure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
