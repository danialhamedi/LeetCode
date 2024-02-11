defangip :: String -> String
defangip string = concat [if char == '.' then "[" ++ ['.'] ++ "]" else [char] | char <- string]
main :: IO ()
main = do
    let input = "255.100.50.0"
    let answer = defangip input
    putStrLn answer
