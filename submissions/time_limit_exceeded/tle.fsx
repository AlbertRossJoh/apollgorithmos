// sol.fsx
open System

let rec readLines n acc =
    match n with
    | 0 -> List.rev acc
    | _ -> let line = Console.ReadLine()
           readLines (n - 1) (line :: acc)

let N = int (Console.ReadLine())
let elms = Console.ReadLine().Split ' '
let M = int (Console.ReadLine())
let lines = readLines M []

let map = 
    lines 
    |> List.map (fun str -> 
        let words = str.Split [|' '|]
        (words.[2], (words.[0], words.[1])))
    |> Map.ofSeq

let goal = Console.ReadLine()
let sol map goal (elms: string array) =
    let rec aux elm =
        let children = Map.tryFind elm map
        match children with
        | None -> 1
        | _ ->
            (aux (fst children.Value)) + (aux (snd children.Value))
            
    let value = aux goal
    value - 1
    
printfn "%A" (sol map goal (elms))
