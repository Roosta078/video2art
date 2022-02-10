#!/bin/bash

echo $#
if [ $# -ne 2 ]
    then echo "proper usage: ./art.sh {input_video_directory} {output_image_directory}"
    exit 2
fi

INPUT_DIR=$1
OUTPUT_DIR=$2
VIDEO_FILE_TYPE=mkv
for f in $INPUT_DIR*.$VIDEO_FILE_TYPE
do
    CMD="./video2art.py \"$f\" \"$OUTPUT_DIR`basename -s .$VIDEO_FILE_TYPE $f`.png\""
    echo $CMD
    ./video2art.py "$f" "$OUTPUT_DIR`basename -s .$VIDEO_FILE_TYPE $f`.png"
done
