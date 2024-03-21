import pygame


class Wall:
    def __init__(self, pos):
       self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

class ProductBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "*"
        self.point = point
        self.is_once = is_once

class SumBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "+"
        self.point = point
        self.is_once = is_once

class SignalBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "-"
        self.point = point
        self.is_once = is_once

class ExpBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "^"
        self.point = point
        self.is_once = is_once

class QuotientBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "/"
        self.point = point
        self.is_once = is_once
class MapGame:
    start = 255
    def __init__(self, level, target, level_img):
        self.target = target
        self.level = level
        self.level_img = level_img
        self.level_img = pygame.transform.scale(self.level_img, (1920/12, 1080/12))
        self.points = []
        self.walls = []
        x = self.start
        y = 100
        for row in self.level:
            for col in row:
                if col[0] == "W":
                    self.walls.append(Wall((x, y)))    
                elif col[0] == "*":
                    point = 1
                    s = col.split("*")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("*")[2])
                    self.points.append(ProductBlock((x, y), point, is_once))
                elif col[0] == "-":
                    point = 0
                    s = col.split("-")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("-")[2])
                    self.points.append(SignalBlock((x, y), point, is_once))
                elif col[0] == "+":
                    point = 0
                    s = col.split("+")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("+")[2])
                    self.points.append(SumBlock((x, y), point, is_once))
                elif col[0] == "^":
                    point = 1
                    s = col.split("^")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("^")[2])
                    self.points.append(ExpBlock((x, y), point, is_once))
                elif col[0] == "/":
                    point = 1
                    s = col.split("/")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("/")[2])
                    self.points.append(QuotientBlock((x, y), point, is_once))
                elif col[0] == "f":
                    self.finish = (x, y)
                elif col[0] == "s":
                    self.start = (x, y)
                x += 32
            y += 32
            x = self.start


path_img_level = ["assets/level/1.png", "assets/level/2.png", "assets/level/3.png", 
                  "assets/level/4.png", "assets/level/5.png", "assets/level/6.png",
                  "assets/level/7.png", "assets/level/8.png", "assets/level/9.png"]

img_level = [pygame.image.load(path) for path in path_img_level]


