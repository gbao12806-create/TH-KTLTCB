print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

class XuLyChuoi:
    def __init__(self):
        self.chuoi = ""
    def get_String(self):
        self.chuoi = input("Nhập vào một chuỗi: ")
    def print_String(self):
        print("Chuỗi in hoa là:", self.chuoi.upper())
obj = XuLyChuoi()
obj.get_String()
obj.print_String()

