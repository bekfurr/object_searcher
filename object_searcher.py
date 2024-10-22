import tkinter as tk
from tkinter import messagebox

def qidirish():

    a = list(map(str,entry_massiv.get().split()))  
    m = entry_qidirilayotgan_object.get()
    
    for i in range(len(a)):
        if m == a[i]:
            messagebox.showinfo("Natija", f"Object topildi! Index: {i}")
            return
    messagebox.showinfo("Natija", "object topilmadi")


root = tk.Tk()
root.title("Massivda son qidirish")
root.geometry("300x200")


label_massiv = tk.Label(root, text="Massivni kiriting (probel bilan ajratib):")
label_massiv.pack()

entry_massiv = tk.Entry(root, width=65)
entry_massiv.pack()

label_qidirilayotgan_object = tk.Label(root, text="Qidirilayotgan Objectni kiriting:")
label_qidirilayotgan_object.pack()

entry_qidirilayotgan_object = tk.Entry(root, width=30)
entry_qidirilayotgan_object.pack()


button_qidirish = tk.Button(root, text="Qidirish", command=qidirish)
button_qidirish.pack(pady=10)


root.mainloop()
