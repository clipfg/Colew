import random
import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


numbers_list = [i for i in range(1, 21)]
win = random.choice(numbers_list)

if win == 1:
    lose = random.choice(numbers_list[1:])
elif win == 20:
    lose = random.choice(numbers_list[:19])
else:
    lose = random.choice(numbers_list[:win]+numbers_list[win+1:])


# подсказки
def numbers_range(r):
    global win
    range_list = [10, 8, 5, 3, 2]
    r = (range_list[r] - 1)
    if win - r <= 1:
        start = random.randint(1, win)
        return start, start + r
    if win - r > 1:
        start = random.randint(win - r, win)
        if start + r <= 20:
            return start, start + r
        else:
            return 20 - r, 20


win = customtkinter.CTk()

win.title = "Угадай число"
win.geometry("800x600")

text_1 = customtkinter.CTkLabel(master=win, text="Угадай число", font=("Comic Sans MS", 38))
text_1.pack(expand=True)

btn_1 = customtkinter.CTkButton(master=win, text="Играть", font=("Comic Sans MS", 38))
btn_1.pack(expand=True)

win.mainloop()


# основной цикл
# for i in range(5):
#     print(f"Номер попытки: {i+1}")
#     num = int(input("Число: "))
#     g, m = numbers_range(i)
#     if num == win:
#         print("Ты победил!")
#         break
#     elif num == lose:
#         print("Упс, это было проклятое число народа N")
#         break
#     else:
#         print(f"Ноуноуноу мистер фиш. Попытай удачи в между {g} и {m}")
