import os
import shutil
from datetime import datetime

def auto_check_and_create_folder_and_file_NG(self):
    link = os.path.join(self.current_file_path, "data_NG")

    self.year_backup = []
    self.month_backup = []
    self.path_ng_save_today = None

    today = datetime.today()
    self.month_now = today.month
    self.year_now = today.year

    # Tạo thư mục hiện tại nếu chưa có
    self.path_folder_year_now = os.path.join(link, str(self.year_now))
    self.path_folder_today_ng_now = os.path.join(self.path_folder_year_now, str(self.month_now))

    if not os.path.exists(self.path_folder_today_ng_now):
        os.makedirs(self.path_folder_today_ng_now)

    # Kiểm tra xem thư mục data_NG có dữ liệu không
    if not os.path.exists(link) or not os.listdir(link):
        print("⚠ Thư mục 'data_NG' trống, không có dữ liệu để kiểm tra.")
        return

    # Thu thập danh sách năm
    self.year_backup = sorted(os.listdir(link))
    
    if len(self.year_backup) == 0:
        print("⚠ Không có năm nào trong thư mục 'data_NG'.")
        return

    check_year_now = os.path.join(link, self.year_backup[-1])  # Lấy năm mới nhất

    # Thu thập danh sách tháng
    self.month_backup = sorted(os.listdir(check_year_now))

    if len(self.month_backup) == 0:
        print("⚠ Không có tháng nào trong thư mục năm gần nhất.")
        return

    # Kiểm tra nếu đã có ít nhất 6 tháng
    if int(self.month_backup[-1]) >= 6:
        if len(self.month_backup) > 6:
            for month in self.month_backup[:-6]:
                path_month_clear = os.path.join(check_year_now, month)

                if os.path.exists(path_month_clear):
                    print(f"🗑 Xóa thư mục tháng cũ: {path_month_clear}")
                    try:
                        shutil.rmtree(path_month_clear)
                    except Exception as e:
                        print(f"⚠ Lỗi khi xóa {path_month_clear}: {e}")

        # Xóa các năm cũ hơn năm gần nhất
        for year in self.year_backup[:-1]:
            path_year_to_clear = os.path.join(link, year)

            if os.path.exists(path_year_to_clear):
                print(f"🗑 Xóa thư mục năm cũ: {path_year_to_clear}")
                try:
                    shutil.rmtree(path_year_to_clear)
                except Exception as e:
                    print(f"⚠ Lỗi khi xóa {path_year_to_clear}: {e}")

    # Nếu chưa đủ 6 tháng, lấy thêm tháng từ năm trước
    else:
        month_cap = 6 - int(self.month_backup[-1])

        if len(self.year_backup) >= 2:
            path_year_old = os.path.join(link, self.year_backup[-2])

            for month in os.listdir(path_year_old):
                if int(month) <= (12 - month_cap):
                    path_month_old_clear = os.path.join(path_year_old, month)

                    if os.path.exists(path_month_old_clear):
                        print(f"🗑 Xóa tháng cũ từ năm trước: {path_month_old_clear}")
                        try:
                            shutil.rmtree(path_month_old_clear)
                        except Exception as e:
                            print(f"⚠ Lỗi khi xóa {path_month_old_clear}: {e}")
