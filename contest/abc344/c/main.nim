import sequtils
import strutils
import sets

var N=stdin.readLine.parseInt
var A=stdin.readLine.split.map parseInt

var M=stdin.readLine.parseInt
var B=stdin.readLine.split.map parseInt

var L=stdin.readLine.parseInt
var C=stdin.readLine.split.map parseInt

var num_set: HashSet[int]

for i in 0..<N:
    for j in 0..<M:
        for k in 0..<L:
            var num=A[i]+B[j]+C[k]
            num_set.incl(num)

var Q=stdin.readLine.parseInt
var X=stdin.readLine.split.map parseInt

for i in 0..<Q:
    if num_set.contains(X[i]):
        echo "Yes"
    else:
        echo "No"