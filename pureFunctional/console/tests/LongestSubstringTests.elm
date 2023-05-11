module LongestSubstringTests exposing (..)

import Expect exposing (..)
import LongestSubstring exposing (lengthOfLongestSubstring)
import Test exposing (..)


suite : Test
suite =
    describe "Default Tests"
        [ test "test1" <|
            \_ ->
                lengthOfLongestSubstring "bbbbbbb"
                    |> Expect.equal 1
        , test "test2" <|
            \_ ->
                lengthOfLongestSubstring "abcabcbb"
                    |> Expect.equal 3
        , test "test3" <|
            \_ ->
                lengthOfLongestSubstring "ddc"
                    |> Expect.equal 2
        , test "test4" <|
            \_ ->
                lengthOfLongestSubstring " "
                    |> Expect.equal 1
        , test "test5" <|
            \_ ->
                lengthOfLongestSubstring "abba"
                    |> Expect.equal 2
        , test "test6" <|
            \_ ->
                lengthOfLongestSubstring "pwwkew"
                    |> Expect.equal 3
        ]
