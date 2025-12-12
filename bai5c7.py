print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import tkinter
import random

# Global variables (Biến toàn cục)
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# BƯỚC 2: Thay đổi thời gian chơi từ 30s thành 120s
timeleft = 120 

# Function that starts the game (Hàm bắt đầu trò chơi)
def startGame(event):
    """Bắt đầu đếm ngược và thiết lập màu đầu tiên."""
    # Chỉ bắt đầu đếm ngược khi trò chơi chưa chạy (lần bấm Enter đầu tiên)
    global timeleft
    if timeleft == 120: 
        countdown()
    # Sau lần bấm đầu tiên, xử lý câu trả lời và chuyển sang màu tiếp theo
    nextColour()

# Function to choose and display the next colour. (Hàm chọn và hiển thị màu tiếp theo)
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        # Làm ô nhập liệu luôn hoạt động
        e.focus_set()
        
        # Lấy giá trị nhập của người dùng. colours[1] là màu thực của chữ.
        user_input = e.get().lower()
        target_color = colours[1].lower()

        # BƯỚC 3: Thay đổi số điểm cộng/trừ
        # Kiểm tra câu trả lời của VÒNG TRƯỚC
        if user_input == target_color:
            score += 2  # Đúng: +2 điểm
        else:
            # Sai: -1 điểm, chỉ trừ khi người dùng đã nhập liệu
            if user_input:
                score -= 1

        # Xóa ô nhập liệu.
        e.delete(0, tkinter.END)
        
        # Xáo trộn danh sách màu để tạo màu mới cho vòng tiếp theo
        random.shuffle(colours)

        # Cập nhật nhãn màu mới: text=colours[0] (tên màu ngẫu nhiên), fg=colours[1] (màu ngẫu nhiên)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        
        # Cập nhật nhãn điểm.
        scoreLabel.config(text = "Score: " + str(score))

# Countdown timer function (Hàm đếm ngược)
def countdown():
    global timeleft
    
    if timeleft > 0:
        # Giảm thời gian
        timeleft -= 1
        
        # Cập nhật nhãn thời gian
        timeLabel.config(text = "Time left: " + str(timeleft) + "s")
        
        # Chạy lại hàm sau 1 giây
        timeLabel.after(1000, countdown)
    
    else:
        # Khi hết giờ
        label.config(text="TIME'S UP! Final Score: " + str(score))
        e.config(state='disabled') # Vô hiệu hóa ô nhập liệu khi hết giờ

# Driver Code (Mã chạy chính)
root = tkinter.Tk()
root.title("COLOR GAME")
root.geometry("375x200") 

# Thêm nhãn hướng dẫn
instructions = tkinter.Label(root, text = "Type in the colour of the words, and not the word itself!", font = ('Helvetica', 12))
instructions.pack()

# Thêm nhãn điểm (ban đầu là thông báo)
scoreLabel = tkinter.Label(root, text = "Press enter to start", font = ('Helvetica', 12))
scoreLabel.pack()

# Thêm nhãn thời gian
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft) + "s", font = ('Helvetica', 12))
timeLabel.pack()

# Thêm nhãn hiển thị màu (font lớn)
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

# Thêm ô nhập liệu
e = tkinter.Entry(root)

# Liên kết phím Enter với hàm startGame
root.bind('<Return>', startGame)
e.pack()

# Thiết lập hiển thị màu đầu tiên trước khi trò chơi bắt đầu
random.shuffle(colours)
label.config(fg = str(colours[1]), text = str(colours[0]))

# Thiết lập focus ban đầu
e.focus_set()

# Khởi động GUI
# root.mainloop()
