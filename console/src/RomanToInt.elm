-- https://leetcode.com/problems/roman-to-integer/


module RomanToInt exposing (romanToInt)

import String exposing (dropLeft, slice)


romanToInt : String -> Int
romanToInt romanNumber =
    case romanNumber of
        "I" ->
            1

        "V" ->
            5

        "X" ->
            10

        "L" ->
            50

        "C" ->
            100

        "D" ->
            500

        "M" ->
            1000

        _ ->
            let
                first =
                    romanNumber
                        |> slice 0 1
                        |> romanToInt

                second =
                    romanNumber
                        |> slice 1 2
                        |> romanToInt

                restValue =
                    romanNumber
                        |> dropLeft 1
                        |> romanToInt
            in
            if first >= second then
                restValue + first

            else
                restValue - first
