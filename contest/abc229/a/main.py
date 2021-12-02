S1 = input()
S2 = input()

ans = "Yes"

if S1[0] == "#" and S1[1] == "." and S2[0] == "." and S2[1] == "#":
    ans = "No"
if S1[0] == "." and S1[1] == "#" and S2[0] == "#" and S2[1] == ".":
    ans = "No"

print(ans)
