import time
import os

CSI = "\x1b["
ZERO = f"{CSI}0G"
ERAZE = f"{CSI}2K"
DEF = f"{CSI}0m"

def draw_line_flag(width, length_white_1, length_blue_1):
    length_white_2 = width - length_white_1 - length_blue_1
    white_1 = f"{CSI}48;5;255m{' '*length_white_1}{DEF}" #белый цвет
    blue_1 = f"{CSI}48;5;26m{' '*length_blue_1}{DEF}" #голубой цвет
    white_2 = f"{CSI}48;5;255m{' '*length_white_2}{DEF}" #белый цвет
    print(f"{white_1}{blue_1}{white_2}")

def draw_flag(width, length):
    width = max(width, 18)
    length = max(length, 3)

    #флаг Финляндии имеет 3 цвета, округляем вниз
    line_len = length // 3

    #флаг Финляндии имеет такие пропорции по горизантали: 5 - белый; 3 - синий; 10 белый
    base = width // 18
    length_white = base * 5
    length_blue = base * 3

    for k in range(3):
        for i in range(line_len):
            if k == 1:
                draw_line_flag(width, 0, width)
            else:
                draw_line_flag(width, length_white, length_blue)

def draw_line_circle(offset, width, color, color_offset):
    part_a = f"{' '*(offset)}"
    part_b = f"{CSI}48;5;{color}m{' ' * width}{DEF}"

    print(f"{part_a}{part_b}{part_a}{CSI}1B{CSI}{2*offset + width}D", end="", flush=True)

def draw_circle(r, color, color_offset): #при нечетном радиусе ломается симметрия
    if r % 2 != 0:
        r += 1

    step = 1
    # ширина = 5*r//2 — эмпирически подобрано так, чтобы круг
    # выглядел круглым, а не вытянутым (символ терминала выше, чем шире)
    width = 5*r//2
    offset = r // 2

    for line in range(2 * r):
        draw_line_circle(offset, width, color, color_offset)
        if line < r // 2:
            #верхняя часть расширяется
            width += 2 * step
            offset -= step
        elif line < 3 * r // 2 - 1:
            #средняя часть круга не меняется
            continue
        else:
            #нижняя часть круга сужается
            width -= 2 * step
            offset += step

def draw_pattern(n, r):
    n = max(n, 1)
    r = max(r, 2)

    color = 255 #цвет круга
    color_offset = 0 
    
    for i in range(n - 1):
        draw_circle(r, color, color_offset)
        #сдвигаем курсор вправо на максимальную ширину круга, поднимаем вверх на диаметр круга
        #end = "", потому что иначе print сбрасывает курсор на нулевой столбец следующей строки
        print(f"{CSI}{7*r//2}C{CSI}{2*r}A", end = "", flush=True)
    draw_circle(r, color, color_offset)

def draw_part_animation(color1, color2, color3):
    #color1 - зеленый
    #color2 - желтый
    #color3 - красный

    color_offset = 0

    r = 4

    draw_circle(r, color3, color_offset)
    print()

    draw_circle(r, color2, color_offset)
    print()

    draw_circle(r, color1, color_offset)
    print()

def draw_animation(): #нарисовать анимцаию светофора с 4 кадрами
    #нужно переделать будет без os.system("clear") используя CSI n k(удаление)
    # и CSI перемещение курсора
    os.system("clear")
    while True:
        for i in range(4):
            if i == 0: #все цвета выключены
                draw_part_animation(28, 143, 124)
            elif i == 1: #включен красный
                draw_part_animation(28, 143, 196)
            elif i == 2: #включен желтый
                draw_part_animation(28, 226, 124)
            elif i == 3: #включен зеленый
                draw_part_animation(118, 143, 124)
            time.sleep(1)
            os.system("clear")
            
    

if __name__ == "__main__":
    #1 задание нарисовать флаг Финляндии
    #draw_flag(18, 6)

    #2 задание нарисовать заданный узор
    #draw_pattern(4, 4)

    #3 задание нарисовать анмиацию на 3-4 кадра
    #draw_animation()
    pass