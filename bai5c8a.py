print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import tkinter as tk

def create_personal_info_form():
    """Xây dựng form hiển thị thông tin cá nhân."""
    root_a = tk.Tk()
    root_a.title("Thông tin Cá nhân")

    # Dữ liệu cá nhân mẫu (Bạn cần thay đổi thông tin này)
    ho_ten = "Nguyễn Văn B"
    ngay_sinh = "15/05/2002"
    mssv = "20205678"
    nganh_hoc = "Khoa học Máy tính"

    # Tiêu đề
    tk.Label(root_a, text="THÔNG TIN CÁ NHÂN", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    # Sử dụng Grid Manager để sắp xếp thông tin
    labels = ["Họ tên:", "Ngày sinh:", "MSSV:", "Ngành học:"]
    data = [ho_ten, ngay_sinh, mssv, nganh_hoc]

    for i, (lbl_text, data_text) in enumerate(zip(labels, data)):
        # Cột 0: Tên trường thông tin
        tk.Label(root_a, text=lbl_text, anchor='w').grid(row=i+1, column=0, padx=10, pady=5, sticky='w')
        # Cột 1: Dữ liệu (in đậm)
        tk.Label(root_a, text=data_text, font=("Arial", 10, "bold"), anchor='w').grid(row=i+1, column=1, padx=10, pady=5, sticky='w')

    root_a.mainloop()

# Để chạy form này, gọi hàm: create_personal_info_form()
