import time

CIS = "\x1b["
ZERO = f"{CIS}0G"
ERAZE = f"{CIS}2K"
DEF = f"{CIS}0m"

def draw_line_flag(width, length_a, length_b):
    part_a = f"{CIS}48;5;255m{' '*length_a}{DEF}"
    part_b = f"{CIS}48;5;26m{' '*length_b}{DEF}"
    part_c = f"{CIS}48;5;255m{' '*(width - length_a - length_b)}{DEF}"
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





if __name__ == "__main__":
    draw_flag(18, 6)