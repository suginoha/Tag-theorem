import os #auto aim
import time
import random


def writeScreen(screen, w, h):
    os.system('clear')
    for y in range(h):
        print(screen[y * w:y * w + w])


def main():
    w ,h = 78, 23
    tgt = [(random.randint(0, w-1), random.randint(0, h-1)) for i in range(50)]
    tgt = list(set(tgt))
    ax, ay, sp = w // 2, h // 2, 10
    while len(tgt) > 0:
        screen = " " * w * h
        for i in tgt:
            x, y = i
            p = x + y * w
            screen = screen[:p] + "T" + screen[p + 1:]
        p = ax * ay * w
        for i in tgt:
            x, y = i
            if (x, y) == (ax, ay):
                tgt.remove((ax, ay))
                p = x + y * w
                screen = screen[:p] + "X"+screen[p + 1:]
                break
        if screen.find("X") == -1:
            bLeng, bx, by = 10000, -1, -1
            for i in tgt:
                x, y = i
                leng = ((x - ax) ** 2 + (y - ay) ** 2) **0.5
                if leng <= sp:
                    bx, by = x, y
                    break
                if leng < bLeng:
                    bx = ax + (x - ax) * sp / leng
                    by = ay + (y - ay) * sp / leng
                    bLeng = leng
            ax, ay = bx, by
        p = int(ax) + int(ay) * w
        if screen.find("X") == -1:screen = screen[:p] + "@" + screen[p + 1:]
        writeScreen(screen, w, h)
        time.sleep(0.02)
    os.system('clear')


main()
