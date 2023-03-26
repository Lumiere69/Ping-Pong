from pygame import *

back = (200, 255, 255)
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
window.fill(back)


class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (65, 65))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


FPS = 60
clock = time.Clock()
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
