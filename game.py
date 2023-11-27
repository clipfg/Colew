#TODO Добавить фон и музяку (в общем довести дизайн с беты до альфы)

import random

import customtkinter
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("Dark")

btn_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
lives = 0


def logic():
    numbers_list = [i for i in range(1, 21)]

    win = random.choice(numbers_list)

    if win == 1:
        lose = random.choice(numbers_list[1:])
    elif win == 20:
        lose = random.choice(numbers_list[:19])
    else:
        lose = random.choice(numbers_list[:win-1]+numbers_list[win:])

    return win, lose


# подсказки
def numbers_range(r):
    global win
    range_list = [10, 8, 5, 3, 2, 1]
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
    global lives, win, lose, btns

    btn = btns[data]

    g, m = numbers_range(lives)

    if data == win:
        btn.configure(fg_color="green")
        scr.text.configure(text=f"Победа :D")
        msg = CTkMessagebox(title="Радостное окно)", message="Вы выиграли, хотите сыграть еще раз?",
                            icon="question", option_1="Да", option_2="Нет", button_color="#303030")
        response = msg.get()
        if response == "Нет":
            scr.destroy()
        else:
            lives = 0
            win, lose = logic()
            cmd()

    elif data == lose:
        btn.configure(fg_color="red")
        scr.text.configure(text=f"Ты проиграл(")
        msg = CTkMessagebox(title="Грустное окно(", message="Вы проиграли, хотите сыграть еще раз?",
                            icon="question", option_1="Да", option_2="Нет", button_color="#303030")
        response = msg.get()
        if response == "Нет":
            scr.destroy()
        else:
            lives = 0
            win, lose = logic()
            cmd()

    else:
        btn.configure(state="disabled")
        scr.text.configure(text=f"Не угадал) попробуй найти между {g} и {m}")

    lives += 1
    if lives == 6:
        scr.text.configure(text="Ты проиграл")
        msg = CTkMessagebox(title="Ни рыба, ни мясо окно :/", message="Вы конечно не выиграли, но и не проиграли."
                                                                      " Хотите сыграть еще раз?",
                            icon="question", option_1="Да", option_2="Нет", button_color="#303030")
        response = msg.get()
        if response == "Нет":
            scr.destroy()
        else:
            lives = 0
            win, lose = logic()
            cmd()


class Window(customtkinter.CTk):
    def __init__(self, btn):
        super().__init__()
        self.destroy_list = []
        self.btn_list = btn

    def mod_2(self):
        global btns
        self.title("Угадай число")
        self.geometry("800x600")
        self.text = customtkinter.CTkLabel(master=self, text=f"Итак, угадай число",
                                           font=("Comic Sans MS", 30))
        self.text.pack(expand=True)
        self.frame = customtkinter.CTkFrame(self, fg_color="#303030")
        self.frame.pack(side="bottom", padx=70, pady=(50, 80))
        self.destroy_list.append(self.frame)
        self.destroy_list.append(self.text)
        row = 0
        column = 0
        btns = {}
        for i in self.btn_list:
            btn_i = (customtkinter.CTkButton(master=self.frame, text=i, command=lambda x=i: main(self, int(x)),
                                    font=("Comic Sans MS", 11), width=20,
                                    fg_color="#484848", hover_color="#585858"))
            btns[int(i)] = btn_i
            btn_i.grid(row=row,column=column, pady=3, padx=5, ipady=5, ipadx=53 if int(i) < 10 else 50)
            column += 1
            if column > 4 or column > 9 or column > 14:
                column = 0
                row += 1

    def mod_1(self):
        self.title("Угадай число")
        self.geometry("800x600")
        text_1 = customtkinter.CTkLabel(master=self, text="Угадай число", font=("Comic Sans MS", 38))
        text_1.pack(expand=True)

        btn_1 = customtkinter.CTkButton(master=self, text="Играть", font=("Comic Sans MS", 38), command=cmd)

        btn_1.pack(expand=True)
        self.destroy_list = [text_1, btn_1]


def cmd():
    global game
    if len(game.destroy_list) > 0:
        for i in game.destroy_list:
            i.destroy()
    game.mod_2()


game = Window(btn_list)
win, lose = logic()
game.mod_1()
game.mainloop()
