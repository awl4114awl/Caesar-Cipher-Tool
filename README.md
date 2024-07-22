# Caesar Cipher Tool

This project is a simple Caesar Cipher tool with a web-based graphical user interface (GUI) built using Python and Flask. It allows users to easily encrypt and decrypt text using the Caesar Cipher method.

## Features
- **User-Friendly Interface**: Intuitive layout for text input, shift value input, and buttons for encryption and decryption.
- **Dark Mode**: A sleek, dark-themed interface to reduce eye strain and improve user experience.
- **Real-Time Results**: Instantly view the encrypted or decrypted text as you input your values.

## File Structure
```
caesar_cipher_tool/
├── caesar_cipher.py  # Contains the Caesar Cipher logic
├── main.py           # Contains the Flask web application
├── LICENSE           # License information
├── README.md         # Project details and usage instructions
├── .replit           # Replit configuration file
├── static/           # Static files (CSS)
│   └── styles.css    # CSS for styling the web interface
└── templates/        # HTML templates
    └── index.html    # Main HTML template for the web interface
```

## How to Use
1. **Run the Application**: Click the "Run" button in Replit to start the Flask web application.
2. **Access the Web Interface**: Open the provided URL (typically `http://127.0.0.1:5000`) in your web browser.
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
```

### Steps to Update and Push to GitHub

1. **Open your `README.md` file** in the Repl.it editor.
2. **Replace the content** with the updated version above.
3. **Open the Repl.it shell** and navigate to your project directory:
   ```sh
   cd path/to/caesar_cipher_tool
   ```
4. **Add and commit the updated `README.md` file**:
   ```sh
   git add README.md
   git commit -m "Update README with project details for Flask-based web app"
   ```
5. **Push the changes to GitHub**:
   ```sh
   git push origin main
   ```

### Example Commands
```sh
cd path/to/caesar_cipher_tool
git add README.md
git commit -m "Update README with project details for Flask-based web app"
git push origin main
```