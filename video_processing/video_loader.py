import cv2

def load_video(video_path):
    """Loads a video file at the given path using OpenCV and returns a list of its frames."""
    # Create a VideoCapture object
    video = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not video.isOpened():
        print("Error opening video file")
        return []

    frames = []
    while video.isOpened():
        # Capture frame-by-frame
        ret, frame = video.read()
        if ret:
            # If frame is read correctly, it will be True
            frames.append(frame)
        else:
            # If we've gotten here, there are no more frames, so we break the loop
            break

    # Release the video file when we're done
    video.release()

    return frames
