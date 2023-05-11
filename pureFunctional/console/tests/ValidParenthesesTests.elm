module ValidParenthesesTests exposing (..)

import Expect exposing (..)
import Test exposing (..)
import ValidParentheses exposing (isValid)


suite : Test
suite =
    describe "Default Tests"
        [ test "test1" <|
            \_ ->
                isValid "()[]{}"
                    |> Expect.equal True
        , test "test2" <|
            \_ ->
                isValid "(({[{[()[]{}]}]}))"
                    |> Expect.equal True
        , test "test3" <|
            \_ ->
                isValid "(((}))"
                    |> Expect.equal False
        , test "test4" <|
            \_ ->
                isValid "((())){"
                    |> Expect.equal False
        ]
