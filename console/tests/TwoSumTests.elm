module TwoSumTests exposing (..)

import Expect exposing (..)
import Test exposing (..)
import TwoSum exposing (twoSum)


suite : Test
suite =
    describe "Default Tests"
        [ test "test1" <|
            \_ ->
                twoSum [ 2, 7, 11, 15 ] 9
                    |> Expect.equal (Just [ 0, 1 ])
        , test "test2" <|
            \_ ->
                twoSum [ 3, 2, 4 ] 6
                    |> Expect.equal (Just [ 1, 2 ])
        , test "test3" <|
            \_ ->
                twoSum [ 3, 3 ] 6
                    |> Expect.equal (Just [ 0, 1 ])
        ]
