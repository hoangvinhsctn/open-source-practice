import numpy as np
import tkinter as tk
from tkinter import Entry, Label, Button, Text, messagebox, filedialog
from PIL import Image, ImageTk
import csv

history = []


def calculate():
    try:
        matrix_input = matrix_entry.get("1.0", "end-1c")
        matrix_a = np.array([list(map(float, row.split())) for row in matrix_input.split('\n') if row.strip()])

        result = f"Largest element is: {matrix_a.max()}\n"
        result += f"Row-wise maximum elements: {matrix_a.max(axis=1)}\n"
        result += f"Column-wise minimum elements: {matrix_a.min(axis=0)}\n"
        result += f"Sum of all array elements: {matrix_a.sum()}\n"
        result += f"Cumulative sum along each row:\n{matrix_a.cumsum(axis=1)}\n"

        if matrix_a.shape[0] == matrix_a.shape[1]:  # Kiểm tra xem ma trận có phải là ma trận vuông không
            determinant = np.linalg.det(matrix_a)
            result += f"Determinant of the matrix: {determinant}"
        else:
            result += "Cannot calculate determinant for non-square matrix."

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)

        # Update the result_text for file export
        result_for_export = result_text.get("1.0", "end-1c")
        history.append(matrix_input + "\n" + result_for_export)

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")
    except np.linalg.LinAlgError as e:
        messagebox.showerror("Error", f"Error calculating determinant: {str(e)}")



def sort_rows():
    try:
        matrix_input = matrix_entry.get("1.0", "end-1c")
        matrix_a = np.array([list(map(float, row.split()))
                            for row in matrix_input.split('\n') if row.strip()])

        sorted_matrix = np.array([np.sort(row) for row in matrix_a])

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Sorted rows:\n{sorted_matrix}")

        # Update the result_text for file export
        result_for_export = result_text.get("1.0", "end-1c")
        history.append(matrix_input + "\n" + result_for_export)

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")


def calculate_median():
    try:
        matrix_input = matrix_entry.get("1.0", "end-1c")
        matrix_a = np.array([list(map(float, row.split()))
                            for row in matrix_input.split('\n') if row.strip()])

        median_value = np.median(matrix_a)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Median value: {median_value}")

        # Update the result_text for file export
        result_for_export = result_text.get("1.0", "end-1c")
        history.append(matrix_input + "\n" + result_for_export)

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")


def calculate_average():
    try:
        matrix_input = matrix_entry.get("1.0", "end-1c")
        matrix_a = np.array([list(map(float, row.split()))
                            for row in matrix_input.split('\n') if row.strip()])

        average_value = np.mean(matrix_a)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Average value: {average_value}")

        # Update the result_text for file export
        result_for_export = result_text.get("1.0", "end-1c")
        history.append(matrix_input + "\n" + result_for_export)

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")


def calculate_determinant():
    try:
        matrix_input = matrix_entry.get("1.0", "end-1c")
        matrix_a = np.array([list(map(float, row.split(','))) for row in matrix_input.split('\n') if row.strip()])

        if matrix_a.shape[0] == matrix_a.shape[1]:  # Kiểm tra xem ma trận có phải là ma trận vuông không
            determinant = np.linalg.det(matrix_a)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Determinant of the matrix: {determinant}")
            # Update the result_text for file export
            result_for_export = result_text.get("1.0", "end-1c")
            history.append(matrix_input + "\n" + result_for_export)
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Cannot calculate determinant for non-square matrix.")

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")
    except np.linalg.LinAlgError as e:
        messagebox.showerror("Error", f"Error calculating determinant: {str(e)}")



def generate_random_matrix():
    try:
        size = int(entry_size.get())
        random_matrix = np.random.rand(size, size)
        # Allow user input to the entry field
        matrix_entry.config(state=tk.NORMAL)
        matrix_entry.delete(1.0, tk.END)
        matrix_entry.insert(tk.END, "\n".join(
            " ".join(map(str, row)) for row in random_matrix))
    except ValueError:
        messagebox.showerror(
            "Error", "Invalid input. Please enter a valid size.")


def clear_data():
    matrix_entry.delete(1.0, tk.END)
    result_text.delete(1.0, tk.END)


def save_history():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
                                             ("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            for entry in history:
                file.write(entry + "\n")


def open_history():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[
                                           ("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            matrix_entry.delete(1.0, tk.END)
            matrix_entry.insert(tk.END, file.read())


def clear_history():
    history.clear()


def import_csv_matrix():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                csv_reader = csv.reader(file)
                matrix_data = list(csv_reader)

            # Hiển thị dữ liệu đúng trong ô ma trận
            matrix_entry.delete(1.0, tk.END)
            matrix_entry.insert(tk.END, "\n".join(",".join(row) for row in matrix_data))

    except Exception as e:
        messagebox.showerror("Error", f"Unable to import CSV file: {str(e)}")


def import_image():
    file_path = filedialog.askopenfilename(defaultextension=".png", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"),
                                                                               ("All files", "*.*")])
    if file_path:
        try:
            image = Image.open(file_path).convert('L')  # Convert to grayscale
            image = image.resize((300, 300))  # Resize for display
            img_tk = ImageTk.PhotoImage(image)

            image_label.img_tk = img_tk  # Keep a reference to avoid garbage collection
            image_label.config(image=img_tk)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to import image: {str(e)}")


# Thêm label để hiển thị ảnh
root = tk.Tk()
image_label = Label(root)
image_label.pack()

if __name__ == "__main__":
    root.title("Matrix Calculator")

    label = Label(
        root, text="Enter Matrix (separate elements by space and rows by newline):")
    label.pack()

    global matrix_entry
    matrix_entry = Text(root, height=5, width=30)
    matrix_entry.pack()

    calculate_button = Button(root, text="Calculate", command=calculate)
    calculate_button.pack()

    sort_rows_button = Button(root, text="Sort Rows", command=sort_rows)
    sort_rows_button.pack()

    calculate_determinant_button = Button(
        root, text="Calculate Determinant", command=calculate_determinant)
    calculate_determinant_button.pack()

    calculate_median_button = Button(
        root, text="Calculate Median", command=calculate_median)
    calculate_median_button.pack()

    calculate_average_button = Button(
        root, text="Calculate Average", command=calculate_average)
    calculate_average_button.pack()

    entry_size_label = Label(root, text="Enter size for random matrix:")
    entry_size_label.pack()

    global entry_size
    entry_size = Entry(root)
    entry_size.pack()

    generate_random_matrix_button = Button(
        root, text="Generate Random Matrix", command=generate_random_matrix)
    generate_random_matrix_button.pack()

    import_csv_button = Button(
        root, text="Import CSV Matrix", command=import_csv_matrix)
    import_csv_button.pack()

    import_image_button = Button(
        root, text="Import Image", command=import_image)
    import_image_button.pack()

    global result_text
    result_text = Text(root, height=8, width=30)
    result_text.pack()

    clear_data_button = Button(root, text="Clear Data", command=clear_data)
    clear_data_button.pack()

    save_button = Button(root, text="Save History", command=save_history)
    save_button.pack()

    open_button = Button(root, text="Open History", command=open_history)
    open_button.pack()

    clear_button = Button(root, text="Clear History", command=clear_history)
    clear_button.pack()

    root.mainloop()
