import random
import tkinter

# создане диапазона чисел(обшего)
numbers_list = [i for i in range(1, 21)]
win = random.choice(numbers_list)

# генерация числа
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


# основной цикл
for i in range(5):
    print(f"Номер попытки: {i+1}")
    num = int(input("Число: "))
    g, m = numbers_range(i)
    if num == win:
        print("Ты победил!")
        break
    elif num == lose:
        print("Упс, это было проклятое число народа N")
        break
    else:
        print(f"Ноуноуноу мистер фиш. Попытай удачи в между {g} и {m}")
