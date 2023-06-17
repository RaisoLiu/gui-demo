import random

def select_frames(frames, num_frames):
    """Randomly selects a given number of frames from a list of frames."""
    num_frames = min(num_frames, len(frames))  # Ensure we don't try to select more frames than are available
    return random.sample(frames, num_frames)
