import pygame
import cv2

fruit_types = [
    [
        {
            'name': 'bomb',
            'icon': 'test',
            'points': 0,
            'velocity': 35,
            'spawnRate': 0.15,
            'size': (200,200)
        },
        {
            'name': 'babyFood',
            'icon': 'test',
            'points': 5,
            'velocity': 60,
            'spawnRate': 0.2,
            'size': (200,200)
        },
        {
            'name': 'james',
            'icon': 'test',
            'points': 5,
            'velocity': 60,
            'spawnRate': 0.3,
            'size': (200,200)
        },
        {
            'name': 'putin',
            'icon': 'test',
            'points': 5,
            'velocity': 60,
            'spawnRate': 0.3,
            'size': (200,200)
        },
    ]
]

class Fruits():
    x = 0
    y = 0
    rotate = 0
    up = True

    #Define fruits object
    def __init__(self, name, img_filepath, starting_point, size, velocity, points):
        self.name = name
        self.velocity = round(velocity)
        self.points = points

        self.x = round(starting_point[0]) 
        self.y = round(starting_point[1])
        self.rotation = 0
        self.pygame_surface = pygame.image.load(img_filepath).convert_alpha()
        self.pygame_surface = pygame.transform.scale(self.pygame_surface, size)
        self.rect = self.pygame_surface.get_rect()
        self.size = self.pygame_surface.get_width(), self.pygame_surface.get_height()
        self.cv2_image = cv2.imread(img_filepath, cv2.IMREAD_UNCHANGED)


