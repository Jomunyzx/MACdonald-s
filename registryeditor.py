import winreg, random, subprocess, time, os, re, uuid, json
from datetime import datetime

path_to_project = ""
registry_key_path = r""
default_wifi_ssid = ""
transport_name = "{}"
adapter = ""

# WIFI
def get_wifi_ssid():
    results = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("utf-8")
    ssid = re.search(r"SSID\s+: (.*)", results)
    if ssid:
        return ssid.group(1).strip()
    else:
        return None
wifi_ssid = get_wifi_ssid()

if wifi_ssid == None:
    try:
        os.system(f'netsh wlan connect name={default_wifi_ssid}')
    except:
        with open(rf'{path_to_project}\addresses.txt', "a") as file:
            file.write(f'Wifi not connected | {datetime.now()}')
# WIFI

# MAC ADDRESS
def generate_random_mac():
    first_byte = random.randint(0x00, 0xff) & 0xfe | 0x02
    remaining_bytes = [random.randint(0x00, 0xff) for _ in range(5)]
    mac_address = [first_byte] + remaining_bytes
    mac_address_str = ''.join(f'{byte:02x}' for byte in mac_address)

    return mac_address_str

random_mac = generate_random_mac()
# MAC ADDRESS

# CURRENT MAC ADDRESS
def get_mac_address(adapter_name):
    result = subprocess.run(['getmac'], capture_output=True, text=True)
    if result.returncode != 0:
        return None
    for line in result.stdout.splitlines():
        if adapter_name in line:
            return line.split()[0]
    return None
current_mac = get_mac_address(transport_name)
# CURRENT MAC ADDRESS

# NETWORK ADAPTERS
def disable_network_adapters():
    command = f'netsh interface set interface "{adapter}" disable'
    subprocess.run(['powershell', '-Command', command], shell=True)

def enable_network_adapters():
    command = f'netsh interface set interface "{adapter}" enable'
    subprocess.run(['powershell', '-Command', command], shell=True)
# NETWORK ADAPTERS

# REGISTRY
def change_registry_value(key_path, value_name, new_value):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_value)
        winreg.CloseKey(key)
    except WindowsError as e:
        with open(rf'{path_to_project}\addresses.txt', "a") as file:
            file.write(f'ERROR: {e} | {random_mac} -> {current_mac} | {datetime.now()}' + '\n')

key_path = registry_key_path
value_name = "NetworkAddress"
new_value = random_mac
# REGISTRY

# START
with open(rf'{path_to_project}\addresses.txt', "a") as file:
    file.write(f'{current_mac.replace("-", ":")} -> {(':'.join(random_mac[i:i+2] for i in range(0, 12, 2))).upper()} | {datetime.now()} | {wifi_ssid}' + '\n')
time.sleep(1)
disable_network_adapters()
time.sleep(3)
change_registry_value(key_path, value_name, new_value)
time.sleep(3)
enable_network_adapters()
time.sleep(3)
if wifi_ssid != None:
    os.system(f'netsh wlan connect name={wifi_ssid}')
# START