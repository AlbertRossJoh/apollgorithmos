#!/bin/bash
tests=(./data/s*/*.in)
expected=(./data/s*/*.ans)
tle=0
normal=0
for (( i=0; i<${#tests[*]}; ++i)); do
    filename=${tests[$i]}
    ex=$(cat ${expected[$i]})
    res1=$(timeout 3s python3 ./submissions/accepted/sol.py < $filename)
    if (( $? == 124 )); then
        normal=1
        res1=100
        printf "Timelimit exceeded on ${filename}\n"
    else
        normal=0
    fi
    res2=$(timeout 3s python3 ./submissions/time_limit_exceeded/tle.py < $filename)
    # printf "${res} \n"
    # printf "${res2} \n"
    if (( $? == 124 )); then
        tle=1
    fi

    if (( $res1 == $ex && $normal == 0 )); then
        printf "Success: ${filename}\n"
    else
        printf "Failed: ${filename}\n"
    fi
done
if (( $tle == 1 )); then
    printf "Successful TLE\n"
else
    printf "Failed TLE\n"
fi
