######################################################### POWERUP #########################################################


class Power_up(pygame.sprite.Sprite):
    def __init__(self, data):
        pygame.sprite.Sprite.__init__(self)
        self.data = data
        self.spawn_location = None
        self.run = True
        self.show_image = False
        self.update_time = pygame.time.get_ticks()
        self.remove_time = pygame.time.get_ticks()
        self.animation_count = 1
        self.index = 0

        self.powerUP = []
        self.powerUP_index = 0
        for i in os.listdir("./resources/images/powerup"):
            img = pygame.image.load(
                f"./resources/images/powerup/{i}")
            self.powerUP.append(img)

        # rendering images
        self.powerUP_lst = ['boom', 'eagle_shiled', 'levelup',
                            'lifes', 'rocket_powerup', 'shiled', 'timer']
        while self.run:
            self.spawn_r = random.randint(2, 12)
            self.spawn_c = random.randint(1, 15)
            row_count = 0
            for row in self.data:
                col_count = 0
                if self.run == False:
                    break
                for tile in row:
                    if self.run == False:
                        break
                    if tile == 0 and row_count == self.spawn_r and col_count == self.spawn_c:
                        self.idx_org = self.powerUP_index = random.randint(
                            0, 6)
                        self.image = pygame.transform.scale(
                            self.powerUP[self.powerUP_index], (tile_size, tile_size))
                        self.rect = img.get_rect()
                        self.rect.x = col_count * tile_size
                        self.rect.y = row_count * tile_size
                        self.spawn_location = [
                            self.image, self.rect, self.powerUP_lst[self.powerUP_index]]
                        self.run = False
                    col_count += 1
                row_count += 1

    def blink(self):
        # update animation
        ANIMATION_COOLDOWN = 250
        # update image depending on current frame
        if self.index == 7:
            self.image = pygame.transform.scale(
                self.powerUP[self.index], (0, 0))
        else:
            self.image = pygame.transform.scale(
                self.powerUP[self.idx_org], (tile_size, tile_size))
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.index = 7
            self.update_time = pygame.time.get_ticks()
            self.animation_count += 1
        # if the animation has run out the reset back to the start
        if self.animation_count >= 3:
            self.animation_count = 1
            self.index = self.idx_org

    # remove powerup after 30 seconds
    def remove_power_up(self):
        # update animation
        ANIMATION_COOLDOWN = 30000
        # update image depending on current frame
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.remove_time > ANIMATION_COOLDOWN:
            self.kill()

    def update(self):
        self.rect.x
        self.rect.y

        # check if character catched the powerup
        for i in char_list_detial:
            if i.born_ == False and i.alive:
                if i.rect.colliderect(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()):
                    index = char_list_detial.index(i)
                    bonus.play()

                    if self.powerUP_lst[self.powerUP_index] == 'boom':
                        tank_blast.play()
                        # check if player catch boom
                        if char_list[index] == "player1" or char_list[index] == "player2" or char_list[index] == "player3" or char_list[index] == "player4":
                            for i in enemy_list_detial:
                                index_ = char_list_detial.index(i)
                                i.health = -5
                                if char_list[index_] not in enemy_pastaway:
                                    enemy_pastaway.append(char_list[index_])
                                """if i.alive == False and index_ not in tank_pastaway:
                                    tank_pastaway.append(index_)"""
                        # check if enemy catch boom
                        else:
                            for i in player_list_detial:
                                # index_ = char_list_detial.index(i)
                                i.health = -5
                                """if i.alive == False and index_ not in tank_pastaway:
                                    tank_pastaway.append(index_)"""

                    elif self.powerUP_lst[self.powerUP_index] == 'eagle_shiled':
                        self.lst = []
                        for item in world.eagle_wall_co:
                            for i in world.tile_list:
                                if (item[1] == i[1]) and (item[4] == 'es'):
                                    self.lst.append(item)
                        for item in world.eagle_wall_co:
                            if item not in self.lst:
                                world.tile_list.append(item)

                        world.eagle_wall_change = True
                        for tile in world.tile_list:
                            if char_list[index] == "player1" or char_list[index] == "player2" or char_list[index] == "player3" or char_list[index] == "player4":
                                world.player = True
                                if tile[4] == 'es':
                                    tile[0] = world.stell_wall[0]
                                    tile[2] = world.s
                                    tile[3] = world.wall_health

                            else:
                                world.player = False
                                if tile[4] == 'es':
                                    tile[0] = pygame.transform.scale(
                                        world.brick_wall[0], (0, 0))
                                    tile[2] = world.g

                    elif self.powerUP_lst[self.powerUP_index] == 'levelup':
                        if i.level < 4:
                            i.level += 1

                        if i.level == 2:
                            i.health = 10
                        elif i.level == 3:
                            i.health = 15
                            i.speed = 2
                            i.speed_o = 2
                        elif i.level == 4:
                            i.health = 20
                            i.speed = 1
                            i.speed_o = 1

                    elif self.powerUP_lst[self.powerUP_index] == 'lifes':
                        if char_list[index] == "player1" or char_list[index] == "player2" or char_list[index] == "player3" or char_list[index] == "player4":
                            i.lifes += 1

                    elif self.powerUP_lst[self.powerUP_index] == 'rocket_powerup':
                        if i.fire_power < 3:
                            i.fire_power += 1

                    elif self.powerUP_lst[self.powerUP_index] == 'shiled':
                        i.health = 100
                        i.shiled_active = True

                    elif self.powerUP_lst[self.powerUP_index] == 'timer':
                        # check if player catch timer
                        if char_list[index] == "player1" or char_list[index] == "player2" or char_list[index] == "player3" or char_list[index] == "player4":
                            for i in enemy_list_detial:
                                i.timer = True
                        # check if enemy catch timer
                        else:
                            for i in player_list_detial:
                                i.timer = True

                    self.kill()
