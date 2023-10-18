import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("焦点时钟")

time_label = tk.Label(root, text="", font=("Helvetica", 48))
time_label.pack()

update_time()

root.mainloop()
