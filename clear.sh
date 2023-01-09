#!/bin/bash

echo "Clearing files..."

{



find ./game -name '*.rpyc' | 
    while IFS= read -r file; do
        rm -rf $file
done

find ./game -name '*.rpy.bak' | 
    while IFS= read -r file; do
        rm -rf $file
done

find ./game -name '*.pyo' | 
    while IFS= read -r file; do
        rm -rf $file
done


rm -rf ./game/saves
} &> /dev/null


