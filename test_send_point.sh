#!/bin/sh
while :
do
	HIT_NUMBER=$((1 + $RANDOM % 10))
	ORD='{"hits":'$HIT_NUMBER'}'
	echo "Sender Point: "$ORD

	curl -X POST -H "Content-Type: application/json" -d '{"hits":'$HIT_NUMBER'}' http://localhost:5000/point  
	echo "\n"
	sleep 1
done