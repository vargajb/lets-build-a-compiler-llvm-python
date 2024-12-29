#!/bin/bash
chk_exit_code () {
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "ErrorCode:" $retVal
        exit $retVal
    fi
}

echo Compile LLVM IR to bitcode
opt --O0 "$1.ll" -o "$1.bc"
chk_exit_code

echo Compile bitcode to assembly code
llc -filetype=asm -O0 -relocation-model=pic "$1.bc" -o "$1.asm"
chk_exit_code

#echo Compile bitcode to target Mainframe assembly code
#llc -filetype=asm -O0 -march=systemz -relocation-model=pic "$1.bc" -o "$1.systemz.asm"
#chk_exit_code

echo Compile assembly code to executable
clang "$1.asm" -o "$1"
chk_exit_code

echo Run the executable
./$1 hello
chk_exit_code
