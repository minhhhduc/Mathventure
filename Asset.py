import pygame
class Player(object):
    _instance = None

    def __new__(cls, x: int = 0, y: int = 0, dt: float = 0, distance: float = 300):
        if (cls._instance is None):
            cls._instance = super(Player, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.dt = dt
            cls._instance.distance = distance

        return cls._instance

    def __init__(self, x: int = 0, y: int = 0, dt: float = 0, distance: float = 300) -> None:
        self.x = x
        self.y = y
        self.dt = dt
        self.distance = distance
        self.point = 0
        self.speed = self.distance * self.dt
        self.rect = pygame.Rect(self.x + 11, self.y + 15, 15, 15)
    
    """ def up(self):
        if (self.y - self.speed < 0):
            self.y = 0
        else:
            self.y -= self.speed
    
    def down(self, bound):
        if (self.y + self.speed >= bound):
            self.y = bound
        else:
            self.y += self.speed
    
    def left(self):
        if (self.x - self.speed < 0):
            self.x = 0
        else:
            self.x -= self.speed
    
    def right(self, bound):
        if (self.x + self.speed >= bound):
            self.x = bound
        else:
            self.x += self.speed """
    
    def get_pos(self):
        return (self.x, self.y)
    
    def move(self, dx, dy, walls):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0, walls)
        if dy != 0:
            self.move_single_axis(0, dy, walls)

    def move_single_axis(self, dx, dy, walls):
        
        # Move the rect
        self.resx = self.x
        self.resy = self.y
        self.x += dx
        self.y += dy
        self.rect.x += dx
        self.rect.y += dy
         # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    self.x = self.resx
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    self.x = self.resx
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    self.y = self.resy
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    self.y = self.resy