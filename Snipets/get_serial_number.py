import subprocess

process = subprocess.run(['wmic', 'bios', 'get', 'serialnumber', '/value'], capture_output=True, text=True, check=True)
output = process.stdout
SN = output.split("=")[1].strip() if "=" in output else output.strip()
print(SN)
