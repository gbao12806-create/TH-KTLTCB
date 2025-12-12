print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

class RomanToInteger:
    def __init__(self, roman):
        self.roman = roman.upper()  
    def to_int(self):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        total = 0
        prev_value = 0
        for char in reversed(self.roman):
            value = roman_values[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total
roman_number = RomanToInteger("MCMXCIV")
print("Số La Mã:", roman_number.roman)
print("Giá trị số nguyên:", roman_number.to_int())

