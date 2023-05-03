module AddTwoNumbersTests exposing (..)

import AddTwoNumbers exposing (addTwoNumbers)
import Expect exposing (..)
import Test exposing (..)


suite : Test
suite =
    describe "Default Tests"
        [ test "test1" <|
            \_ ->
                addTwoNumbers [ 2, 4, 3 ] [ 5, 6, 4 ]
                    |> Expect.equal [ 7, 0, 8 ]
        , test "test2" <|
            \_ ->
                addTwoNumbers [ 2, 4, 9 ] [ 5, 6, 4 ]
                    |> Expect.equal [ 7, 0, 4, 1 ]
        , test "test3" <|
            \_ ->
                addTwoNumbers [ 9, 9, 9, 9, 9, 9, 9 ] [ 9, 9, 9, 9 ]
                    |> Expect.equal [ 8, 9, 9, 9, 0, 0, 0, 1 ]
        ]