#(((8*12 - 99)^3)*12)
target_1 = -324
level_1 = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "*12*True", " ", " ", " ", "-99-True", " ", "^3^False", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W", "W", "W", "W", "W", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W", "W", "W", "W", " ", " ", "W"],
    ["W", " ", "W", "W", "W", " ", " ", "W", "W", "W", "W", " ", " ", " ", "+12+False", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W", "W", "W", " ", "W", "W"],
    ["W", " ", " ", " ", "W", "W", "W", " ", "W", "W", "W", " ", " ", " ", "W", " ", "W", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W", " ", " ", " ", "W", " ", "W", " ", " ", "W"],
    ["W", "W", "W", "W", " ", " ", "W", " ", " ", " ", "W", "W", "W", "W", "W", " ", "W", " ", " ", "W"],
    ["W", " ", " ", "W", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", "W", " ", " ", "W", "W", "W", "W", "W", " ", " ", "W", "W", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
]

target_2 = 9
level_2 = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", " ", "+1+False", " ", "W", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", "W", "W", " ", "W", " ", " ", " ", " ", "W", " ", "W", "W", "W", "W", "W", "W", "W", " ", "W"],
    ["W", " ", "W", " ", "W", "W", "*7*False", " ", "W", "W", " ", " ", " ", " ", " ", " ", " ", "W", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", "W", "W", " ", " ", " ", " ", " ", " ", "W", " ", "W"],
    ["W", "W", "W", " ", " ", " ", " ", "W", " ", " ", "W", " ", "W", "W", "^2^True", "W", " ", "W", " ", "W"],
    ["W", " ", "W", " ", "W", "W", " ", "W", "W", " ", "W", "W", "W", " ", " ", "W", " ", "W", " ", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
    ["W", "W", "W", " ", "W", " ", " ", " ", "W", " ", " ", " ", " ", "W", " ", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", "W", "W", "W", "W", " ", " ", " ", "W", "W", "W", " ", "W"],
    ["W", " ", " ", " ", "/3/False", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W", " ", "W"],
    ["W", "W", "W", " ", " ", " ", "W", " ", " ", " ", "W", "W", "W", "W", "W", " ", " ", "W", " ", "W"],
    ["W", " ", "W", " ", " ", " ", "W", " ", " ", " ", "W", " ", " ", "-3-False", " ", " ", " ", "W", " ", "W"],
    ["W", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", "W", " ", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]
]
target_3 = -36
level_3 = [
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "+12+False" , "W" , " " , " " , " " , "W" , " " , " " , " " , " " , " " , "W" , " " , " " , "W" , " " , " " , " " , "W"],
    ["W" , " " , "W" , "W" , "W" , " " , "W" , "W" , "W" , " " , " " , " " , "W" , " " , " " , "W" , " " , " " , " " , "W"],
    ["W" , " " , "W" , " " , "W" , " " , " " , " " , "W" , "W" , " " , " " , "W" , " " , "W" , "W" , "W" , "W" , " " , "W"],
    ["W" , " " , " " , " " , "W" , "-7-True" , " " , " " , " " , "W" , " " , " " , " " , " " , "W" , " " , " " , "W" , " " , "W"],
    ["W" , "W" , "W" , " " , "W" , " " , "W" , " " , " " , "W" , "*12*True" , "W" , "W" , " " , "W" , " " , "W" , "W" , " " , "W"],
    ["W" , " " , " " , " " , "W" , "W" , "W" , " " , " " , "W" , " " , "W" , "W" , " " , "W" , " " , "W" , " " , " " , "W"],
    ["W" , "W" , "W" , " " , " " , " " , " " , " " , " " , "W" , " " , " " , " " , " " , "W" , " " , "W" , " " , " " , "W"],
    ["W" , " " , "W" , "W" , " " , " " , " " , " " , " " , "W" , "W" , "W" , " " , " " , " " , " " , "W" , "W" , " " , "W"], 
    ["W" , " " , " " , "W" , "W" , "W" , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , "W" , " " , "W"],
    ["W" , " " , " " , "W" , " " , "/3/False" , " " , " " , " " , " " , " " , " " , " " , " " , "W" , "W" , " " , "W" , " " , "W"],
    ["W" , " " , " " , "W" , " " , "W" , "W" , "W" , "W" , "W" , "W" , "W" , " " , "W" , "W" , " " , " " , " " , " " , "W"],
    ["W" , " " , " " , "W" , " " , " " , " " , " " , "W" , " " , " " , " " , " " , "W" , "^2^False" , " " , "W" , "W" , "W" , "W"],
    ["W" , " " , " " , "W" , "W" , "W" , "W" , " " , "W" , " " , "W" , "W" , "W" , "W" , " " , " " , "W" , " " , " " , "W"],
    ["W" , " " , " " , " " , " " , " " , " " , " " , "W" , " " , "W" , " " , " " , " " , " " , " " , " " , " " , " " , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"]
]

target_4 = 6
level_4 = [
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , " " , " " , "W" , " " , " " , " " , " " , " " , " " , "W" , " " , " " , " " , "W" , " " , " " , " " , " " , "W"],
    ["W" , " " , " " , "W" , "W" , "W" , " " , " " , " " , " " , "W" , " " , " " , " " , "W" , " " , " " , " " , " " , "W"],
    ["W" , " " , " " , " " , " " , "W" , " " , " " , " " , " " , "W" , " " , " " , "W" , "W" , " " , "W" , " " , " " , "W"],
    ["W" , "W" , "W" , " " , " " , "W" , " " , " " , "W" , "W" , "W" , "-3-False" , " " , " " , " " , " " , "W" , " " , " " , "W"],
    ["W" , " " , "W" , " " , " " , "W" , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , "W" , "W" , "W" , "W"],
    ["W" , " " , "W" , " " , " " , "W" , "*5*False" , " " , " " , " " , " " , " " , " " , "W" , " " , " " , "W" , "-4-True" , " " , "W"],
    ["W" , " " , "W" , " " , " " , " " , " " , " " , " " , " " , "W" , " " , " " , " " , " " , " " , "W" , " " , " " , "W"],
    ["W" , " " , "W" , " " , " " , " " , " " , " " , " " , " " , "W" , " " , " " , " " , " " , " " , "W" , " " , " " , "W"], 
    ["W" , " " , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , " " , " " , " " , " " , "+1+True" , "W" , " " , " " , "W"],
    ["W" , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , "W"],
    ["W" , " " , " " , "/2/True" , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , "W"],
    ["W" , " " , " " , "W" , "W" , "W" , "W" , "W" , "W" , "W" , " " , " " , "W" , "W" , "W" , " " , " " , " " , " " , "W"],
    ["W" , " " , " " , " " , " " , " " , "W" , " " , " " , " " , " " , " " , " " , " " , "W" , " " , " " , "^2^False" , " " , "W"],
    ["W" , " " , " " , " " , " " , " " , "W" , " " , " " , " " , " " , " " , " " , " " , "W" , " " , " " , " " , " " , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"]
]


target_5 = 149
level_5 = [
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , " " , " " , "W" , " " , " " , " " , " " , " " , " " , " " , " " , "W" , " " , " " , " " , " " , " " , " " , "W"],
    ["W" , " " , "+3+True" , "W" , " " , " " , " " , " " , " " , " " , " " , " " , "W" , " " , " " , " " , " " , " " , " " , "W"],
    ["W" , " " , " " , "W" , " " , " " , "W" , " " , " " , " " , " " , "W" , "W" , "W" , " " , " " , "W" , " " , "*99*False" , "W"],
    ["W" , " " , " " , "W" , " " , " " , "W" , " " , " " , " " , " " , " " , " " , " " , " " , " " , "W" , "W" , "W" , "W"],
    ["W" , " " , "W" , "W" , " " , " " , "W" , "W" , "W" , " " , " " , "+1+True" , " " , " " , " " , " " , "W" , " " , " " , "W"],
    ["W" , " " , " " , " " , " " , " " , "W" , " " , "W" , " " , " " , " " , " " , " " , " " , " " , "W" , " " , " " , "W"],
    ["W" , " " , " " , " " , " " , " " , "W" , " " , " " , " " , " " , " " , " " , " " , " " , "W" , "W" , " " , " " , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , " " , " " , " " , " " , " " , " " , " " , "W"], 
    ["W" , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , "W"],
    ["W" , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , "W" , " " , " " , "W"],
    ["W" , " " , " " , "W" , "W" , " " , " " , "W" , "W" , "W" , "W" , " " , " " , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , " " , " " , "*7*False" , "W" , " " , " " , "W" , " " , " " , "W" , " " , " " , " " , " " , " " , " " , " " , " " , "W"],
    ["W" , " " , " " , " " , "W" , " " , " " , "W" , " " , " " , " " , " " , " " , " " , " " , " " , " " , "/2/True" , " " , "W"],
    ["W" , " " , " " , " " , "W" , " " , " " , "W" , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , " " , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"]
]

target_6 = 1
level_6 = [
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"], 
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"]
]

target_7 = 1
level_7 = [
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"], 
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"]
]

target_8 = 1
level_8 = [
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"], 
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"],
    ["W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W" , "W"]
]

levels = [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8]
targets = [target_1, target_2, target_3, target_4, target_5, target_6, target_7, target_8]

game_maps = [MapGame(level_1, target_1, img_level[0]), MapGame(level_2, target_2, img_level[1]), 
             MapGame(level_3, target_3, img_level[2]), MapGame(level_4, target_4, img_level[3]),
             MapGame(level_5, target_5, img_level[4]), MapGame(level_6, target_6, img_level[5]), 
             MapGame(level_7, target_7, img_level[6]), MapGame(level_8, target_8, img_level[7])]
