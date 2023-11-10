#2-	Thiết kế phần mềm hỗ trợ học tập môn giải tích
import tkinter as tk

import sympy as sym


# Hàm tính đạo hàm
def calculate_derivative():
    expression = expression_entry.get()
    try:
        derivative = sym.diff(expression, x)
        result_label.config(text=f"Đạo hàm: {derivative}")
    except:
        result_label.config(text="Lỗi! Kiểm tra biểu thức đầu vào.")


# Hàm tính tích phân
def calculate_integral():
    expression = expression_entry.get()
    start = start_entry.get()
    stop = stop_entry.get()
    try:
        integral = sym.integrate(expression, (x, start, stop))
        result_label.config(text=f"Tích phân: {integral}")
    except:
        result_label.config(text="Lỗi! Kiểm tra biểu thức đầu vào.")


# Hàm tính giới hạn
def calculate_limit():
    expression = expression_entry.get()
    limit_point = limit_point_entry.get()
    try:
        value = sym.limit(expression, x, limit_point)
        result_label.config(text=f"Giới hạn tại x = {limit_point}: {value}")
    except:
        result_label.config(text="Lỗi! Kiểm tra giới hạn hoặc biểu thức đầu vào.")


# Hàm giải phương trình
def solve_equation():
    expression = expression_entry.get()
    y_str = y_entry.get()

    try:
        # Chuyển đổi chuỗi thành biểu thức SymPy
        equation = sym.sympify(expression)
        y = sym.sympify(y_str)

        # Tạo phương trình SymPy với Eq
        equation = sym.Eq(equation, y)

        # Giải phương trình
        solution = sym.solve(equation, x)

        result_label.config(text=f"Kết quả: {solution}")
    except:
        result_label.config(text="Lỗi! Kiểm tra giới hạn hoặc biểu thức đầu vào.")


# Tạo biến ký tự
x = sym.symbols('x')

# Tạo giao diện
# Tạo cửa sổ ứng dụng
app = tk.Tk()
app.title("Phần mềm hỗ trợ học tập Giải tích")

expression_label = tk.Label(app, text="Nhập biểu thức theo x(VD: x**2+2*x+1):")
expression_label.pack()

expression_entry = tk.Entry(app)
expression_entry.pack()

calculate_derivative_button = tk.Button(app, text="Tính Đạo hàm", command=calculate_derivative)
calculate_derivative_button.pack()

start_label = tk.Label(app, text="điểm đầu:")
start_label.pack()

start_entry = tk.Entry(app)
start_entry.pack()

stop_label = tk.Label(app, text="điểm cuối:")
stop_label.pack()

stop_entry = tk.Entry(app)
stop_entry.pack()

calculate_integral_button = tk.Button(app, text="Tính Tích phân", command=calculate_integral)
calculate_integral_button.pack()

limit_point_label = tk.Label(app, text="Nhập điểm giới hạn (x):")
limit_point_label.pack()

limit_point_entry = tk.Entry(app)
limit_point_entry.pack()

calculate_limit_button = tk.Button(app, text="Tính Giới hạn", command=calculate_limit)
calculate_limit_button.pack()

y_label = tk.Label(app, text="Nhập vế phải của phương trình")
y_label.pack()

y_entry = tk.Entry(app)
y_entry.pack()

solve_button = tk.Button(app, text="Giải phương trình", command=solve_equation)
solve_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
