import sys
def I(): return int(sys.stdin.readline().rstrip())


def main():

    def cnt_day(Mt, mt, cnt):
        if 35 <= Mt:
            cnt[0] += 1
        if 30 <= Mt < 35:
            cnt[1] += 1
        if 25 <= Mt < 30:
            cnt[2] += 1
        if 25 <= mt:
            cnt[3] += 1
        if mt < 0 and 0 <= Mt:
            cnt[4] += 1
        if Mt < 0:
            cnt[5] += 1
        return cnt

    N = I()
    cnt_list = [0]*6
    for _ in range(N):
        M, m = map(float, input().split())
        cnt_list = cnt_day(M, m, cnt_list)
    print(*cnt_list)


if __name__ == "__main__":
    main()
