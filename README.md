# Caesar Cipher Tool

This is a simple Caesar Cipher tool with a web-based user interface built using Flask. It allows users to easily encrypt and decrypt text using the Caesar Cipher method.

## Features
- **User-Friendly Web Interface**: Intuitive layout for text input, shift value input, and buttons for encryption and decryption.
- **Dark Mode**: A sleek, dark-themed interface to reduce eye strain and improve user experience.
- **Real-Time Results**: Instantly view the encrypted or decrypted text as you input your values.

## File Structure
```
caesar_cipher_web/
├── caesar_cipher.py  # Contains the Caesar Cipher logic
├── app.py            # Contains the Flask application
├── templates/
│   └── index.html    # HTML template for the web interface
├── static/
│   └── styles.css    # CSS styles for the web interface
└── README.md         # Project details and usage instructions
```

## How to Use
1. **Enter Text**: Type the text you want to encrypt or decrypt.
2. **Enter Shift Value**: Specify the number of positions to shift.
3. **Encrypt/Decrypt**: Click the "Encrypt" or "Decrypt" button to see the results.

This tool is perfect for learning about basic cryptography and exploring web development with Flask in Python.

## Getting Started
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/caesar_cipher_web.git
   ```
2. Navigate to the project directory:
   ```sh
   cd caesar_cipher_web
   ```
3. Install the dependencies:
   ```sh
   pip install Flask
   ```
4. Run the application:
   ```sh
   python app.py
   ```

5. Open your web browser and go to:
   ```sh
   http://127.0.0.1:5000
   ```

## License
This project is licensed under the MIT License.
```

### Explanation of Changes
- Updated the project description to reflect the new web-based implementation using Flask.
- Modified the file structure to match the new setup.
- Updated the "How to Use" section to describe the web interface.
- Changed the "Getting Started" instructions to include the installation of Flask and running the Flask application. 