# MACdonald-s
**A MAC Address Changer Tool 🖧**

This tool allows you to change the MAC address of your network adapter on Windows systems easily.

## Prerequisites

- Administrator rights on your machine.
- Python 3.x installed with required libraries.
- Familiarity with basic Windows tools like Command Prompt and Registry Editor.

## Configuration Parameters

Before running the script, update the following variables in the code or as environment inputs:

### `path_to_project`
Specify the absolute path to the folder containing this project on your system.

---

### `transport_name`
The transport name identifies your network adapter in the system. To find it:
1. Open **Command Prompt**.
2. Type: `getmac`.
3. Locate the full transport name in the output and copy it. Paste this value into the script where required.

---

### `registry_key_path`
This defines the registry path for the network adapter.
1. Open **Registry Editor**:
   - Press `Win + R`, type `regedit`, and press Enter.
2. Navigate to: `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`.
3. Right-click on the `Class` folder, and search for your network adapter using the transport name from the previous step.
4. Verify that the `NetworkAddress` entry (REG_SZ) exists and contains your current MAC address.
5. Copy the full registry path of the relevant adapter and paste it here.

---

### `default_wifi_ssid`
Enter the name (SSID) of your current Wi-Fi network. Alternatively, leave it blank to skip this step.

---

### `adapter`
Identify the name of your active network adapter:
1. Open **Control Panel**.
2. Navigate to: `Network and Internet > Network Connections`.
3. Locate your adapter used for Wi-Fi or Ethernet (e.g., `Wi-Fi`).
4. Copy its name and provide it as input.

---

## How It Works

1. The tool retrieves the current MAC address and generates a new random MAC address.
2. It disables your network adapter to prepare for MAC address changes.
3. The Windows Registry is updated with the new MAC address.
4. The tool re-enables the adapter and reconnects to the Wi-Fi network (if specified).

## Logs

Two log files are maintained in the project directory:
- **addresses.txt**: Records MAC address changes with timestamps.
- **elog.txt**: Tracks errors encountered during execution.

## Known Issues

- Ensure you have administrative privileges. Without them, the script will fail to modify registry keys or manage network adapters. You can run registryeditor.bat which will run the script as admin.
- The script is tested only on Windows systems and requires dependencies like `winreg` and `subprocess`.

## Disclaimer

This tool is for educational purposes only. Unauthorized MAC address spoofing may violate the terms of service of your network provider.
