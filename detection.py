#File for body detection
import pygame
import cv2
import mediapipe as mp
import numpy as np

MP_DRAWING = mp.solutions.drawing_utils
MP_DRAWING_STYLES = mp.solutions.drawing_styles
MP_POSE = mp.solutions.pose


#Function to draw pose from media pipe
def draw_pose(pose, frame, background) -> tuple:
    background = background.copy()

    process_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # improve performance by optionally marking image as not writeable
    process_image.flags.writeable = False
    results = pose.process(process_image)

    # draw pose
    MP_DRAWING.draw_landmarks(
        background,
        results.pose_landmarks,
        MP_POSE.POSE_CONNECTIONS,
        landmark_drawing_spec=MP_DRAWING_STYLES.get_default_pose_landmarks_style())

    return results, background
