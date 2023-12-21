# Color Image Steganography Using Columnar Transposition Cipher

## Project Overview
This Flask-based web application implements steganography in color images using the Columnar Transposition Cipher technique. It allows for the secure embedding of text or data into color images. The project blends classical cryptography with digital image processing to offer a unique approach to secure information hiding.

## Key Features
- **Secure Data Embedding:** Embed text or other data into color images using steganography, effectively hiding information within the image.
- **Columnar Transposition Cipher:** Employing this classical encryption method, the application rearranges the characters of the plaintext to form the ciphertext, which is then used for embedding into the image.
- **Versatile Media Handling:** Supports handling and processing of various media formats, including images, text, and videos.
- **User-Friendly Web Interface:** Provides an easy-to-use Flask web application for seamless data processing and retrieval.

## Technical Details
- **Flask Framework:** The application is built on Flask, enabling web-based interaction and processing.
- **Image Processing:** Utilizes Python libraries like OpenCV for image manipulation, ensuring that the embedded data does not significantly alter the appearance of the image.
- **Encryption Technique:** The Columnar Transposition Cipher is used to encrypt the data before embedding it into the image. This involves writing the data into a grid of fixed-size columns and then permuting the columns based on a key.
- **Data Embedding:** The encrypted data is embedded into the pixel values of the image, with careful manipulation to ensure minimal visual change.

## How to Run
1. Install Python and Flask, along with other dependencies listed in `requirements.txt`.
2. Clone the repository and navigate to the project directory.
3. Run `python app.py` to start the Flask server.
4. Access the application via a web browser using the provided local URL.

## Requirements
- Python
- Flask
- OpenCV and other Python libraries (see `requirements.txt` for a full list).

