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

### Tesseract OCR
1. **Download and Install Tesseract OCR:
  - Install Tesseract OCR from the official repository.
  - During installation, ensure the Language Data component is selected.

2. **Update the Tesseract Path:
  - In the script, update the path to match your Tesseract installation:
  - pytesseract.pytesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

### ViGEmBus Driver (For Controller Input)
- **Install the ViGEmBus driver from ViGEmBus Releases.
- **This driver is required to emulate controller inputs.

### Usage
1. Clone or Download the Repository

Clone the repository using:

git clone <repository-url>

Alternatively, download the files directly from GitHub.
2. Install Dependencies

Navigate to the repository folder and install the required dependencies:

pip install -r requirements.txt

3. Run the Script

Run the script using Python:

python map_automation.py

4. Select Input Method

When prompted, select your preferred input method:

    1: Controller
    2: PC (Keyboard/Mouse)

5. Script Behaviour

    The script monitors the final map selection screen and compares the selected map to the target map (e.g., "Stakeout").
    If the map is not "Stakeout", the script:
        Backs out of the lobby.
        Requeues for matchmaking.
    The script repeats this process until the target map is selected.

Customisation
Adjust Target Map

Change the desired map by updating the PREFERRED_MAP variable in the script:

PREFERRED_MAP = "Stakeout"

Adjust Screen Region

Modify the region where the map name is detected. Update the FINAL_MAP_REGION variable:

FINAL_MAP_REGION = (50, 900, 500, 1020)  # Coordinates for your screen

Adjust Delays

Customise delays to simulate human-like behaviour by modifying the random_sleep function:

def random_sleep(min_time=0.5, max_time=1.5):
    time.sleep(random.uniform(min_time, max_time))

Example Workflow
PC Input

    Back Out: Esc -> Up -> Space
    Requeue: Space -> Space

Controller Input

    Back Out: Circle -> Up D-Pad -> X
    Requeue: X -> X

Contributing

Contributions are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request.
Licence

This project is licensed under the MIT Licence. See the LICENSE file for details.
Acknowledgements

    Tesseract OCR: For text recognition.
    ViGEmBus: For enabling virtual controller inputs.
    Python Libraries:
        pyautogui
        pytesseract
        pillow
        vgamepad
