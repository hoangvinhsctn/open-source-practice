import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Đọc file và lấy dữ liệu
df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = np.array(df.iloc[:, :])

# Lấy ra tổng sinh viên
tongsv = np.sum(in_data[:, 1])

# Lấy ra tất cả các điểm
diemA = in_data[:, 3]
diemB_plus = in_data[:, 4]
diemB = in_data[:, 5]
diemC_plus = in_data[:, 6]
diemC = in_data[:, 7]
diemD_plus = in_data[:, 8]
diemD = in_data[:, 9]
diemF = in_data[:, 10]


def xoa_cac_label_cu():
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()


def solve():
    try:
        plt.clf()
        xoa_cac_label_cu()
        num_equations = int(entry.get())
        if num_equations >= 1 and num_equations <= 9:
            students = in_data[num_equations - 1, 1]
            lb1 = tk.Label(window,
                           text="Số sinh viên của lớp " + in_data[num_equations - 1, 0] + " là: " + str(students))
            lb1.pack()
            good_student = in_data[num_equations -
                                   1, 3] + in_data[num_equations - 1, 4]
            lb2 = tk.Label(
                window, text="Số sinh viên giỏi: " + str(good_student))
            lb2.pack()
            bad_student = in_data[num_equations - 1, 10]
            lb3 = tk.Label(window, text="Số sinh viên kém: " +
                           str(bad_student))
            lb3.pack()

            categories = ['Qua môn', 'Trượt môn']
            values = [students - bad_student, bad_student]

            colors = ['green', 'red']

            plt.bar(categories, values, color=colors)
            # Đặt tiêu đề cho biểu đồ
            plt.title('Thông tin sinh viên đỗ/ trượt của lớp')

            # Hiển thị biểu đồ
            plt.show()
        else:
            messagebox.showerror("Error", "Lớp không tồn tại")
    except Exception as e:
        messagebox.showerror("Error", e)

# Hàm xử lý hiển thị thông tin dưới dạng biểu đồ với từng lớp


def solve1():
    try:
        plt.close()
        num_equations = int(entry.get())
        if num_equations >= 1 and num_equations <= 9:
            scoreA = in_data[num_equations - 1, 3]
            scoreB_plus = in_data[num_equations - 1, 4]
            scoreB = in_data[num_equations - 1, 5]
            scoreC_plus = in_data[num_equations - 1, 6]
            scoreC = in_data[num_equations - 1, 7]
            scoreD_plus = in_data[num_equations - 1, 8]
            scoreD = in_data[num_equations - 1, 9]
            scoreF = in_data[num_equations - 1, 10]
            labels = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
            sizes = [scoreA, scoreB_plus, scoreB, scoreC_plus,
                     scoreC, scoreD_plus, scoreD, scoreF]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            # Vẽ biểu đồ thanh
            plt.title('Biểu đồ đánh giá số điểm lớp')
            plt.show()
        else:
            messagebox.showerror("Error", "Lớp không tồn tại")
    except Exception as e:
        messagebox.showerror("Error", e)

# Hàm vẽ biểu đồ tròn so sánh tổng số điểm của các lớp


def solve2():
    plt.close()
    averageSumA = np.sum(diemA)
    averageSumB_plus = np.sum(diemB_plus)
    averageSumB = np.sum(diemB)
    averageSumC_plus = np.sum(diemC_plus)
    averageSumC = np.sum(diemC)
    averageSumD_plus = np.sum(diemD_plus)
    averageSumD = np.sum(diemD)
    averageSumF = np.sum(diemF)

    labels = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
    sizes = [averageSumA, averageSumB_plus, averageSumB, averageSumC_plus,
             averageSumC, averageSumD_plus, averageSumD, averageSumF]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Biểu đồ đánh giá tất cả sinh viên đi thi môn học')
    plt.show()


# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Phân tích kết quả kết thúc học phần môn học")

lb = tk.Label(window, text="Nhập vào số thứ tự lớp muốn phân tích:")
lb.pack()

entry = tk.Entry(window)
entry.pack()

btn1 = tk.Button(window, text="Xem thông tin", command=solve)
btn1.pack()

btn2 = tk.Button(window, text="Xem biểu đồ", command=solve1)
btn2.pack()

btn3 = tk.Button(window, text="Xem biểu đồ phân tích chung", command=solve2)
btn3.pack()

window.mainloop()
