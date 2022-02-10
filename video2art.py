#!/usr/bin/env python3
import sys

import cv2
from math import trunc
import png

print(cv2.__version__)



if __name__=="__main__":
    if len(sys.argv) != 3:
        print(len(sys.argv))
        print("incorrect arguements\nProper usage: ./video2art.py {input_video_file} {output_image_file}")
        exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    cap=cv2.VideoCapture(input_file)
    if cap.isOpened() == False:
        print(f"error opening video file: {input_file}")
        exit()
    success, frame=cap.read()
    if success == False:
        print("Video opened, but frame grab unsuccessful")
        exit()
    width=1920
    height=1080
    output=[]

    success = True
    count =1
    row = ()
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if frame_count <= width:
        width = frame_count-5

    multiplier= trunc(frame_count/width)
    print(frame_count)
    print(multiplier)
    for x in range(width):
        cap.set(cv2.CAP_PROP_POS_FRAMES,(x*multiplier))
        success,frame=cap.read()
        #print(success)
        avg=frame.mean(axis=(0,1))
        print(f"{x} out of {width}")
        row = row + (trunc(avg[2]), trunc(avg[1]), trunc(avg[0]))
        if x==(width/2):
            cv2.imwrite("./out.png", frame)
    for y in range(height):
        output.append(row)

    with open(output_file, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, output)
        print(f"wrote to {output_file}")

    #print(success)
    #print(frame.shape)
    #red=frame.mean(axis=(0,1))
    #print(red)
    #cv2.imwrite("./out.png", frame)
