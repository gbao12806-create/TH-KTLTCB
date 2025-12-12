print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def dientich(self):
        return self.chieu_dai * self.chieu_rong
hcn = Hinhchunhat(5, 3)
print("Diện tích hình chữ nhật là:", hcn.dientich())

