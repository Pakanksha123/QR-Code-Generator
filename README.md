#  QR Code Generator using Python (qrcode + PIL)

A Python-based application that generates QR codes from user input (text or URLs) and saves them as image files using the `qrcode` library with PIL support.

---

##  Overview

This project demonstrates how to generate and customize QR code images using Python. It takes user input and converts it into a QR code image that can be scanned using any QR scanner.

Built using:

* Python
* qrcode
* Pillow

---

##  Features

* Generate QR codes for text or URLs
* Save QR codes as image files (.png)
* Uses PIL for image handling
* Simple and beginner-friendly
* Fast and lightweight

---

## 🛠️ Requirements

* Python 3.x
* qrcode
* Pillow

---

##  Installation

Install required libraries:

```bash id="g7d2hs"
pip install qrcode[pil]
```

---

##  How to Run

```bash id="l3p9xa"
python qr_generator.py
```

---

##  How It Works

1. User enters text or URL
2. The `qrcode` library encodes the data
3. PIL processes the image internally
4. The QR code is generated and saved as a `.png` file

---

## Project Structure

```id="m9c2kd"
qr-code-generator/
│
├── qr_generator.py   # Main script
├── output.png        # Generated QR code image
├── README.md         # Documentation
```

---

##  Sample Code

```python id="y8k2vd"
import qrcode

# Get input
data = input("Enter text or URL: ")

# Create QR object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

# Generate image using PIL
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("output.png")

print("QR Code generated successfully!")
```

---

##  Notes

* Pillow (PIL) is required for image processing
* Ensure dependencies are installed before running
* Works offline after installation

---

##  Future Enhancements

* Add GUI using Tkinter
* Customize colors and styles
* Add logo inside QR code
* Batch QR code generation

---



**Project:** QR Code Generator using Python
**Description:**
Developed a Python application to generate QR codes from user input using the qrcode library with Pillow for image processing, demonstrating data encoding and image generation.

---

## 👩‍💻 Author

Akanksha

---

## 📜 License

This project is open-source and free to use.
# QR-Code-Generator
