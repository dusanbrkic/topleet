module FirstUniqueChar exposing (firstUniqueChar)

import Dict



-- https://leetcode.com/problems/first-unique-character-in-a-string


firstUniqueChar : String -> Int
firstUniqueChar s =
    let
        charDict =
            s
                |> String.foldl
                    (\c ( dict, idx ) ->
                        ( case Dict.get c dict of
                            Nothing ->
                                Dict.insert c ( idx, 1 ) dict

                            Just ( _, n ) ->
                                Dict.insert c ( idx, n + 1 ) dict
                        , idx + 1
                        )
                    )
                    ( Dict.empty, 0 )
                |> Tuple.first
    in
    s
        |> String.foldl
            (\c found ->
                case ( Dict.get c charDict, found + 1 ) of
                    ( Just ( idx, 1 ), 0 ) ->
                        idx

                    ( _, idx ) ->
                        idx - 1
            )
            -1
