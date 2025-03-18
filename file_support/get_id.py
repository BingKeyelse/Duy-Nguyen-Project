import subprocess

def get_hdd_serial():
    """Lấy số serial ổ cứng bằng PowerShell"""
    try:
        output = subprocess.check_output(
            ["powershell", "-Command", "(Get-PhysicalDisk)[0].SerialNumber"], 
            shell=True
        ).decode().strip()
        return output
    except Exception as e:
        print(f"Lỗi khi lấy serial ổ cứng: {e}")
        return None

serial = get_hdd_serial()
if not serial:
    print("Không lấy được serial, thoát chương trình!")
    exit()

print(f"Serial của ổ cứng: {serial}")
