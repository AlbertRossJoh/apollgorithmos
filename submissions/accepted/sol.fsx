// sol.fsx
open System
open System.Collections

let rec readLines n acc =
    match n with
    | 0 -> List.rev acc
    | _ -> let line = Console.ReadLine()
           readLines (n - 1) (line :: acc)

int (Console.ReadLine())
let elms = Console.ReadLine().Split ' '
let M = int (Console.ReadLine())
let lines = readLines M []

let map2 = Hashtable()
lines 
    |> List.map (fun str -> 
        let words = str.Split [|' '|]
        (words.[2], (words.[0], words.[1])))
    |> List.iter (fun (k, v) -> map2.Add(k, v))

let goal = Console.ReadLine()
let mutable mem = Hashtable()
elms |> Array.iter (fun elm -> mem.Add(elm,1))

let sol goal =
    let rec aux elm =
        if mem.Contains elm then
            mem.Item(elm) :?> int
        else
            let res =
                if map2.Contains(elm) then
                    let (f, s) = map2.Item(elm) :?> (string*string)
                    (aux f) + (aux s)
                else
                    1
            mem.Add(elm,res)
            mem.Item(elm) :?> int
    let value = aux goal
    value - 1
    
printfn "%A" (sol goal)
