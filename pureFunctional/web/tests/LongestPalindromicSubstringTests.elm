module LongestPalindromicSubstringTests exposing (..)

import Expect exposing (..)
import LongestPalindromicSubstring exposing (longestPalindromicSubstring)
import Test exposing (..)


suite : Test
suite =
    describe "Default Tests"
        [ test "test1" <|
            \_ ->
                longestPalindromicSubstring "babad"
                    |> Expect.equal "bab"
        , test "test2" <|
            \_ ->
                longestPalindromicSubstring "cbbd"
                    |> Expect.equal "bb"
        , test "test3" <|
            \_ ->
                longestPalindromicSubstring "abcda"
                    |> Expect.equal "a"
        , test "test4" <|
            \_ ->
                longestPalindromicSubstring "dfddawaqqaqqaqqaqqaabbaasd"
                    |> Expect.equal "aqqaqqaqqaqqa"
        , test "test5" <|
            \_ ->
                longestPalindromicSubstring "dfddawqaqaqaabbaasd"
                    |> Expect.equal "aabbaa"
        , test "test6" <|
            \_ ->
                longestPalindromicSubstring "faaaadqbq"
                    |> Expect.equal "aaaa"
        , test "test7" <|
            \_ ->
                longestPalindromicSubstring "faaaaadssss"
                    |> Expect.equal "aaaaa"
        ]
