########################################################## WORLD ##########################################################


class World():
    def __init__(self, data):
        self.tile_list = []
        self.s = 's'
        self.b = 'b'
        self.g = 'g'
        self.w = 'w'
        self.e = 'e'
        self.sp = 'sp'
        self.es = 'es'
        self.default = 'default'
        self.data = data
        self.water_position = []
        self.wall_health = 20
        self.eagle_wall_change = False
        self.eagle_wall_co = []
        self.update_time = pygame.time.get_ticks()
        self.restore_time = pygame.time.get_ticks()
        self.eagle_blast_time = pygame.time.get_ticks()
        self.player = None
        self.eagle_blast = False
        self.blink_count = 1

        # map images load
        self.img_ = pygame.image.load(
            f"C:/Users/ASUS/Desktop/python/tanki/resources/images/powerup/zzz.png")
        self.boarder = pygame.image.load(
            'C:/Users/ASUS/Desktop/python/tanki/resources/images/boarder.png')
        self.grass = pygame.image.load(
            "C:/Users/ASUS/Desktop/python/tanki/resources/images/grass/1.png")
        self.speed_tiled = pygame.image.load(
            "C:/Users/ASUS/Desktop/python/tanki/resources/images/speed_tiled/1.png")

        self.stell_wall = []
        self.stell_wall_index = 0
        for i in range(1, len(os.listdir("C:/Users/ASUS/Desktop/python/tanki/resources/images/stell_wall"))+1):
            img = pygame.image.load(
                f"C:/Users/ASUS/Desktop/python/tanki/resources/images/stell_wall/{i}.png")
            self.stell_wall.append(img)

        self.brick_wall = []
        self.brick_wall_index = 0
        for i in range(1, len(os.listdir("C:/Users/ASUS/Desktop/python/tanki/resources/images/brick_wall"))+1):
            img = pygame.image.load(
                f"C:/Users/ASUS/Desktop/python/tanki/resources/images/brick_wall/{i}.png")
            self.brick_wall.append(img)

        self.water = []
        self.water_index = 0
        for i in range(1, len(os.listdir("C:/Users/ASUS/Desktop/python/tanki/resources/images/water"))+1):
            img = pygame.image.load(
                f"C:/Users/ASUS/Desktop/python/tanki/resources/images/water/{i}.png")
            self.water.append(img)

        self.eagle = []
        self.eagle_index = 0
        for i in range(1, len(os.listdir("C:/Users/ASUS/Desktop/python/tanki/resources/images/eagle"))+1):
            img = pygame.image.load(
                f"C:/Users/ASUS/Desktop/python/tanki/resources/images/eagle/{i}.png")
            self.eagle.append(img)

        self.eagle_boom = []
        self.eagle_boom_index = 0
        for i in range(1, len(os.listdir("C:/Users/ASUS/Desktop/python/tanki/resources/images/boom"))+1):
            img = pygame.image.load(
                f"C:/Users/ASUS/Desktop/python/tanki/resources/images/boom/{i}.png")
            self.eagle_boom.append(img)

        self.map_tile_lst = [self.boarder, self.grass, self.speed_tiled, self.stell_wall[self.stell_wall_index],
                             self.brick_wall[self.brick_wall_index], self.water[self.water_index], self.eagle[self.eagle_index]]
        # rendering images
        ep = 'en'
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                tile = tile - 1
                if tile != -1:
                    if tile == 7:
                        img = pygame.transform.scale(
                            self.map_tile_lst[4], (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        self.eagle_wall_co.append(
                            [img, img_rect, self.b, self.wall_health, 'es'])
                        self.tile_list.append(
                            [img, img_rect, self.b, self.wall_health, 'es'])

                    if tile != 7:
                        img = pygame.transform.scale(
                            self.map_tile_lst[tile], (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size

                        if tile == 1:
                            tile = [img, img_rect, self.g,
                                    self.wall_health, ep]   # grass
                        elif tile == 2:
                            tile = [img, img_rect, self.sp,
                                    self.wall_health, ep]  # speed_tiled
                        elif tile == 5:
                            tile = [img, img_rect, self.w,
                                    self.wall_health, ep]   # water
                            self.water_position.append(img_rect)
                        elif tile == 3:
                            tile = [img, img_rect, self.s,
                                    self.wall_health, ep]   # stell_wall
                        elif tile == 4:
                            tile = [img, img_rect, self.b,
                                    self.wall_health, ep]   # brick_wall
                        elif tile == 6:
                            tile = [img, img_rect, self.e,
                                    self.wall_health, ep]   # eagle
                            self.ex, self.ey = img_rect.x+25, img_rect.y+25
                        else:
                            tile = [img, img_rect, self.default,
                                    self.wall_health, ep]
                        self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def water_effect(self):
        # update animation
        ANIMATION_COOLDOWN = 550
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.water_index += 1
        # if the animation has run out the reset back to the start
        if self.water_index >= len(self.water):
            self.water_index = 0
        if self.eagle_wall_change == False:
            self.restore_time = pygame.time.get_ticks()
            self.blink = pygame.time.get_ticks()

    def eagle_blast_effect(self):
        # update animation
        ANIMATION_COOLDOWN = 180
        # update image depending on current frame
        if self.eagle_boom_index < len(self.eagle_boom):
            self.image_blast = self.eagle_boom[self.eagle_boom_index]
        image_w = self.image_blast.get_width()//2
        image_h = self.image_blast.get_height()//2
        if self.eagle_boom_index == 0:
            tank_blast.play()
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.eagle_blast_time > ANIMATION_COOLDOWN:
            self.eagle_blast_time = pygame.time.get_ticks()
            self.eagle_boom_index += 1
        # if the animation has run out the reset back to the start
        if self.eagle_boom_index >= len(self.eagle_boom):
            self.image_blast = self.eagle_boom[0]

        screen.blit(self.image_blast, (self.ex-image_w, self.ey-image_h))

    def restore_ewall(self):
        # update animation
        if self.eagle_wall_change:
            # update image depending on current frame
            # check if enough time has passed since the last update
            if pygame.time.get_ticks() - self.restore_time > 40000 and pygame.time.get_ticks() - self.restore_time < 50000:
                if pygame.time.get_ticks() - self.blink > 1000:
                    self.blink = pygame.time.get_ticks()
                    for tile in self.tile_list:
                        if tile[4] == 'es':
                            if self.player:
                                if self.blink_count % 2 == 0:
                                    tile[0] = self.stell_wall[0]
                                    tile[2] = self.b
                                    tile[3] = self.wall_health
                                else:
                                    tile[0] = self.brick_wall[0]
                            else:
                                if self.blink_count % 2 == 0:
                                    tile[0] = pygame.transform.scale(
                                        self.img_, (0, 0))
                                else:
                                    tile[0] = self.brick_wall[0]
                    self.blink_count += 1

            ANIMATION_COOLDOWN = 50000
            if pygame.time.get_ticks() - self.restore_time > ANIMATION_COOLDOWN:
                self.restore_time = pygame.time.get_ticks()
                for tile in self.tile_list:
                    if tile[4] == 'es':
                        tile[0] = self.brick_wall[0]
                        tile[2] = self.b
                        tile[3] = self.wall_health

                self.eagle_wall_change = False

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

            # water effect
            self.water_effect()
            for k in self.water_position:
                if tile[1] == k:
                    screen.blit(self.water[self.water_index], k)

    def draw_grass(self):
        for tile in self.tile_list:
            if tile[2] == self.g:
                screen.blit(tile[0], tile[1])
