S="wbwbwwbwbwbw"
W,B=gets.split.map(&:to_i)

w_cnt=W//7
b_cnt=B//5

for i in 0..S.size-1
    for j in 0..w_cnt
        if S[i+j]!=S[j]
            break
        end
        if j==w_cnt
            puts "w"
            exit
        end
    end
end