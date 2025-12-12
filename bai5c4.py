print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200') # Thiết lập kích thước cửa sổ
# Tạo Label (để hiển thị thông báo)
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# Tạo Button (để người dùng tương tác)
# Button này sẽ được tạo ở bước c và d
def clicked():
    # Khi nút được nhấn, văn bản của Label sẽ thay đổi
    lbl.configure(text="Button was clicked !!")
    
# Thêm Button vào cửa sổ và liên kết nó với hàm clicked()
# Gợi ý trong đề bài sử dụng các thuộc tính cơ bản
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
from tkinter import *

# 1. Khởi tạo cửa sổ đồ họa
window = Tk()
window.title("Welcome to Tkinter App") # Đặt tiêu đề cửa sổ
window.geometry('350x200') # Đặt kích thước cửa sổ

# 2. Xây dựng phương thức xử lý sự kiện
def clicked():
    # Thay đổi văn bản của Label khi nút được nhấn
    lbl.configure(text="Nút đã được bấm!")
    # Thay đổi màu nền của Label để tạo hiệu ứng
    lbl.configure(bg="yellow")

# 3. Thêm widget Label
# Column 0, Row 0
lbl = Label(window, text="Chào mừng đến với Tkinter!", font=("Arial Bold", 10))
lbl.grid(column=0, row=0, padx=10, pady=10) # Thêm padding cho đẹp hơn

# 4. Thêm widget Button với thuộc tính màu sắc (bg và fg)
# bg: background color (Màu nền)
# fg: foreground color (Màu chữ)
# Column 1, Row 0
btn = Button(window, 
             text="Bấm vào đây!", 
             command=clicked, 
             bg="blue", 
             fg="white", 
             font=("Arial", 10))
btn.grid(column=1, row=0, padx=10, pady=10) # Thêm padding

# Khởi chạy vòng lặp sự kiện chính của Tkinter
window.mainloop()
