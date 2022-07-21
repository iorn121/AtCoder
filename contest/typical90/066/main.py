N = int(input())
LR = [tuple(map(float, input().split())) for _ in range(N)]
combinations = []
total_combinations = 1
for i in range(N):
    L, R = LR[i]
    combinations.append(int(R-L+1))
    total_combinations *= (R-L+1)
# print(total_combinations)
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        fL, fR = LR[i]
        nL, nR = LR[j]
        this_turn_ans = 0
        for formerX in range(int(fL), int(fR+1)):
            this_turn_ans += max(0, formerX-nL)-max(1, formerX-nR)+1
        ans += this_turn_ans*(total_combinations //
                              combinations[i]//combinations[j])
        # print(ans)
print(f"{ans/total_combinations:.10}")
