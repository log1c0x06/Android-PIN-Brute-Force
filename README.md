
# Android PIN Brute Force

This script attempts to brute-force the PIN of an Android device connected via ADB (Android Debug Bridge). It supports both brute-forcing numeric PINs of specific lengths and using a wordlist to try specific PINs.

## Features

- Brute force 4-digit or 6-digit PINs.
- Use a custom wordlist for PIN attempts.
- Delays to mimic device lockout behavior after multiple incorrect attempts.
- Checks for ADB device authorization.

## Requirements

- Python 3.x
- ADB (Android Debug Bridge) installed and properly configured.
- USB debugging enabled on the target Android device.
- The target device should be connected via USB.

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install ADB:
    ```sh
    sudo apt-get install adb
    ```
3. Clone this repository:
    ```sh
    git clone https://github.com/log1c0x06/android-pin-brute-force.git
    ```
4. Navigate to the project directory:
    ```sh
    cd android-pin-brute-force
    ```
5. Install required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure your Android device is connected and authorized for ADB.
2. Run the script:
    ```sh
    python3 PIN_Brute_Force.py
    ```
3. Follow the on-screen menu to choose your desired option:
    - Brute force a 4-digit PIN.
    - Brute force a 6-digit PIN.
    - Use a wordlist to try specific PINs.
    - Exit the script.

## Sample Output

```
Android PIN Brute Force

          1. Brute Force 4-Digit PIN
          2. Brute Force 6-Digit PIN
          3. Use Wordlist
          4. Exit

Enter your choice: 1

Trying PIN: 0000
Trying PIN: 0001
Trying PIN: 0002
...
PIN found: 1234

Created by LOG1C0x06
```

## Troubleshooting

If you encounter issues with ADB device authorization, make sure:
- USB debugging is enabled on the Android device.
- The device is properly connected via USB.
- You authorize the device when prompted.

To reset ADB and reauthorize the device, you can use:
```sh
adb kill-server
adb start-server
adb devices
```

## License

This project is licensed under the MIT License.
