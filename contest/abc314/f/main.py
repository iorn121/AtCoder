# 解説 https://atcoder.jp/contests/abc314/editorial/6978 の実装例

n = int(input())
C = [list(map(int, input().split())) for _ in range(n - 1)]
mod = 998244353

# 0-indexed に直す
for i in range(n - 1):
    for j in range(2):
        C[i][j] -= 1


def inv(x):
    """x の mod での逆元を返す。mod が素数で、x と mod が互いに素である必要あり。"""
    x %= mod
    return pow(x, mod - 2, mod)


# マージテク操作 1 回目

team = [[i] for i in range(n)]  # チーム一覧
blng = [i for i in range(n)]  # プレイヤー i は現在チーム U[i] に所属している

for i in range(n - 1):
    a, b = C[i][0], C[i][1]
    n_team_a = len(team[blng[a]])  # a が属するチームの人数
    n_team_b = len(team[blng[b]])  # b が属するチームの人数
    if n_team_a < n_team_b:
        a, b = b, a
    team[blng[a]] += team[blng[b]]
    for j in team[blng[b]]:  # 所属変更
        blng[j] = blng[a]

# 数列 A を求める
for i in range(n):
    if len(team[i]) == n:
        A = team[i]

# 番号振り直し
no_new = [-1] * n
for i in range(n):
    no_new[A[i]] = i

for i in range(n - 1):
    for j in range(2):
        C[i][j] = no_new[C[i][j]]


# マージテク操作 2 回目 (期待値の数列の構築もする)

e_imos = [0] * (n + 1)  # 期待値の数列

team = [[i] for i in range(n)]  # チーム一覧
blng = [i for i in range(n)]  # プレイヤー i は現在チーム U[i] に所属している

for i in range(n - 1):
    a, b = C[i][0], C[i][1]
    n_team_a = len(team[blng[a]])  # a が属するチームの人数
    n_team_b = len(team[blng[b]])  # b が属するチームの人数

    min_mem_a = team[blng[a]][0]  # a が属するチームの番号最小のプレイヤー
    min_mem_b = team[blng[b]][0]  # b が属するチームの番号最小のプレイヤー
    win_rate_a = (n_team_a * inv(n_team_a + n_team_b)) % mod
    win_rate_b = (n_team_b * inv(n_team_a + n_team_b)) % mod

    e_imos[min_mem_a] += win_rate_a
    e_imos[min_mem_a] %= mod
    e_imos[min_mem_a + n_team_a] -= win_rate_a
    e_imos[min_mem_a + n_team_a] %= mod

    e_imos[min_mem_b] += win_rate_b
    e_imos[min_mem_b] %= mod
    e_imos[min_mem_b + n_team_b] -= win_rate_b
    e_imos[min_mem_b + n_team_b] %= mod

    if n_team_a < n_team_b:
        a, b = b, a
    team[blng[a]] += team[blng[b]]
    for j in team[blng[b]]:  # 所属変更
        blng[j] = blng[a]

# 累積和をとる
for i in range(1, n + 1):
    e_imos[i] += e_imos[i - 1]
    e_imos[i] %= mod

# 振り直す前の番号を考慮した解答を作成
ANS = [-1] * n
for i in range(n):
    ANS[A[i]] = e_imos[i]

print(*ANS)
