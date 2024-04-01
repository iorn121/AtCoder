S="wbwbwwbwbwbw"*20
W,B=gets.split.map(&:to_i)


for i in 0..11
    w_cnt=0
    b_cnt=0
    for j in i..i+W+B-1
        if S[j]=="w"
            w_cnt+=1
        else
            b_cnt+=1
        end
    end
    # puts "i:#{i}, w_cnt:#{w_cnt}, b_cnt:#{b_cnt}"
    if w_cnt==W && b_cnt==B
        puts "Yes"
        exit
    end
end
puts "No"