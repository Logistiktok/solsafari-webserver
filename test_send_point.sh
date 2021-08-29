#!/bin/sh
while :
do
	HIT_NUMBER_BLUE=$((1 + $RANDOM % 10))
	HIT_NUMBER_ORANGE=$((1 + $RANDOM % 10))

	ORD='{"orangeHits":'$HIT_NUMBER_ORANGE', "blueHits":'$HIT_NUMBER_BLUE'}'
	echo "Sender Point: "$ORD

	curl -X POST -H "Content-Type: application/json" -d '{"orangeHits":'$HIT_NUMBER_ORANGE', "blueHits":'$HIT_NUMBER_BLUE'}' http://localhost:5000/point  
	#{'orangeHits': 0, 'blueHits': 0}
	echo "\n"
	sleep 1
done