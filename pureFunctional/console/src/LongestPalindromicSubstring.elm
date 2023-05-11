module LongestPalindromicSubstring exposing (longestPalindromicSubstring)

import Array



-- https://leetcode.com/problems/longest-palindromic-substring/


longestPalindromicSubstring : String -> String
longestPalindromicSubstring s =
    let
        sArr =
            Array.fromList (String.toList s)

        findLongest lArr =
            lArr
                |> List.foldl
                    (\arr maximum ->
                        if Array.length maximum < Array.length arr then
                            arr

                        else
                            maximum
                    )
                    (Array.fromList [])

        search lIdx rIdx found =
            let
                first =
                    Array.get 0 found

                left =
                    Array.get lIdx sArr

                right =
                    Array.get rIdx sArr

                foundEven =
                    if Array.length found == 1 && first == right then
                        search lIdx (rIdx + 1) (Array.slice (lIdx + 1) (rIdx + 1) sArr)

                    else
                        Array.fromList []

                foundOdd =
                    if left == right && left /= Nothing && lIdx >= 0 then
                        search (lIdx - 1) (rIdx + 1) (Array.slice lIdx (rIdx + 1) sArr)

                    else
                        Array.fromList []
            in
            findLongest [ found, foundEven, foundOdd ]
    in
    s
        |> String.foldl
            (\c ( idx, found ) ->
                let
                    newFound =
                        search (idx - 1) (idx + 1) (Array.fromList [ c ])
                in
                ( idx + 1, findLongest [ found, newFound ] )
            )
            ( 0, Array.fromList [] )
        |> Tuple.second
        |> Array.toList
        |> String.fromList
