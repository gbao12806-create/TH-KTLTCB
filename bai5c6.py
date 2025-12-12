print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

from tkinter import *
from tkinter import messagebox # Cần thư viện này để hiển thị hộp thoại thông báo

# ----------------------------------------------------
# BƯỚC 3: Thêm các phương thức xử lý sự kiện
# ----------------------------------------------------

def NewFile():
    """Hiển thị thông báo khi chọn New."""
    print("New File!")
    messagebox.showinfo("Thông báo", "Tạo tệp mới!") # Thêm hộp thoại thông báo

def OpenFile():
    """Hiển thị thông báo khi chọn Open."""
    print("Open File!")
    messagebox.showinfo("Thông báo", "Mở tệp hiện có!")

def Exit():
    """Thoát chương trình."""
    root.quit() # root.quit() là cách chuẩn để thoát chương trình Tkinter

def InsText():
    """Hiển thị thông báo khi chọn Text."""
    print("Insert Text!")
    messagebox.showinfo("Thông báo", "Chèn văn bản!")

def InsPic():
    """Hiển thị thông báo khi chọn Picture."""
    print("Insert Picture!")
    messagebox.showinfo("Thông báo", "Chèn hình ảnh!")

def About():
    """Hiển thị thông báo về ứng dụng."""
    print("This is a simple example of a menu")
    messagebox.showinfo("Về ứng dụng", "Đây là một ứng dụng menu mẫu đơn giản.")

# ----------------------------------------------------
# BƯỚC 1 & 2: Thực hiện tạo window form và Menu Bar
# ----------------------------------------------------

root = Tk()
root.title("tk") # Đặt tiêu đề là 'tk' theo hình ảnh mẫu
root.geometry("300x200") # Thiết lập kích thước cửa sổ

# Tạo đối tượng Menu chính
menu = Menu(root)

# Thiết lập Menu chính cho cửa sổ
root.config(menu=menu)

# ------------------
# 1. Menu FILE
# ------------------
filemenu = Menu(menu, tearoff=0) # tearoff=0 loại bỏ đường gạch ngang ở đầu menu
menu.add_cascade(label="File", menu=filemenu)

# Thêm các lệnh con cho Menu File
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator() # Đường kẻ phân cách
filemenu.add_command(label="Exit", command=Exit)

# ------------------
# 2. Menu INSERT
# ------------------
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)

# Thêm các lệnh con cho Menu Insert
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# ------------------
# 3. Menu HELP
# ------------------
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)

# Thêm lệnh con cho Menu Help
helpmenu.add_command(label="About...", command=About)

# Khởi chạy vòng lặp sự kiện chính
root.mainloop()
