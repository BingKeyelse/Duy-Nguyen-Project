from import_all import*

class ListWidget():
    def __init__(self, parent: "MainWindow"):
        self.parent = parent

        filenames = self.parent .get_recent_filenames(self.parent.database[0])

        # Xóa danh sách cũ trước khi thêm mới
        self.parent.ui.list_ng1cam.clear() 
        if filenames:
            self.parent.ui.list_ng1cam.addItems(filenames)  # Thêm dữ liệu vào QListWidget
            print(f"✅ Đã tải {len(filenames)} file vào ListWidget")
        else:
            print("⚠️ Không có file nào trong database!")
