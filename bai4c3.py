print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

class Nguoi(object):
    def getGender(self):
        return "Unknown"
class Nam(Nguoi):
    def getGender(self):
       return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())

