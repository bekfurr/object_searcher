import tkinter as tk
from tkinter import messagebox

def qidirish():
    a = list(map(str, entry_massiv.get().split()))
    m = entry_qidirilayotgan_object.get()
    hisobchi = 0
    indeks_xab = ""

    for i in range(len(a)):
        if m == a[i]:
            if hisobchi == 0:
                indeks_xab = f"Object topildi! Index:{i}"
            else:
                indeks_xab += f", {i}"
            hisobchi += 1

    if hisobchi > 0:
        messagebox.showinfo("Natija", f"{indeks_xab}\nObject ro'yxatda {hisobchi} marta foydalanilgan")
    else:
        messagebox.showinfo("Natija", "Object topilmadi")

oyna = tk.Tk()
oyna.title("Massivda son qidirish")
oyna.geometry("500x200")

label_massiv = tk.Label(oyna, text="Massivni kiriting (probel bilan ajratib):")
label_massiv.pack()

entry_massiv = tk.Entry(oyna, width=85)
entry_massiv.pack()

label_qidirilayotgan_object = tk.Label(oyna, text="Qidirilayotgan Objectni kiriting:")
label_qidirilayotgan_object.pack()

entry_qidirilayotgan_object = tk.Entry(oyna, width=50)
entry_qidirilayotgan_object.pack()

button_qidirish = tk.Button(oyna, text="Qidirish", command=qidirish)
button_qidirish.pack(pady=10)

oyna.mainloop()

# CODE CREATED WITH PYHTON AT 10.27.2024
# CODER: @BEKFURR
# Github Repository link:https://github.com/bekfurr/Obeject_qidir
