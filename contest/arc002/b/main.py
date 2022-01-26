import datetime
Y, M, D = map(int, input().split('/'))


def check(y, m, d):
    return y % (m*d) == 0


while not check(Y, M, D):
    newDay = datetime.date(Y, M, D)+datetime.timedelta(days=1)
    Y, M, D = newDay.year, newDay.month, newDay.day

print(f'{Y}/{M:02}/{D:02}')
