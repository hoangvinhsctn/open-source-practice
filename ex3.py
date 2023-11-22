import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox


def activeRectangle():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        x = np.array([0, a])
        y = np.array([0, b])

        perimeter = (a + b) * 2
        area = a * b

        showResult(perimeter, area)

        plt.clf()

        plt.plot([0, x[0]], [0, x[1]], 'b-')
        plt.plot([x[0], y[1]], [x[1], x[1]], 'b-')
        plt.plot([y[1], y[1]], [x[1], 0], 'b-')
        plt.plot([y[1], 0], [0, 0], 'b-')

        plt.title('Vẽ HCN')
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def activeSquare():
    try:
        a = float(entry_a.get())

        x = np.array([0, a])

        perimeter = a * 4
        area = a ** 2

        showResult(perimeter, area)

        plt.clf()

        plt.plot([0, x[0]], [0, x[1]], 'b-')
        plt.plot([x[0], x[1]], [x[1], x[1]], 'b-')
        plt.plot([x[1], x[1]], [x[1], 0], 'b-')
        plt.plot([x[1], 0], [0, 0], 'b-')

        plt.title('Vẽ hình vuông')
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def activeTriangle():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a + b > c and a + c > b and b + c > a:
            # Tính toán tọa độ các đỉnh của tam giác
            A = np.array([0, 0])
            B = np.array([b, 0])
            cos_angle = (b ** 2 + a ** 2 - c ** 2) / (2 ** a ** b)
            sin_angle = np.sqrt(1 - cos_angle ** 2)

            height = a * sin_angle

            C = np.array([a * cos_angle, height])

            # Tính chu vi và diện tích tam giác
            perimeter = a + b + c
            s = perimeter / 2  # Nửa chu vi
            area = np.sqrt(s * (s - a) * (s - b) * (s - c))

            showResult(perimeter, area)

            plt.clf()

            plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
            plt.plot([B[0], C[0]], [B[1], C[1]], 'b-')
            plt.plot([C[0], A[0]], [C[1], A[1]], 'b-')

            plt.title('Vẽ tam giác')
            plt.show()
        else:
            messagebox.showwarning(
                "Warning", "Ba cạnh vừa nhập không tạo thành tam giác")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def showResult(perimeter, area):
    result.delete(1.0, tk.END)
    result.insert(tk.END, "Kết quả:\n")
    result.insert(tk.END, f"Chu vi: {perimeter}\n")
    result.insert(tk.END, f"Diện tích: {area}")


window = tk.Tk()
window.title('App hỗ trợ hình học')

label_a = tk.Label(window, text="Cạnh thứ nhất: ")
label_a.pack()

entry_a = tk.Entry(window)
entry_a.pack()

label_b = tk.Label(window, text="Cạnh thứ hai: ")
label_b.pack()

entry_b = tk.Entry(window)
entry_b.pack()

label_c = tk.Label(window, text="Cạnh thứ ba: ")
label_c.pack()

entry_c = tk.Entry(window)
entry_c.pack()

result_label = tk.Label(window)
result_label.pack()

btn_activeTg = tk.Button(window, text="Vẽ tam giác", command=activeTriangle)
btn_activeTg.pack()

btn_activeHCN = tk.Button(window, text="Vẽ HCN", command=activeRectangle)
btn_activeHCN.pack()


btn_activeHV = tk.Button(window, text="Vẽ Hình vuông", command=activeSquare)
btn_activeHV.pack()

result_label = tk.Label(window, text="Result")
result_label.pack()

result = tk.Text(window, height=5, width=40)
result.pack()

window.mainloop()
