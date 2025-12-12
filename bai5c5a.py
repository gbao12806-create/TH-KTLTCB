print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")

# 1. Khởi tạo biến điều khiển (Control Variable)
v = tk.IntVar()
v.set(1) # Khởi tạo lựa chọn ban đầu là Python (value=1)

# 2. Định nghĩa danh sách các lựa chọn
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# 3. Định nghĩa hàm xử lý sự kiện
def ShowChoice():
    # In giá trị (value) của Radio Button đã chọn ra console
    print("Giá trị đã chọn:", v.get())

# 4. Thêm Label
tk.Label(root,
         text="""Chọn ngôn ngữ lập trình yêu thích của bạn:""",
         justify=tk.LEFT,
         padx=20).pack(anchor=tk.W) # anchor=tk.W căn lề trái

# 5. Vòng lặp tạo Radio Button
# language là tên hiển thị, val là giá trị (1, 2, 3,...)
for language, val in languages:
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,          # Liên kết với biến v
                   command=ShowChoice,  # Gọi hàm ShowChoice khi được chọn
                   value=val)           # Giá trị được gán cho v khi chọn
    .pack(anchor=tk.W) # anchor=tk.W căn lề trái

root.mainloop()
