module AddTwoNumbers exposing (..)

-- https://leetcode.com/problems/add-two-numbers/


addTwoNumbers : List Int -> List Int -> List Int
addTwoNumbers pl1 pl2 =
    let
        ( l1, l2 ) =
            preprocess pl1 pl2
    in
    l1
        |> List.map2 Tuple.pair l2
        |> List.foldl
            (\( e1, e2 ) ( overflow, result ) ->
                let
                    value =
                        e1 + e2 + overflow
                in
                ( value // 10, result ++ [ modBy 10 value ] )
            )
            ( 0, [] )
        |> (\( overflow, result ) ->
                if overflow > 0 then
                    result ++ [ overflow ]

                else
                    result
           )


preprocess : List Int -> List Int -> ( List Int, List Int )
preprocess l1 l2 =
    let
        lengthDif =
            List.length l1 - List.length l2
    in
    if lengthDif > 0 then
        ( l1, l2 ++ List.repeat lengthDif 0 )

    else if lengthDif < 0 then
        ( l1 ++ List.repeat (abs lengthDif) 0, l2 )

    else
        ( l1, l2 )
