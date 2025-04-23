main :: IO ()
main = do
    -- 1行目の入力を受け取る（9つの数字）
    input1 <- getLine
    let numbers1 = map read (words input1) :: [Int]

    -- 2行目の入力を受け取る（8つの数字）
    input2 <- getLine
    let numbers2 = map read (words input2) :: [Int]

    --　numbers1の和を求める
    let sum1 = sum numbers1
    -- numbers2の和を求める
    let sum2 = sum numbers2
    -- numbers1の和からnumbers2の和を引いて1を足す
    let result = sum1 - sum2 + 1
    -- 結果を出力する
    print result