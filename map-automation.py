import vgamepad as vg
import pyautogui
import pytesseract
import time
import random
from PIL import ImageGrab

# Configure Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Define preferred map
PREFERRED_MAP = "Stakeout"

# Define the region for detecting the final map (adjust these coordinates based on your screen resolution)
FINAL_MAP_REGION = (50, 900, 500, 1020)  # Adjusted for 1920x1080

# Initialise global variables
use_controller = False
gamepad = None  # Placeholder for gamepad object if using a controller


# Helper functions
def random_sleep(min_time=0.5, max_time=1.5):
    """
    Adds a random delay to mimic human behaviour.
    """
    time.sleep(random.uniform(min_time, max_time))


def capture_text(region):
    """
    Captures text from a specific region using OCR.
    """
    screenshot = ImageGrab.grab(bbox=region)  # Capture the region
    detected_text = pytesseract.image_to_string(screenshot).strip()  # Extract text
    return detected_text


def get_final_map_name():
    """
    Extracts the final map name from the specific screen region.
    """
    return capture_text(FINAL_MAP_REGION)


# PC Keyboard Input Functions
def back_out_pc():
    """
    Performs the key sequence to back out of the lobby using PC keyboard input.
    """
    print("Backing out (PC)...")
    pyautogui.press('esc')  # Open menu
    random_sleep()
    pyautogui.press('up')  # Navigate up in the menu
    random_sleep()
    pyautogui.press('space')  # Confirm leaving
    random_sleep(1, 2)  # Wait for animation


def requeue_pc():
    """
    Performs the key sequence to requeue using PC keyboard input.
    """
    print("Requeuing (PC)...")
    pyautogui.press('space')  # Start matchmaking
    random_sleep()
    pyautogui.press('space')  # Confirm matchmaking
    random_sleep(2, 3)  # Wait for matchmaking to start


# Controller Input Functions
def initialise_gamepad():
    """
    Initialises the virtual gamepad for controller input.
    """
    global gamepad
    gamepad = vg.VX360Gamepad()


def press_button(button, duration=0.2):
    """
    Simulates pressing a button on the controller.
    """
    gamepad.press_button(button=button)
    gamepad.update()
    time.sleep(duration)
    gamepad.release_button(button=button)
    gamepad.update()


def back_out_controller():
    """
    Performs the key sequence to back out of the lobby using controller buttons:
    Circle -> Up D-Pad -> X
    """
    print("Backing out (Controller)...")
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)  # Circle (Back)
    random_sleep()
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)  # D-Pad Up
    random_sleep()
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # X (Confirm)
    random_sleep(1, 2)  # Wait for animation


def requeue_controller():
    """
    Performs the key sequence to requeue using controller buttons:
    X -> X
    """
    print("Requeuing (Controller)...")
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # X (Confirm search)
    random_sleep()
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # X (Start matchmaking)
    random_sleep(2, 3)  # Wait for matchmaking


# Main Loop
def main_loop():
    """
    Main loop that checks for the final map name and decides to back out or stay.
    """
    while True:
        print("Waiting for final map selection...")
        final_map_name = get_final_map_name()
        print(f"Detected final map: {final_map_name}")

        if final_map_name.lower() != PREFERRED_MAP.lower():
            print("Not the preferred map. Backing out...")
            if use_controller:
                back_out_controller()
                requeue_controller()
            else:
                back_out_pc()
                requeue_pc()
        else:
            print("Preferred map found! No further action needed.")
            break
        time.sleep(1)


# User Input Selection
def select_input_method():
    """
    Prompts the user to select their input method (Controller or PC).
    """
    global use_controller
    print("Select your input method:")
    print("1: Controller")
    print("2: PC (Keyboard/Mouse)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        use_controller = True
        initialise_gamepad()
        print("Controller input selected.")
    elif choice == "2":
        use_controller = False
        print("PC input selected.")
    else:
        print("Invalid choice. Defaulting to PC input.")
        use_controller = False


# Entry Point
if __name__ == "__main__":
    select_input_method()
    print("Starting map automation...")
    main_loop()
