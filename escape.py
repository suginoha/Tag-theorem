#auto aim & escape
import os
import time
import random
import math


def writeScreen(screen, w, h, tgt, turn, esp):
    os.system('clear')
    for y in range(h):print(screen[y * w:y * w + w])
    print("turn result escapeSpeed", turn, len(tgt), esp)


def tgtMove(tgt, w, h, ax, ay, esp):
    nTgt = []
    out = [(ax, ay)]
    for i in tgt:
        x, y, tn = i
        e = []
        for i in range(72):
            th = (i * 5) * 3.1415 / 180
            dx = int(math.sin(th) * esp)
            dy = int(math.cos(th) * esp)
            #print(dx, dy)
            nx, ny = x + dx, y + dy
            if (nx, ny) in out:continue
            if nx < 0 or ny < 0 or nx > w - 1 or ny > h - 1:continue
            leng = (ax - nx) ** 2 + (ay - ny) ** 2
            e  += [(leng, nx, ny)]
        if len(e) == 0:
            nTgt  += [(x, y, tn)]
            out  += [(x, y)]
            continue
        e.sort()
        _, tx, ty = e[-1]
        nTgt  += [(tx, ty, tn)]
        out  += [(tx, ty)]
    return nTgt


def main():
    w, h = 40, 40 #width height
    ax, ay, sp = w // 2, h // 2, 10 #aimX, aimY, aimSpeed
    esp, tgtNum = 12, 100 #escapeSpeed, targetNum
    tgt = [(random.randint(0, w - 1), random.randint(0, h - 1), i) for i in range(tgtNum)]
    tgt = list(set(tgt))
    turn = 0
    while len(tgt) > 0:
        turn  += 1
        screen = " " * w * h
        for i in tgt:
            x, y, n = i
            p = x + y * w
            screen = screen[:p] + str(n%10) + screen[p + 1:]
        p = ax * ay * w
        dontMove = False
        for i in tgt:
            x, y, n = i
            if (x, y) == (ax, ay):dontMove = True
        if dontMove == False:
            bLeng, bx, by = 100000, -1, -1
            for ti, i in enumerate(tgt):
                x, y, _ = i
                leng = ((x - ax) ** 2 + (y - ay) ** 2) ** 0.5
                if leng <= sp:
                    bx, by = x, y
                    break
                if leng < bLeng:
                    bx = ax + (x - ax) * sp / leng
                    by = ay + (y - ay) * sp / leng
                    bLeng = leng
            ax, ay = bx, by
        for i in tgt:
            x, y, n = i
            if (x, y) == (ax, ay):
                tgt.remove((ax, ay, n))
                p = x + y * w
                screen = screen[:p] + "X" + screen[p + 1:]
                break
        p = int(ax) + int(ay) * w
        if screen.find("X") == -1:screen = screen[:p] + "@" + screen[p + 1:]
        if turn%10 == 0:writeScreen(screen, w, h, tgt, turn, esp)
        tgt = tgtMove(tgt, w, h, ax, ay, esp)
        #time.sleep(0.1)
    os.system('clear')
    print("turn", turn)


main()
