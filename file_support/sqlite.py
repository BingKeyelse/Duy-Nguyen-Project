import sqlite3
import os
from datetime import datetime

DB_FILE = "image_database.db"

# Kết nối đến SQLite (tạo nếu chưa có)
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Tạo bảng nếu chưa tồn tại
cursor.execute('''
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT UNIQUE,
        filepath TEXT,
        saved_at TEXT
    )
''')
conn.commit()

def save_image_to_db(filename, folder_path):
    """Lưu ảnh vào database nếu chưa tồn tại."""
    filepath = os.path.join(folder_path, filename)
    saved_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute("INSERT INTO images (filename, filepath, saved_at) VALUES (?, ?, ?)", 
                       (filename, filepath, saved_at))
        conn.commit()
        print(f"✅ Đã lưu: {filename}")
    except sqlite3.IntegrityError:
        print(f"⚠️ Đã tồn tại: {filename}")

def get_recent_images(limit=100):
    """Lấy danh sách 100 ảnh gần nhất."""
    cursor.execute("SELECT filename, filepath, saved_at FROM images ORDER BY saved_at DESC LIMIT ?", (limit,))
    return cursor.fetchall()

if __name__ == "__main__":
    # Ví dụ lưu ảnh vào database
    folder = "path/to/images"
    new_file = "example.png"
    
    save_image_to_db(new_file, folder)

    # Lấy 100 ảnh gần nhất
    recent_images = get_recent_images()
    print("\n📌 Danh sách 100 ảnh gần nhất:")
    for img in recent_images:
        print(img)

    conn.close()
