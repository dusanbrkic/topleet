module FirstUniqueCharTests exposing (..)

import Expect exposing (..)
import FirstUniqueChar exposing (firstUniqueChar)
import Test exposing (..)


suite : Test
suite =
    describe "Default Tests"
        [ test "test1" <|
            \_ ->
                firstUniqueChar "leetcode"
                    |> Expect.equal 0
        , test "test2" <|
            \_ ->
                firstUniqueChar "loveleetcode"
                    |> Expect.equal 2
        , test "test3" <|
            \_ ->
                firstUniqueChar "aabb"
                    |> Expect.equal -1
        ]
