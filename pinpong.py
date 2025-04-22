from pygame import *
from random import *

run = True

window = display.set_mode((700,500))#Создание окна приложения
display.set_caption('Пинпонг')#Заголовок
window.fill((12, 211, 242))#Задний фон

while run:#Игровой цикл
    for e in event.get():#Проверка на нажание кнопки закрыть
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                reset_game()

    display.update()