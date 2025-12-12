print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import tkinter as tk
from tkinter import messagebox

def create_radio_button_form():
    """Xây dựng form có Radio Button và Button Click Me."""
    root_b = tk.Tk()
    root_b.title("Welcome") # Tiêu đề theo hình mẫu

    # 1. Biến điều khiển cho Radio Buttons
    # Giá trị của Radio Button sẽ được lưu ở đây (1, 2, hoặc 3)
    v = tk.IntVar()
    v.set(1) # Giá trị mặc định là First (1)

    # 2. Hàm xử lý sự kiện khi nút "Click Me" được nhấn
    def click_me_button():
        selected_value = v.get()
        # Hiển thị giá trị đang chọn trong hộp thoại thông báo
        messagebox.showinfo("Lựa chọn Radio Button", 
                            f"Giá trị đang chọn: {selected_value}")

    # 3. Thêm các Widget

    # Nhãn 'Welcome' (giả định đây là nhãn chính)
    tk.Label(root_b, text="Welcome", font=("Arial", 12)).pack(pady=5)
    
    # Khung chứa (Frame) để giữ các phần tử trên cùng một hàng
    frame = tk.Frame(root_b)
    frame.pack(pady=10)

    # Radio Buttons (Liên kết tất cả với biến v)
    tk.Radiobutton(frame, text="First", variable=v, value=1).pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(frame, text="Second", variable=v, value=2).pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(frame, text="Third", variable=v, value=3).pack(side=tk.LEFT, padx=5)

    # Button "Click Me"
    tk.Button(frame, text="Click Me", command=click_me_button).pack(side=tk.LEFT, padx=10)

    root_b.mainloop()

# Để chạy form này, gọi hàm: create_radio_button_form()
