#!/bin/bash
tests=(./data/s*/*.in)
expected=(./data/s*/*.ans)
for (( i=0; i<${#tests[*]}; ++i)); do
    filename=${tests[$i]}
    ex=$(cat ${expected[$i]})
    res=$(python3 ./submissions/accepted/sol.py < $filename)
    # printf "${res} \n"
    # printf "${ex} \n"

    if (( $res == $ex )); then
        printf "Success \n"
    else
        printf "Failed \n"
    fi
done
