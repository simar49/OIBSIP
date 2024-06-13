import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

def create_connection():
    conn = sqlite3.connect('bmi_data.db')
    return conn

def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bmi_records
                 (user TEXT, date TEXT, weight REAL, height REAL, bmi REAL)''')
    conn.commit()

def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    return bmi

def save_bmi_data(conn, user, weight, height, bmi):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c = conn.cursor()
    c.execute("INSERT INTO bmi_records (user, date, weight, height, bmi) VALUES (?, ?, ?, ?, ?)",
              (user, date, weight, height, bmi))
    conn.commit()

def view_history(conn, user):
    c = conn.cursor()
    c.execute("SELECT date, weight, height, bmi FROM bmi_records WHERE user=? ORDER BY date", (user,))
    records = c.fetchall()
    
    history_list.delete(0, tk.END)  # Clear the listbox before adding new records
    if records:
        for record in records:
            history_list.insert(tk.END, f"Date: {record[0]}, Weight: {record[1]}, Height: {record[2]}, BMI: {record[3]}")
    else:
        messagebox.showinfo("No Records", "No records found for the specified user.")

def plot_bmi_trend(conn, user):
    c = conn.cursor()
    c.execute("SELECT date, bmi FROM bmi_records WHERE user=? ORDER BY date", (user,))
    records = c.fetchall()
   
    if records:
        dates = [datetime.strptime(record[0], "%Y-%m-%d %H:%M:%S") for record in records]
        bmis = [record[1] for record in records]

        plt.plot(dates, bmis, marker='o')
        plt.xlabel('Date')
        plt.ylabel('BMI')
        plt.title(f'BMI Trend for {user}')
        plt.grid(True)
        plt.show()
    else:
        messagebox.showinfo("No Records", "No records found for the specified user.")

def on_calculate():
    try:
        user = entry_user.get()
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = calculate_bmi(weight, height)
        save_bmi_data(conn, user, weight, height, bmi)
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for weight and height.")

def on_view_history():
    user = entry_user.get()
    view_history(conn, user)

def on_plot_trend():
    user = entry_user.get()
    plot_bmi_trend(conn, user)

# Establish the database connection and create the table
conn = create_connection()
create_table(conn)

# Set up the GUI
root = tk.Tk()
root.title("BMI CALCULATOR")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1)

tk.Label(root, text="Height (cm):").grid(row=2, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=2, column=1)

btn_calculate = tk.Button(root, text="Calculate BMI", command=on_calculate)
btn_calculate.grid(row=3, column=0, columnspan=2)

history_list = tk.Listbox(root, width=50, height=10)
history_list.grid(row=4, column=0, columnspan=2)

btn_view_history = tk.Button(root, text="View History", command=on_view_history)
btn_view_history.grid(row=5, column=0, columnspan=2)

btn_plot_trend = tk.Button(root, text="Plot BMI Trend", command=on_plot_trend)
btn_plot_trend.grid(row=6, column=0, columnspan=2)

# Run the GUI event loop
root.mainloop()

# Close the database connection when the GUI is closed
conn.close()