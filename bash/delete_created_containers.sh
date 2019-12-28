#!/bin/bash

containers_with_header=$(docker ps --filter "status=created" | awk '{print $1 }')
#echo "${containers_with_header}"
lines_with_header=$(echo "${containers_with_header}" | wc -l)
#echo $lines_with_header
lines_without_header=$(expr ${lines_with_header} - 1)
#echo "${lines_without_header}"

for OUTPUT in $(echo "${containers_with_header}" | tail -n ${lines_without_header})
do
	docker rm $OUTPUT
done
