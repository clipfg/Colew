import random
import tkinter

numbers_list = [i for i in range(1, 21)]
win = random.choice(numbers_list)

if win == 1:
    lose = random.choice(numbers_list[1:])
elif win == 20:
    lose = random.choice(numbers_list[:19])
else:
    lose = random.choice(numbers_list[:win]+numbers_list[win+1:])
print(win, lose)


while True:
    num = int(input("Число: "))
    if num == win:
        print("Ебать")
        break
    elif num == lose:
        print("лох")
        break
    else:
        print("Ноуноуноу мистер фиш")