module RomanToIntTests exposing (..)

import Expect exposing (..)
import RomanToInt exposing (romanToInt)
import Test exposing (..)


suite : Test
suite =
    describe "Default Tests"
        [ test "test1" <|
            \_ ->
                "III"
                    |> romanToInt
                    |> Expect.equal 3
        , test "test2" <|
            \_ ->
                "LVIII"
                    |> romanToInt
                    |> Expect.equal 58
        , test "test3" <|
            \_ ->
                "MCMXCIV"
                    |> romanToInt
                    |> Expect.equal 1994
        ]
