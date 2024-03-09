import algorithm

var ans = newSeq[string]()

while true:
    var n = stdin.readLine()
    ans.add(n)
    if n == "0":
        break

for a in reversed(ans):
    echo a
