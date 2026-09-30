import time

CSI = "\x1b["
ZERO = f"{CSI}0G"
ERAZE = f"{CSI}2K"
DEF = f"{CSI}0m"

def draw_line_flag(width, length_a, length_b):
    part_a = f"{CSI}48;5;255m{' '*length_a}{DEF}"
    part_b = f"{CSI}48;5;26m{' '*length_b}{DEF}"
    part_c = f"{CSI}48;5;255m{' '*(width - length_a - length_b)}{DEF}"
    print(f"{ZERO}{ERAZE}{part_a}{part_b}{part_c}")

def draw_flag(width, length):
    width = max(width, 18)
    length = max(length, 3)
    len = length // 3
    base = width // 18
    for k in range(3):
        for i in range(len):
            if k == 1:
                draw_line_flag(width, 0, width)
            else:
                draw_line_flag(width, base*5, base*3)

def draw_line_circle(offset, width):
    part_a = f"{' '*(offset)}"
    part_b = f"{CSI}48;5;15m{' ' * width}{DEF}"

    print(f"{part_a}{part_b}{part_a}{CSI}1B{CSI}{2*offset + width}D", end="", flush=True)

def draw_circle(r): #делать радиус четными, а то беда ужас
    if r % 2 != 0:
        r += 1
    step = 1
    width = 5*r//2
    offset = r // 2

    for line in range(2 * r):
        draw_line_circle(offset, width)
        if line < r // 2:
            width += 2 * step
            offset -= step
        elif line < 3 * r // 2 - 1:
            continue
        else:
            width -= 2 * step
            offset += step

def draw_pattern(n, r):
    n = max(n, 1)
    r = max(r, 2)
    
    for i in range(n - 1):
        draw_circle(r)
        print(f"{CSI}{7*r//2}C{CSI}{2*r}A", end = "", flush=True)
    draw_circle(r)

if __name__ == "__main__":
    #draw_flag(18, 6)
    draw_pattern(4, 4)