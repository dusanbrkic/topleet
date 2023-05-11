module LongestCommonPrefix exposing (longestCommonPrefix)

-- https://leetcode.com/problems/longest-common-prefix/


longestCommonPrefix : List String -> String
longestCommonPrefix l =
    case List.head l of
        Nothing ->
            ""

        Just head ->
            l
                |> List.drop 1
                |> List.foldl longestPrefix head


longestPrefix : String -> String -> String
longestPrefix s1 s2 =
    if String.startsWith s2 s1 then
        s2

    else
        longestPrefix s1 (String.dropRight 1 s2)
