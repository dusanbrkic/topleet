module ValidParentheses exposing (isValid)


isValid : String -> Bool
isValid s =
    let
        opening =
            "({["

        closing =
            ")}]"
    in
    s
        |> String.foldl
            (\c ( stack, _ ) ->
                case ( String.indices (String.fromChar c) opening, String.indices (String.fromChar c) closing ) of
                    ( _, [] ) ->
                        ( c :: stack, False )

                    ( [], closed ) ->
                        case List.head stack of
                            Nothing ->
                                ( [], False )

                            Just head ->
                                if String.indices (String.fromChar head) opening == closed then
                                    ( List.drop 1 stack, True )

                                else
                                    ( [], False )

                    ( _, _ ) ->
                        ( [], False )
            )
            ( [], False )
        |> Tuple.second
