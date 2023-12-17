#################################################### ROCKET BLAST #######################################################


class Rocket_blast(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.update_time = pygame.time.get_ticks()
        self.frame_index_blast = 0

        # load tank blast images
        self.tank_blast = []
        for i in range(1, len(os.listdir(f'.resources/images/tank_blast'))+1):
            img = pygame.image.load(
                f"./resources/images/tank_blast/{i}.png")
            self.tank_blast.append(img)
        self.image = self.tank_blast[0]
        self.rect = self.image.get_rect()
        image_w = self.image.get_width()//2
        image_h = self.image.get_height()//2
        self.rect.x = x-image_w
        self.rect.y = y-image_h

    def update(self):
        # blast animation
        ANIMATION_COOLDOWN = 150
        # update image depending on current frame
        self.image = self.tank_blast[self.frame_index_blast]

        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index_blast += 1
        # if the animation has run out the reset back to the start
        if self.frame_index_blast == len(self.tank_blast):
            self.kill()

####################################################### WALL BLAST #######################################################


class Wall_blast(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, tile_remove):
        pygame.sprite.Sprite.__init__(self)

        self.update_time = pygame.time.get_ticks()
        self.tile_remove = tile_remove
        self.frame_index_blast = 0
        self.direction = direction
        # cсвязь направления и угла 
        if self.direction == 1:
            self.angle = 270
        elif self.direction == -1:
            self.angle = 90
        elif self.direction == 2:
            self.angle = 0
        elif self.direction == -2:
            self.angle = 180

        # load all images for the rocket_boom
        self.rocket_boom = []
        for i in range(len(os.listdir("./resources/images/rocket_boom"))):
            img = pygame.image.load(
                f"./resources/images/rocket_boom/{i}.png")
            self.rocket_boom.append(img)
        self.image = pygame.transform.rotate(self.rocket_boom[0], self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # blast animation
        ANIMATION_COOLDOWN = 55
        # update image depending on current frame

        self.image = pygame.transform.rotate(
            self.rocket_boom[self.frame_index_blast], self.angle)

        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index_blast += 1
        # if the animation has run out the reset back to the start
        if self.frame_index_blast == len(self.rocket_boom):
            if len(self.tile_remove) != 0:
                for tile in self.tile_remove:
                    if tile[3] <= 0:
                        try:
                            world.tile_list.remove(tile)
                            self.tile_remove.remove(tile)
                        except:
                            pass
            self.kill()
