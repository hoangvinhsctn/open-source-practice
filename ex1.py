# 1-	Thiết kế phần mềm ứng dụng giải hệ phương trình tuyến tính n phương trình n ẩn
import tkinter as tk
from tkinter import messagebox

import numpy as np


# Hàm tạo hệ các phương trình
def create(entry):
    delete_fields()
    num_equations = int(entry.get())
    for i in range(num_equations):
        frame = tk.Frame(window)
        # Đặt frame ở trên cùng, cách lề 10 pixel và cách lề dưới 5 pixel
        frame.pack(side=tk.TOP, padx=10, pady=5)
        equation_frames.append(frame)
        # Lưu trữ các hệ số của phương trình
        equation_entries = []
        label = tk.Label(frame, text=f"Phương trình {i + 1}:")
        label.pack(side=tk.LEFT)  # Đặt label bên trái trong frame
        for j in range(num_equations + 1):
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)  # Đặt entry bên trái trong frame
            equation_entries.append(entry)

        # Lưu trữ các phương trình
        equation_entries_list.append(equation_entries)


# Hàm xóa các hệ phương trình
def delete_fields():
    result.delete(1.0, tk.END)
    equation_entries_list.clear()
    for frame in equation_frames:
        frame.destroy()


# Kiểm tra dữ liệu hợp lệ
def validate_input(entry):
    try:
        num_equations = int(entry.get())
        if num_equations <= 0 or num_equations > 10:
            raise ValueError("Nhập lại số phương trình hợp lệ.")
        return True

    except ValueError:
        messagebox.showerror("Error", "Nhập lại số phương trình hợp lệ.")
        return False


# Giải hệ phương trình vừa tạo
def solve(entry):
    try:
        coefficients = []
        results = []

        for entry_list in equation_entries_list:
            equation_coefficients = []
            for entry in entry_list[:-1]:
                val = float(entry.get())
                equation_coefficients.append(val)
            coefficients.append(equation_coefficients)

            result_val = float(entry_list[-1].get())
            results.append(result_val)

        a = np.array(coefficients)
        b = np.array(results)
        x = np.linalg.solve(a, b)

        result.delete(1.0, tk.END)
        result.insert(tk.END, "Kết quả:\n")
        for i, val in enumerate(x):
            result.insert(tk.END, f"x{i + 1} = {round(val, 2)}\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Giải hệ phương trình tuyến tính")

equation_entries_list = []
equation_frames = []

# Nhập số phương trình n
n_level = tk.Label(window, text="Nhập số phương trình (max = 10)")
n_level.pack()  # Sử dụng pack() thay vì grid()
n_entry = tk.Entry(window)
n_entry.pack()  # Sử dụng pack() thay vì grid()

# Tạo button tạo hệ phương trình
btn_create = tk.Button(window, text="Create", command=lambda: validate_input(
    n_entry) and create(n_entry))
btn_create.pack()  # Sử dụng pack() thay vì grid()

# Tạo button xóa hệ phương trình
btn_delete = tk.Button(window, text="Delete", command=delete_fields)
btn_delete.pack()  # Sử dụng pack() thay vì grid()

# Tạo button giải hệ phương trình
btn_solve = tk.Button(window, text="Solve", command=lambda: solve(n_entry))
btn_solve.pack()  # Sử dụng pack() thay vì grid()

# Hiển thị kết quả
result_label = tk.Label(window, text="Result")
result_label.pack()  # Sử dụng pack() thay vì grid()
result = tk.Text(window, height=3, width=30)
result.pack()  # Sử dụng pack() thay vì grid()

window.mainloop()
