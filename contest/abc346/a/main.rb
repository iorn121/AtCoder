N=gets.to_i
A=gets.split.map(&:to_i)

ans=[]
for i in 0..N-2
    ans.push(A[i]*A[i+1])
end

puts ans.join(" ")