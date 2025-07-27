# Vehicle-counter-tracker
# Vehicle Counter and Tracker

This project is a real-time vehicle detection and counting system developed using Python and OpenCV. It processes video input (either from a file or a live camera feed) and counts vehicles that pass through a defined virtual line. The system uses background subtraction and contour detection to identify and track moving vehicles in the frame.

Preview


https://github.com/user-attachments/assets/d80889fd-5e01-4323-854c-50b03eb5fbba




## Features

- Processes video frames in real-time
- Detects and tracks moving vehicles
- Counts vehicles that cross a predefined virtual line
- Displays live vehicle count on the video
- Uses basic image processing techniques for motion detection

## Tech Stack

- **Programming Language:** Python
- **Libraries:** OpenCV (cv2), NumPy (optional)

## How It Works

1. The program captures video input using OpenCV’s `VideoCapture`.
2. Background subtraction is applied to isolate moving objects from the static background.
3. Each frame is processed using grayscale conversion and Gaussian blur to reduce noise.
4. Contours are extracted from the foreground mask to detect objects.
5. A virtual line is drawn across the frame, and vehicle movement is tracked.
6. When the center point of a detected vehicle crosses the line, the counter is incremented.
7. The count is displayed on the video feed in real-time.

## File Structure

vehicle-counter/
│
├── vehicle_counter.py       # Main script for video processing and vehicle counting
├── traffic.mp4              # Sample input video (optional)
