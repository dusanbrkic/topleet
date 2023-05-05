module LongestCommonPrefixTests exposing (..)

import Expect exposing (..)
import LongestCommonPrefix exposing (longestCommonPrefix)
import Test exposing (..)


suite : Test
suite =
    describe "Default Tests"
        [ test "test1" <|
            \_ ->
                longestCommonPrefix [ "b", "bbbbbbb" ]
                    |> Expect.equal "b"
        , test "test2" <|
            \_ ->
                longestCommonPrefix [ "abcabcabc", "abcabcabc", "abcabcabc", "abcabcabddc", "abcabcabcdd" ]
                    |> Expect.equal "abcabcab"
        , test "test3" <|
            \_ ->
                longestCommonPrefix [ "This" ]
                    |> Expect.equal "This"
        , test "test4" <|
            \_ ->
                longestCommonPrefix []
                    |> Expect.equal ""
        , test "test5" <|
            \_ ->
                longestCommonPrefix [ "abbaca", "abbaba" ]
                    |> Expect.equal "abba"
        , test "test6" <|
            \_ ->
                longestCommonPrefix [ "flower", "flow", "flight" ]
                    |> Expect.equal "fl"
        ]
