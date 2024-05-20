#!/bin/bash
tests=(./data/s*/*.in)
expected=(./data/s*/*.ans)
normal=0
printf "If successful intended solution is correct\n"
printf "\n"
for (( i=0; i<${#tests[*]}; ++i)); do
    filename=${tests[$i]}
    ex=$(cat ${expected[$i]})
    res1=$(timeout 2s python3 ./submissions/accepted/sol.py < $filename)
    if (( $? == 124 )); then
        normal=1
        res1=100
        printf "Timelimit exceeded on ${filename}\n"
    else
        normal=0
    fi
    if (( $res1 == $ex && $normal == 0 )); then
        printf "Success: ${filename}\n"
    else
        printf "Failed: ${filename}\n"
    fi
done
tle=0
printf "\n\n\n"
printf "If successful time limit exceeded\n"
printf "\n"
for (( i=0; i<${#tests[*]}; ++i)); do
    filename=${tests[$i]}
    res2=$(timeout 2s python3 ./submissions/time_limit_exceeded/tle.py < $filename)
    if (( $? == 124 )); then
        tle=1
        printf "Successful TLE: ${filename}\n"
    else 
        printf "Failed TLE: ${filename}\n"
    fi
done

printf "\n\n\n"
printf "If successful answer is wrong\n"
printf "\n"
wa=(./submissions/wrong_answer/*.py)
for (( i=0; i<${#tests[*]}; ++i)); do
    filename=${tests[$i]}
    ex=$(cat ${expected[$i]})
    for (( j=0; j<${#wa[*]}; ++j)); do
        testfilename=${wa[$j]}
        discription=$(head -n 1 $testfilename)
        echo
        echo $discription
        res3=$(python3 $testfilename < $filename)
        if (( $res3 != $ex )); then
            printf "Success: ${filename}\n"
        else
            printf "Failed: ${filename} ${testfilename}}\n"
        fi
    done
done
