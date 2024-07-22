# Caesar Cipher Tool

This project is a simple Caesar Cipher tool with a web-based graphical user interface (GUI) built using Python and Flask. It allows users to easily encrypt and decrypt text using the Caesar Cipher method.

## Features
- **User-Friendly Interface**: Intuitive layout for text input, shift value input, and buttons for encryption and decryption.
- **Dark Mode**: A sleek, dark-themed interface to reduce eye strain and improve user experience.
- **Real-Time Results**: Instantly view the encrypted or decrypted text as you input your values.
- **Mobile Friendly**: Accessible and functional on mobile devices.

## File Structure
```
caesar_cipher_tool/
├── caesar_cipher.py  # Contains the Caesar Cipher logic
├── main.py           # Contains the Flask web application
├── LICENSE           # License information
├── README.md         # Project details and usage instructions
├── .replit           # Replit configuration file
├── requirements.txt  # Dependencies for the project
├── static/           # Static files (CSS)
│   └── styles.css    # CSS for styling the web interface
└── templates/        # HTML templates
    └── index.html    # Main HTML template for the web interface
```

## How to Use
1. **Run the Application**: Click the "Run" button in Repl.it to start the Flask web application.
2. **Access the Web Interface**: Open the provided URL (typically `https://<your-repl-username>.<your-repl-project>.repl.co`) in your web browser.
3. **Enter Text**: Type the text you want to encrypt or decrypt.
4. **Enter Shift Value**: Specify the number of positions to shift.
5. **Encrypt/Decrypt**: Click the "Encrypt" or "Decrypt" button to see the results.

## Getting Started
### Prerequisites
- Ensure you have Python installed.
- Flask should be installed (`pip install flask`).

### Running Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/caesar_cipher_tool.git
   ```
2. Navigate to the project directory:
   ```sh
   cd caesar_cipher_tool
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python main.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.