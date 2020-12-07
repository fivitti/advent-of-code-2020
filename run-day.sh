#! /bin/sh

DAY_PREFIX="day-$1"
SCRIPT_FILE="$DAY_PREFIX.py"

if [[ $# > 1 ]]; then
    DATA_FILE="${DAY_PREFIX}-$2.data"
else
    DATA_FILE="${DAY_PREFIX}.data"
fi

echo Script $DAY_PREFIX using $DATA_FILE
cat $DATA_FILE | python $SCRIPT_FILE
