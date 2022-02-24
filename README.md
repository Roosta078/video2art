# video2art

This script will convert any video file into a piece of art.  It will sample frames throughout the video and compute the average color of that frame.  Each sample is represented as a vertical line in the output image.  The resulting image will show the average color as the video progresses.  The intent is to use your favorite movie, but any video file will do.

## Instructions
To run on a single file:

- `./video2art.py input_video_file output_image_file`

To run on every file in a directory:

- Set line 11 of art.sh to desired video file type

- `./art.sh input_video_directory output_image_directory`

## Example Ouputs
### Finding Dory
![Finding Dory](../assests/dory.png)

### Harry Potter and The Chamber of Secrets
![Chamber](../assests/CoS.png)
