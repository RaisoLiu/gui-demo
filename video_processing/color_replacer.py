import cv2
import numpy as np


def replace_color(frame: np.ndarray, target_color: list, replacement_color: list, threshold: int) -> np.ndarray:
    target_color = np.array(target_color, dtype=np.uint8).reshape(1, 1, 3)
    replacement_color = np.array(replacement_color, dtype=np.uint8)

    color_difference = np.sqrt(np.sum((frame.astype(np.int32) - target_color)**2, axis=-1))
    is_close = color_difference < threshold

    frame[is_close] = replacement_color

    return frame




# def replace_color(frame, target_color, replacement_color, threshold=40):
#     """Replaces a target color in a frame with a different color.

#     Args:
#     frame: An image as a numpy array.
#     target_color: A BGR color to be replaced.
#     replacement_color: A BGR color to use as the replacement.
#     threshold: An integer controlling the strictness of the color match. Higher values will replace colors similar to the target color.

#     Returns:
#     The frame with the target color replaced by the replacement color.
#     """
#     # Convert the target and replacement colors to numpy arrays
#     target_color = np.array(target_color).reshape(1, 1, 3)
#     replacement_color = np.array(replacement_color)

#     # Create a mask for pixels close to the target color
#     color_difference = cv2.absdiff(frame, target_color)
#     mask = cv2.inRange(color_difference, np.array([0, 0, 0]), np.array([threshold, threshold, threshold]))

#     # Replace the target color with the replacement color
#     frame = cv2.addWeighted(frame, 1, mask[..., None] * replacement_color, 1, 0)

#     return frame
