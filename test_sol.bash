#!/bin/bash
tests=(./data/s*/*.in)
expected=(./data/s*/*.ans)
extensions=("py" "fsx" "cpp")
commandtorun=("python3 " "dotnet fsi" "/usr/bin/g++ -std=c++11")
optionalcommand=("" "" "&& timeout 2 ./a.out")
normal=0

for (( j=0; j<${#extensions[*]}; ++j )); do
    extension=${extensions[$j]}
    command=${commandtorun[$j]}
    optional=${optionalcommand[$j]}
    printf "\n"
    printf "${extension}\n"
    for (( i=0; i<${#tests[*]}; ++i)); do
        filename=${tests[$i]}
        ex=$(cat ${expected[$i]})
        cmd="${command} ./submissions/accepted/sol.${extension} ${optional} < $filename"
        res1=$(eval timeout 2 $cmd)
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
done
tle=0
printf "\n\n"
for (( j=0; j<${#extensions[*]}; ++j )); do
    extension=${extensions[$j]}
    command=${commandtorun[$j]}
    optional=${optionalcommand[$j]}
    printf "\n"
    printf "If successful time limit exceeded extension: ${extension}\n"
    for (( i=0; i<${#tests[*]}; ++i)); do
        filename=${tests[$i]}
        cmd="${command} ./submissions/time_limit_exceeded/tle.${extension} ${optional} < $filename"
        # res2=$(timeout 2s ${command} ./submissions/time_limit_exceeded/tle.${extension} ${optional} < $filename)
        res2=$(eval timeout 2 $cmd)
        if (( $? == 124 )); then
            tle=1
            printf "Successful TLE: ${filename}\n"
        else 
            printf "Failed TLE: ${filename}\n"
        fi
    done
done

printf "\n\n\n"
printf "If successful answer is wrong\n"
printf "\n"
wa=(./submissions/wrong_answer/*.py)
for (( j=0; j<${#wa[*]}; ++j)); do
    testfilename=${wa[$j]}
    discription=$(head -n 1 $testfilename)
    echo
    echo $discription
    for (( i=0; i<${#tests[*]}; ++i)); do
        filename=${tests[$i]}
        ex=$(cat ${expected[$i]})
        res3=$(python3 $testfilename < $filename)
        if (( $res3 != $ex )); then
            printf "Success: ${filename}\n"
        else
            printf "Failed: ${filename} ${testfilename}}\n"
        fi
    done
done
