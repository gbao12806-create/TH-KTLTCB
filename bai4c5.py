print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

class DaoNguocChuoi:
    def __init__(self, chuoi):
        self.chuoi = chuoi

    def dao_nguoc_tu(self):
        tu = self.chuoi.split()
        tu.reverse()
        return ' '.join(tu)
chuoi_vao = "hello .py"
obj = DaoNguocChuoi(chuoi_vao)
print("Chuỗi ban đầu:", chuoi_vao)
print("Chuỗi sau khi đảo:", obj.dao_nguoc_tu())

