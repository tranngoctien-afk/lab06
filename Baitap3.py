import tkinter as tk
from tkinter import ttk

def submit_data():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_entry.get()
    registered = reg_status_var.get()
    completed_courses = completed_courses_spinbox.get()
    semesters = semesters_spinbox.get()
    terms_accepted = terms_var.get()
    
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Title: {title}")
    print(f"Age: {age}")
    print(f"Nationality: {nationality}")
    print(f"Currently Registered: {registered}")
    print(f"Completed Courses: {completed_courses}")
    print(f"Semesters: {semesters}")
    print(f"Terms Accepted: {terms_accepted}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Data Entry Form")
window.geometry("500x400")
window.configure(bg='#e6f7ff')  # Đặt màu nền cửa sổ

# Khung thông tin người dùng
user_info_frame = ttk.LabelFrame(window, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = ttk.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
first_name_entry = ttk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_label = ttk.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
last_name_entry = ttk.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = ttk.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2)
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr.", "Prof."])
title_combobox.grid(row=1, column=2)

age_label = ttk.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)
age_spinbox = ttk.Spinbox(user_info_frame, from_=18, to=100)
age_spinbox.grid(row=3, column=0)

nationality_label = ttk.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)
nationality_entry = ttk.Entry(user_info_frame)
nationality_entry.grid(row=3, column=1)

# Khung đăng ký
registration_frame = ttk.LabelFrame(window, text="Registration Status")
registration_frame.grid(row=1, column=0, padx=20, pady=10)

reg_status_var = tk.StringVar(value="Not Registered")
reg_status_checkbutton = ttk.Checkbutton(registration_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
reg_status_checkbutton.grid(row=0, column=0)

completed_courses_label = ttk.Label(registration_frame, text="# Completed Courses")
completed_courses_label.grid(row=0, column=1)
completed_courses_spinbox = ttk.Spinbox(registration_frame, from_=0, to=50)
completed_courses_spinbox.grid(row=1, column=1)

semesters_label = ttk.Label(registration_frame, text="# Semesters")
semesters_label.grid(row=0, column=2)
semesters_spinbox = ttk.Spinbox(registration_frame, from_=0, to=12)
semesters_spinbox.grid(row=1, column=2)

# Khung Điều khoản và Điều kiện
terms_frame = ttk.LabelFrame(window, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, padx=20, pady=10)

terms_var = tk.StringVar(value="Not Accepted")
terms_checkbutton = ttk.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=terms_var, onvalue="Accepted", offvalue="Not Accepted")
terms_checkbutton.grid(row=0, column=0)

# Nút Gửi
submit_button = ttk.Button(window, text="Enter data", command=submit_data)
submit_button.grid(row=3, column=0, padx=20, pady=10)

window.mainloop()