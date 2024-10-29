import tkinter as tk
import random
from tkinter import messagebox


def generate():

    word = entry.get()
    if len(word) > 6 or "0123456789" in word:
        messagebox.showerror("Ошибка", "Неверный ввод")
        return 0 
    word = word.upper()
    word_list = list(word)
    key1 = ""
    for i in range(6):
        key1 += word_list.pop(random.randint(0,len(word_list)-1))
    
    key_dight = ""
    for el in word:
        key_dight += str((ord(el)-64)%10)


    Re_key = f"{key1[0:3]} {key_dight} {key1[3:6]}"

    key.configure(text=Re_key)

win = tk.Tk()
win.title("KEYGEN")
win.geometry("1300x800")

image_bg = tk.PhotoImage(file="tanki.png")
lab_bg = tk.Label(win, image=image_bg)
lab_bg.place(x=0,y=0, relwidth=1, relheight=1)

invite = tk.Label(win, text="ВВЕДИТЕ СЛОВО 6 БУКВ")
invite.place(relx=0.5, rely=0.1, anchor="center")

entry = tk.Entry(win, width=20)
entry.insert(0, "сюда")
entry.place(relx=0.45, rely=0.25)

accept_but = tk.Button(win, text="OK", width=5, command=generate)
accept_but.place(relx=0.55,rely=0.24)

key = invite = tk.Label(win, text="ВАШ БУДУЮЩИЙ КОД", font=("Consolas", 20))
invite.place(relx=0.5, rely=0.5, anchor="center")



win.mainloop()