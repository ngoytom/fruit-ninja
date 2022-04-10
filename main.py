import pygame, sys
import cv2
import mediapipe as mp

from detection import MP_POSE

import time
import numpy as np

import detection
from fruits import Fruits, fruit_types

#Create Screen
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
CAP_WIDTH, CAP_HEIGHT = 1280, 720 #Video Capture Size
clock = pygame.time.Clock()
FPS = 60

#Global
pygame.display.set_caption("Fruit Ninja")
#BG = "assets/background.jpeg"
ROUND_COOLDOWN = 2 #Seconds
SUBSCRIBE = pygame.image.load("assets/subscribe.png")
SUBSCRIBE = pygame.transform.scale(SUBSCRIBE, (300, 300))

#Fonts
pygame.font.init()
TITLE_FONT = pygame.font.Font('assets/Ninja Font.ttf', 45)

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#Drawing detection
MP_POSE = mp.solutions.pose
#background_cv2_image = cv2.imread(BG)

#List of tuples that store coords of knife trail, and when they're drawn
right_knife_trail = []

def display():
    #Main Menu Display
    starting_title = TITLE_FONT.render("GAME NAME", False, RED)
    screen.blit(starting_title, (400, 100)) #x , y
    screen.blit(SUBSCRIBE, (400, 300))

def main(): 
    run = True #game is running
    start_game = False #game has not started

    start_fruit = None #slice this fruit to start game
    
    #Pose object to detect motion of user
    with MP_POSE.Pose(
        min_detection_confidence = 0.7,
        min_tracking_confidence=0.5,
        model_complexity=0) as pose:
        
        #Open cv webcamera
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAP_WIDTH)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAP_HEIGHT)
        cap.set(cv2.CAP_PROP_FPS, 60)
        while cap.isOpened() and run:
            clock.tick(FPS)

            ret, frame = cap.read() #Frame returns image from webcame
            
            #Process webcam image to track pose, and draw it on image_to_display
            results, image_to_display = detection.draw_pose(
                pose, 
                frame,
                frame)
            
            #Display Mediapipe on PyGame Surface
            frame = cv2.cvtColor(image_to_display, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            surf = pygame.surfarray.make_surface(frame)
            screen.blit(surf, (0,0))

            # pass mutable reference of knife_trail lists, add trails based on results, and get coords of hands
            right_hand = detection.knife_trails_and_find_hands(
                results, 
                right_knife_trail, 
                WIDTH, 
                HEIGHT)

            print (right_hand)
                
            if start_game == False:
                icon_size = (400, 300)
                start_pos = (375, 400)
                start_fruit = Fruits(
                    name="Subscribe",
                    img_filepath="assets/subscribe.png",
                    starting_point=start_pos,
                    size=icon_size,
                    velocity=0,
                    points=0
                )
                
            for event in pygame.event.get(): #Get Events
                if event.type == pygame.QUIT: #Quit Event
                    pygame.quit()
                    run = False
                    sys.exit()

            #update display
            display()
            pygame.display.update()

if __name__ == "__main__":
    main()