module Example exposing (..)

import Expect exposing (Expectation)
import Fuzz exposing (Fuzzer, int, list, string)
import Test exposing (..)


suite : Test
suite =
    describe "Sanity Tests"
        [ test "test1" <|
            \_ ->
                let
                    helloWorld =
                        "Hello World!"
                in
                Expect.equal helloWorld "Hello World!"
        ]
