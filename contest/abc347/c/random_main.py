# N,A,B を1~10**5の範囲でrandomに生成
# D をN個1~10**9の範囲でrandomに生成
# main.pyを実行して、1行目にN,A,Bを、2行目にDを入力として実行結果を得る
from random import randint
import subprocess
N=randint(1,10**2)
A=randint(1,10**5)
B=randint(1,10**5)
D=[randint(1,10**5) for _ in range(N)]
print(N,A,B)
ret = subprocess.run(['python3', 'main.py'], input=f'{N} {A} {B}\n{" ".join(map(str,D))}\n', text=True, capture_output=True).stdout
print(ret)