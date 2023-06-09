module TwoSum exposing (..)

import Dict



-- https://leetcode.com/problems/two-sum/


twoSum : List Int -> Int -> Maybe (List Int)
twoSum nums target =
    nums
        |> List.indexedMap (\i num -> ( i, num ))
        |> List.foldr
            (\( i, num ) ( complements, acc ) ->
                case ( Dict.get (target - num) complements, acc ) of
                    ( _, Just _ ) ->
                        ( complements, acc )

                    ( Just complement, _ ) ->
                        ( complements, Just ( i, complement ) )

                    ( Nothing, _ ) ->
                        ( Dict.insert num i complements, Nothing )
            )
            ( Dict.empty, Nothing )
        |> (\( _, acc ) -> acc |> Maybe.map (\( first, second ) -> [ first, second ]))
