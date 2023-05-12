import cv2
import numpy as np
import moviepy.editor as mp
import os

# Load the video file using OpenCV
video_path = "HyperSkill/Videos/P1011757_Proxy.mp4"
cap = cv2.VideoCapture(video_path)
os.environ['IMAGEIO_FFMPEG_EXE'] = 'HyperSkill/Videos/ffmpeg'

# Get the video properties
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the minimum threshold for audio volume and motion detection
audio_threshold = 0.5
motion_threshold = 1000

# Define the output file name and codec
out_file = "HyperSkill/Videos/output.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Initialize the video writer
out = cv2.VideoWriter(out_file, fourcc, frame_rate,
                      (frame_width, frame_height))

# Iterate over the video frames
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Compute the audio volume
    audio_volume = np.mean(frame)

    # Compute the frame difference
    if prev_gray is not None:
        frame_diff = cv2.absdiff(gray, prev_gray)
        motion = np.sum(frame_diff)
    else:
        motion = 0

    # Check if the audio volume and motion are below the threshold
    if audio_volume < audio_threshold and motion < motion_threshold:
        continue

    # Write the frame to the output video
    out.write(frame)

    # Update the previous frame
    prev_gray = gray

# Release the resources
cap.release()
out.release()

# Use moviepy to crop the video
clip = mp.VideoFileClip(out_file).subclip()
clip.write_videofile(out_file)
