var S = stdin.readLine()

# |の間の文字列を削除, 例: test|hoge|piyo -> testpiyo
# for文で文字列を1文字ずつ見ていく

var result = ""
var isPipe = false
for i in 0..<S.len:
    if S[i] == '|':
        isPipe = not isPipe
    elif not isPipe:
        result.add(S[i])

echo result