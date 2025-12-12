print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import tkinter as tk

root = tk.Tk()
root.title("tk") # Đặt tiêu đề là 'tk' theo hình ảnh gốc

# 1. Khởi tạo biến điều khiển
v = tk.IntVar()
v.set(1)

# 2. Định nghĩa danh sách các lựa chọn (Đã sửa lại danh sách để khớp với nội dung hiển thị)
# Đây là danh sách chính xác từ gợi ý (Python 1, Perl 2, ...)
languages_data = [
    ("Python 1", 1),
    ("Perl 2", 2),
    ("Java 3", 3),
    ("C++ 4", 4),
    ("C 5", 5)
]

# 3. Định nghĩa hàm xử lý sự kiện
def ShowChoice():
    # In giá trị (value) của Radio Button đã chọn ra console
    print("Giá trị đã chọn (Indicator):", v.get())

# 4. Thêm Label
tk.Label(root,
         text="Choose your favourite\nprogramming language:",
         justify=tk.LEFT,
         padx=20).pack(anchor=tk.W)

# 5. Vòng lặp tạo Radio Button dưới dạng Indicator
for language, val in languages_data:
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val,
                   # ********** THUỘC TÍNH MỚI **********
                   indicatoron=0, # Tắt hình tròn chỉ báo
                   width=20       # Đặt chiều rộng cố định
                   # ***********************************
                   )
    .pack(anchor=tk.W)

root.mainloop()
