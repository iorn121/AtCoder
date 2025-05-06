import Data.List (findIndex)

main :: IO()
main = do
    input1 <- getLine
    let n = read input1 :: Int
    input2 <- getLine
    let heights = map read (words input2) :: [Int]

    let firstHeight = head heights

    let index = findIndex (> firstHeight) heights

    let result = case index of
            Just i -> i + 1
            Nothing -> -1
    print result