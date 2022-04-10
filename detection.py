#File for body detection
import pygame
import cv2
import mediapipe as mp
import numpy as np
import time

MP_DRAWING = mp.solutions.drawing_utils
MP_DRAWING_STYLES = mp.solutions.drawing_styles
MP_POSE = mp.solutions.pose

#Return coords
def midpoint(point1: tuple, point2: tuple, rounding = False) -> tuple:
    x1, y1 = point1
    x2, y2 = point2
    return (int(round((x1 + x2) / 2)), int(round((y1 + y2) / 2))) if rounding else ((x1 + x2) / 2, (y1 + y2) / 2)

#Tracks Right landmarks (Refer to mediapipe pose)
def find_hand(
    results, 
    right_knife_trail,
    width, 
    height):
    right_hand_is_visible = True

    if results.pose_landmarks:
        right_pinky = results.pose_landmarks.landmark[18]
        right_index = results.pose_landmarks.landmark[20]

        if right_pinky.visibility >= 1 and right_index.visibility >= 1:
            right_hand_is_visible = True
            
        right_hand = midpoint(
            (width - right_pinky.x * width, right_pinky.y * height), 
            (width - right_index.x * width, right_index.y * height), rounding = True)
        right_knife_trail.append((right_hand, time.time()))
        return (
            right_hand if right_hand_is_visible else None) 
    else:
        return None

#Function to draw pose from media pipe
def draw_pose(pose, frame, background) -> tuple:
    background = background.copy()

    process_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    process_image.flags.writeable = False
    results = pose.process(process_image)

    #Draw pose
    MP_DRAWING.draw_landmarks(
        background,
        results.pose_landmarks,
        MP_POSE.POSE_CONNECTIONS,
        landmark_drawing_spec=MP_DRAWING_STYLES.get_default_pose_landmarks_style())

    return results, background
