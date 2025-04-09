# 📷Image Stego Secure 

A Python based **Image Steganography** tool that allows you to securely hide secret messages within the images. The tool uses basic image processing techniques to embed and extract messages, protected by a custom passcode.

## 🛠️Requirements

Make sure you have Python installed. Install the required libraries using:

```
pip install opencv-python
```

## 💻Usage

### 1. Clone the Repository

```
git clone https://github.com/Apoorva-Satakolla/image-stego-secure.git
cd image-stego-secure
```

### 2. Run the Script

```
python image-stego-secure.py
```

### 3. How it Works

- Input the path of the image you want to use.
- Enter the secret message you want to hide.
- Set a passcode for encrypting the message.
- The tool will generate an encrypted image and open it automatically.
- For decryption, input the correct passcode to reveal the hidden message.

## 📝License

Distributed under the MIT License.
