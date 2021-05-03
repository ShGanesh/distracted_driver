#!/bin/bash

cd pics

d=($(ls))

for img in ${d[@]}
do
	if [[ ${img:16:1} == "0" ]]
	then
		mv $img ../close
	elif [[ ${img:16:1} == "1" ]]
	then
		mv $img ../open
	fi
done
