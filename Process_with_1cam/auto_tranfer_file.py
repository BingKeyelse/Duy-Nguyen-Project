# from import_all import*
import subprocess

# Định nghĩa file giao diện và file output
file_ui = "main_gui.ui"
file_ui_to_py = "main_gui.py"

file_qrc = "icons.qrc"
file_qrc_to_py = "icons_rc.py"

# Chạy lệnh pyuic5 để cập nhật giao diện
def convert_ui_qrc_to_py():
    subprocess.run(f"pyuic5 {file_ui} -o {file_ui_to_py}", shell=True)
    subprocess.run(f"pyrcc5 {file_qrc} -o {file_qrc_to_py}", shell=True)
    print("UI updated successfully.")

convert_ui_qrc_to_py()