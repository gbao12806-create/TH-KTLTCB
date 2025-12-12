print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import turtle

# Thiết lập cửa sổ
window = turtle.Screen()
window.bgcolor("white")

# Thiết lập rùa vẽ
painter = turtle.Turtle()
painter.speed(0) # Đặt tốc độ tối đa để vẽ nhanh hơn
painter.pensize(2)

# Định nghĩa danh sách màu
colors = ["red", "green", "blue"] 

# Bắt đầu vòng lặp vẽ
for i in range(18): 
    # Chọn màu luân phiên: colors[0] -> colors[1] -> colors[2] -> colors[0] ...
    # i % 3 sẽ cho ra các chỉ số 0, 1, 2, 0, 1, 2, ...
    color_index = i % len(colors)
    painter.pencolor(colors[color_index])

    # Vẽ hình tròn
    painter.circle(100)
    
    # Xoay rùa 20 độ để hình tròn tiếp theo được đặt ở vị trí mới
    painter.left(20) 

# Ẩn rùa sau khi vẽ xong
painter.hideturtle()

# Giữ cửa sổ mở
window.mainloop()
