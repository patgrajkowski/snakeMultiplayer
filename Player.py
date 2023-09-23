import pygame

class Player:
    score = 0
    def __init__(self, name, color, direction, position_x, position_y):
        self.name = name
        self.color = color
        self.direction = direction
        self.change_to = direction
        self.position = [position_x, position_y]
        match direction:
            case "RIGHT":
                self.snake_body = [
                                [position_x, position_y],
                                [position_x-10, position_y],
                                [position_x-20, position_y],
                                [position_x-30, position_y]
                ]
            case "LEFT":
                self.snake_body = [
                                [position_x, position_y],
                                  [position_x+10, position_y],
                                  [position_x+20, position_y],
                                  [position_x+30, position_y]
                ]
            case "UP":
                self.snake_body = [
                                [position_x, position_y],
                                  [position_x, position_y-10],
                                  [position_x, position_y-20],
                                  [position_x, position_y-30]
                ]
            case "DOWN":
                self.snake_body = [
                                [position_x, position_y],
                                  [position_x, position_y+10],
                                  [position_x, position_y+20],
                                  [position_x, position_y+30]
                ]

    def setDirection(self, direction):
        match direction:
            case "RIGHT":
                if self.direction != "LEFT":
                    self.direction = "RIGHT"
            case "LEFT":
                if self.direction != "RIGHT":
                    self.direction = "LEFT"
            case "UP":
                if self.direction != "DOWN":
                    self.direction = "UP"
            case "DOWN":
                if self.direction != "UP":
                    self.direction = "DOWN"

    def move(self, shouldPop):
        if  self.direction == 'UP':
            self.position[1] -= 10
        if  self.direction == 'DOWN':
            self.position[1] += 10
        if  self.direction == 'LEFT':
            self.position[0] -= 10
        if  self.direction == 'RIGHT':
            self.position[0] += 10
        self.snake_body.insert(0, list(self.position))
        if shouldPop == False:
            self.snake_body.pop()



    def draw(self, screen):
        for position in self.snake_body:
            pygame.draw.rect(screen, self.color, (position[0], position[1], 10, 10))


