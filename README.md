# Call of Duty: Black Ops 6 Map Automation Script

This project provides a Python-based automation script to back out of lobbies and requeue until a specific map, such as "Stakeout", is selected during the **final map selection screen** in *Call of Duty: Black Ops 6*. The script supports **PC (keyboard/mouse)** and **controller** inputs, making it versatile for different setups.

---

## Features

- **Automatic Map Detection**: Uses Optical Character Recognition (OCR) to detect the final map name.
- **Multi-Input Support**: Allows both PC (keyboard/mouse) and controller (PS4/Xbox) inputs.
- **Smart Automation**:
  - Automatically backs out if the map is not your preferred one.
  - Requeues until your desired map is selected.
- **Human-Like Behaviour**: Introduces randomised delays for realistic input simulation.
- **Customisable Preferences**: Easily adjust the target map name, screen region, and delays.

---

## Requirements

### Python
- **Version**: Python 3.8 or higher

### Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt

## Tesseract OCR

### Download and Install Tesseract OCR:
1. Install Tesseract OCR from the [official repository](https://github.com/tesseract-ocr/tesseract).
2. During installation, ensure the **Language Data** component is selected.

### Update the Tesseract Path:
Update the path in the script to match your Tesseract installation:

```python
pytesseract.pytesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
