module LongestSubstring exposing (..)

import Dict



-- https://leetcode.com/problems/longest-substring-without-repeating-characters/


lengthOfLongestSubstring : String -> Int
lengthOfLongestSubstring s =
    let
        iterData =
            { charDict = Dict.empty, total = 0, start = 0 }
    in
    s
        |> String.toList
        |> List.indexedMap Tuple.pair
        |> List.foldl
            (\( current, c ) acc ->
                let
                    dict =
                        Dict.insert c current acc.charDict
                in
                case Dict.get c acc.charDict of
                    Just idx ->
                        let
                            start =
                                max acc.start (idx + 1)
                        in
                        { charDict = dict
                        , start = start
                        , total = max acc.total (current - start + 1)
                        }

                    Nothing ->
                        { charDict = dict
                        , total = max acc.total (current - acc.start + 1)
                        , start = acc.start
                        }
            )
            iterData
        |> .total
