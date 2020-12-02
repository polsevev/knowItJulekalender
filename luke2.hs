isPrime k = if k > 1 then null [ x | x <- [2..k - 1], k `mod` x == 0] else False

closestPrime y = head ([x | x <- reverse ([2..y]), isPrime x])

isInList l
        |'7'`elem` (show l) =True
        |otherwise=False

checkStuff:: [Int] -> [Int]
checkStuff [] = []
checkStuff (x:xs)
    | isInList x = checkStuff (drop (closestPrime x) xs)
    | otherwise = x: checkStuff xs

findNumberOfPackages = length ([0,1,2,3,4,5,6] ++ checkStuff [7..5433000])
