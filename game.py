import random
import customtkinter
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


numbers_list = [i for i in range(1, 21)]
win = random.choice(numbers_list)
btn_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
lives = 0

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


def main(scr, data):
    global lives, win, lose

    g, m = numbers_range(lives)
    if data == win:
        msg = CTkMessagebox(title="Радостное окно)", message="Вы выиграли, хотите сыграть еще раз?",
                            icon="question", option_1="Да", option_2="Нет")
        response = msg.get()
        if response == "Нет":
            scr.destroy()
        else:
            scr.destroy()
            lives = 0
            cmd()

    elif data == lose:
        msg = CTkMessagebox(title="Грустное окно(", message="Вы проиграли, хотите сыграть еще раз?",
                            icon="question", option_1="Да", option_2="Нет")
        response = msg.get()
        if response == "Нет":
            scr.destroy()
        else:
            scr.destroy()
            lives = 0
            cmd()

    else:
        print(f"Ноуноуноу мистер фиш. Попытай удачи в между {g} и {m}")

    lives += 1
    if lives == 5:
        msg = CTkMessagebox(title="Ни рыба, ни мясо окно :/", message="Вы конечно не выиграли, но и не проиграли."
                                                                      "Хотите сыграть еще раз?",
                            icon="question", option_1="Да", option_2="Нет")
        response = msg.get()
        if response == "Нет":
            scr.destroy()
        else:
            scr.destroy()
            lives = 0
            cmd()


class Window(customtkinter.CTk):
    def __init__(self, btn):
        super().__init__()

        self.title("Угадай число")
        self.geometry("800x600")

        self.frame = customtkinter.CTkFrame(self, fg_color="#303030")
        self.frame.pack(side="bottom", padx=70, pady=(50, 80))

        row = 0
        column = 0
        for i in btn:
            customtkinter.CTkButton(master=self.frame, text=i, command=lambda x=i: main(self, x),
                                    font=("Comic Sans MS", 11), width=20,
                                    fg_color="#484848", hover_color="#585858").grid(row=row,
                                                                                    column=column, pady=3,
                                                                                    padx=5, ipady=5, ipadx=53
                                                                                    if int(i) < 10 else 50)
            column += 1
            if column > 4 or column > 9 or column > 14:
                column = 0
                row += 1


def cmd():
    global scr
    game = Window(btn_list)
    game.mainloop()


scr = customtkinter.CTk()

scr.title("Угадай число")
scr.geometry("800x600")

text_1 = customtkinter.CTkLabel(master=scr, text="Угадай число", font=("Comic Sans MS", 38))
text_1.pack(expand=True)

btn_1 = customtkinter.CTkButton(master=scr, text="Играть", font=("Comic Sans MS", 38), command=cmd)
btn_1.pack(expand=True)

scr.mainloop()


