from import_all import*
from Main import*

class UI_of_main_gui(MainWindow):
    def change_window(self):
        self.ui.but_tool_cam1.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_calib.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_4cam.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_take.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_ng1cam.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_ng4cam.clicked.connect(self.toggle_visibility)
        self.ui.but_tool_output.clicked.connect(self.toggle_visibility)