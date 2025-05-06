main :: IO ()
main = do
    -- N, X, Y, Zを受け取る
    input <- getLine
    let [n, x, y, z] = map read (words input) :: [Int]

    -- X<Z<Y または Y<Z<X かどうかを判定
    if (x < z && z < y) || (y < z && z < x)
        then putStrLn "Yes"
        else putStrLn "No"