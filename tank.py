############################################################## TANK #######################################################


class Tank(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, direction, level, health, speed):  # конструктор  с параметром
        pygame.sprite.Sprite.__init__(self)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.shoot = False
        self.alive = True
        self.level = level
        self.fire_power = 1
        self.skit = False  # ??????????????????????????????????????????????????????????????????????????????????????????????
        self.char_type = char_type
        self.speed_o = self.speed = speed
        self.shoot_cooldown = 0
        self.health = health
        self.lifes = 3
        self.count = 0
        self.max_health = self.health
        self.direction = direction
        self.action = 0
        # and char_type != "player3" and char_type != "player4":
        if char_type != "player1" and char_type != "player2":
            self.action = 1
            self.direction = -2
            self.lifes = 1
        # action timers
        self.frame_index = 0
        self.frame_index_blast = 0
        self.frame_spawn_index = 0
        self.frame_shiled_index = 0
        self.animation_list = []
        self.blast = 0
        self.born = 0
        self.blink_count = 1
        self.born_ = True
        self.timer = False
        self.shiled_active = False
        self.update_time = pygame.time.get_ticks()
        self.spawn_time = pygame.time.get_ticks()
        self.shiled_time = pygame.time.get_ticks()
        self.shiled_time_end = pygame.time.get_ticks()
        self.cooldown_timer = pygame.time.get_ticks()
        self.blink = pygame.time.get_ticks()

        # load tank blast images
        self.tank_blast = []
        for i in range(1, len(os.listdir(f'C:/Users/91166/Desktop/python/tanki/resources/images/tank_blast'))+1):
            img = pygame.image.load(
                f"C:/Users/91166/Desktop/python/tanki/resources/images/tank_blast/{i}.png")
            self.tank_blast.append(img)
        self.image_blast = self.tank_blast[0]

        # load tank shiled images
        self.tank_shiled = []
        for i in range(1, len(os.listdir(f'C:/Users/91166/Desktop/python/tanki/resources/images/shiled'))+1):
            img = pygame.image.load(
                f"C:/Users/91166/Desktop/python/tanki/resources/images/shiled/{i}.png")
            self.tank_shiled.append(img)
        self.image_shiled = self.tank_shiled[0]

        # load tank spawn images
        self.tank_spawn = []
        for i in range(1, len(os.listdir(f'C:/Users/91166/Desktop/python/tanki/resources/images/tank_spawn'))+1):
            img = pygame.image.load(
                f"C:/Users/91166/Desktop/python/tanki/resources/images/tank_spawn/{i}.png")
            self.tank_spawn.append(img)
        self.image_spawn = self.tank_spawn[0]

        # load all images for the players
        animation_types = ['up', 'down', 'right', 'left']
        for animation_index in range(1, 5):
            temp_list_lv = []
            for animation in animation_types:
                # reset temporary list of images
                temp_list = []
                # count number of files in the folder
                if char_type != "player1" and char_type != "player2":
                    num_of_frames = len(os.listdir(
                        f'C:/Users/91166/Desktop/python/tanki/resources/images/enemy/{"lv"+str(animation_index)}/{animation}'))
                else:
                    num_of_frames = len(os.listdir(
                        f'C:/Users/91166/Desktop/python/tanki/resources/images/{self.char_type}/{"lv"+str(animation_index)}/{animation}'))
                for i in range(1, num_of_frames+1):
                    if char_type != "player1" and char_type != "player2":
                        img = pygame.image.load(
                            f"C:/Users/91166/Desktop/python/tanki/resources/images/enemy/{'lv'+str(animation_index)}/{animation}/{i}.png")
                    else:
                        img = pygame.image.load(
                            f"C:/Users/91166/Desktop/python/tanki/resources/images/{self.char_type}/{'lv'+str(animation_index)}/{animation}/{i}.png")
                    temp_list.append(img)
                temp_list_lv.append(temp_list)
            self.animation_list.append(temp_list_lv)

        self.image = self.animation_list[self.level -1][self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.spawn_x = self.rect.x = x
        self.spawn_y = self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.space = False
        self.collusion = False

        # AI variables
        self.ran_move = 1
        self.movement_count = 0
        self.vision = pygame.Rect(0, 0, 300, 20)
        self.angle = 0

    def update(self):
        self.update_animation()
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self):
        dx = 0
        dy = 0

        if self.moving_up:
            self.skit = True
            dy -= self.speed
            self.direction = 2

        elif self.moving_down:
            self.skit = True
            dy += self.speed
            self.direction = -2

        elif self.moving_left:
            self.skit = True
            dx -= self.speed
            self.direction = -1

        elif self.moving_right:
            self.skit = True
            dx += self.speed
            self.direction = 1

        if self.direction == 1:
            self.angle = 270
        elif self.direction == -1:
            self.angle = 90
        elif self.direction == 2:
            self.angle = 0
        elif self.direction == -2:
            self.angle = 180

        self.char_collusionx = False # стлкноыение
        self.char_collusiony = False
        # check for tank collision
        index = char_list.index(self.char_type)
        j = 0
        for i in char_list_detial:
            if i.alive:
                # x-axis
                if i.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) and j != index:
                    self.char_collusionx = True
                    if self.direction == 1:
                        self.ran_move = random.choice([1, 2, 4])
                        self.movement_count = 0
                    elif self.direction == -1:
                        self.ran_move = random.choice([1, 2, 3])
                        self.movement_count = 0
                    dx = 0

                # y-axis
                elif i.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height) and j != index:
                    self.char_collusiony = True
                    if self.direction == 2:
                        self.ran_move = random.choice([1, 3, 4])
                        self.movement_count = 0
                    elif self.direction == -2:
                        self.ran_move = random.choice([2, 3, 4])
                        self.movement_count = 0
                    dy = 0
            j += 1

        # check for wall collision
        self.speed = self.speed_o
        for tile in world.tile_list:
            if tile[2] == 'sp':
                if tile[1].colliderect(self.rect.x, self.rect.y, self.width, self.height):
                    if self.skit:
                        # if self.direction == 1 or self.direction == -1 or self.direction == -2 or self.direction == 2:
                        self.speed = self.speed_o + 1
                        if self.direction == -1 and self.moving_left == False:
                            self.count += 1
                            dx -= 1
                        elif self.direction == 1 and self.moving_right == False:
                            self.count += 1
                            dx += 1
                        elif self.direction == -2 and self.moving_down == False:
                            self.count += 1
                            dy += 1
                        elif self.direction == 2 and self.moving_up == False:
                            self.count += 1
                            dy -= 1

                        if self.count >= 40:
                            self.skit = False
                            self.count = 0

            if tile[2] == 's' or tile[2] == 'e' or tile[2] == 'default' or tile[2] == 'b' or tile[2] == 'w':
                # x-axis
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    if self.direction == 1:
                        self.ran_move = random.choice([1, 2, 4])
                        self.movement_count = 0
                    elif self.direction == -1:
                        self.ran_move = random.choice([1, 2, 3])
                        self.movement_count = 0

                    y = str(self.rect.y)
                    if len(y) == 1:
                        y = "00"+y
                    elif len(y) == 2:
                        y = "0"+y

                    if int(y[1:]) >= 40 and int(y[1:]) <= 60:
                        self.rect.y = int(y[0]+"50")
                    if int(y[1:]) >= 90:
                        self.rect.y = int(y[0]+"00")+100
                    if int(y[1:]) <= 10:
                        self.rect.y = int(y[0]+"00")
                    dx = 0
                    break

                # y-axis
                elif tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.direction == 2:
                        self.ran_move = random.choice([1, 3, 4])
                        self.movement_count = 0
                    elif self.direction == -2:
                        self.ran_move = random.choice([2, 3, 4])
                        self.movement_count = 0

                    x = str(self.rect.x)
                    if len(x) == 1:
                        x = "00"+x
                    elif len(x) == 2:
                        x = "0"+x

                    if int(x[1:]) >= 40 and int(x[1:]) <= 60:
                        self.rect.x = int(x[0]+"50")
                    if int(x[1:]) >= 90:
                        self.rect.x = int(x[0]+"00")+100
                    if int(x[1:]) <= 10:
                        self.rect.x = int(x[0]+"00")
                    dy = 0
                    break

        if self.char_collusionx:
            dx = 0
        if self.char_collusiony:
            dy = 0

        # update player coordinates
        if self.timer == False and self.born_ == False and self.health >= 0:
            self.rect.x += dx
            self.rect.y += dy

        # boarder check
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0
            self.ran_move = random.choice([2, 3, 4])
            self.movement_count = 0
        if self.rect.top < 0:
            self.rect.top = 0
            dy = 0
            self.ran_move = random.choice([1, 3, 4])
            self.movement_count = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            dx = 0
            self.ran_move = random.choice([1, 2, 4])
            self.movement_count = 0
        if self.rect.left < 0:
            self.rect.left = 0
            dx = 0
            self.ran_move = random.choice([1, 2, 3])
            self.movement_count = 0

    def AI(self):
        if self.alive:
            self.movement_count += 1
            if self.movement_count < 50:
                if self.ran_move == 1:
                    self.action = 0
                    self.moving_down = self.moving_right = self.moving_left = False
                    self.moving_up = True
                    self.direction = 2
                    self.vision = pygame.Rect(0, 0, 20, 300)
                    self.vision.center = (
                        self.rect.centerx, self.rect.centery - 150)
                elif self.ran_move == 2:
                    self.action = 1
                    self.moving_up = self.moving_right = self.moving_left = False
                    self.moving_down = True
                    self.direction = -2
                    self.vision = pygame.Rect(0, 0, 20, 300)
                    self.vision.center = (
                        self.rect.centerx, self.rect.centery + 150)
                elif self.ran_move == 3:
                    self.action = 2
                    self.moving_up = self.moving_down = self.moving_left = False
                    self.moving_right = True
                    self.direction = 1
                    self.vision = pygame.Rect(0, 0, 300, 20)
                    self.vision.center = (
                        self.rect.centerx + 150, self.rect.centery)
                elif self.ran_move == 4:
                    self.action = 3
                    self.moving_right = self.moving_up = self.moving_down = False
                    self.moving_left = True
                    self.direction = -1
                    self.vision = pygame.Rect(0, 0, 300, 20)
                    self.vision.center = (
                        self.rect.centerx - 150, self.rect.centery)

            if self.movement_count >= 100:
                self.ran_move = random.randint(1, 4)
                self.movement_count = 0

            # vision of AI
            for tile in world.tile_list:
                if self.vision.colliderect(tile[1]):
                    if tile[2] == 'b':
                        self.enemy_shoot()
                    if (tile[2] == 's' and self.fire_power >= 2):
                        self.enemy_shoot()
                    if tile[2] == 'e' and (self.char_type != "player1" or self.char_type != "player2" or self.char_type != "player3" or self.char_type != "player4"):
                        if tile[3] != 1:
                            self.enemy_shoot()

            if self.char_type == "player1" or self.char_type == "player2" or self.char_type == "player3" or self.char_type == "player4":
                self.check_list = enemy_list_detial
            else:
                self.check_list = player_list_detial
            for pl in self.check_list:
                if pl.alive:
                    if self.vision.colliderect(pl.rect):
                        self.enemy_shoot()

    def shoot_rocket(self):
        if self.born_ == False and self.timer == False and self.shoot == True:
            if self.fire_power <= 2 and self.shoot_cooldown == 0:
                self.shoot_cooldown = 80
                tank_fire.play()
                rocket = Rocket(self.rect.x, self.rect.y,
                                self.direction, self.char_type, self.fire_power)
                rocket_group.add(rocket)
            elif self.fire_power == 3 and (self.shoot_cooldown == 0 or self.shoot_cooldown == 8):
                if self.shoot_cooldown == 0:
                    self.shoot_cooldown = 50
                tank_fire.play()
                rocket = Rocket(self.rect.x, self.rect.y,
                                self.direction, self.char_type, self.fire_power)
                rocket_group.add(rocket)

    def enemy_shoot(self):
        if self.born_ == False and self.timer == False:
            if self.fire_power <= 2 and self.shoot_cooldown == 0:
                self.shoot_cooldown = 80
                tank_fire.play()
                rocket = Rocket(self.rect.x, self.rect.y,
                                self.direction, self.char_type, self.fire_power)
                rocket_group.add(rocket)
            elif self.fire_power == 3 and (self.shoot_cooldown == 0 or self.shoot_cooldown == 8):
                if self.shoot_cooldown == 0:
                    self.shoot_cooldown = 50
                tank_fire.play()
                rocket = Rocket(self.rect.x, self.rect.y,
                                self.direction, self.char_type, self.fire_power)
                rocket_group.add(rocket)

    def shiled_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 200
        # update image depending on current frame
        self.image_shiled = self.tank_shiled[self.frame_shiled_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.shiled_time > ANIMATION_COOLDOWN:
            self.shiled_time = pygame.time.get_ticks()
            self.frame_shiled_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_shiled_index >= len(self.tank_shiled):
            self.frame_shiled_index = 0
        if pygame.time.get_ticks() - self.shiled_time_end > 30000:
            self.shiled_active = False
            self.health = self.level*5

    def timer_cooldown(self):
        if pygame.time.get_ticks() - self.cooldown_timer > 15000:
            self.timer = False
        # update image depending on current frame
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.cooldown_timer > 10000 and pygame.time.get_ticks() - self.cooldown_timer < 15000:
            if pygame.time.get_ticks() - self.blink > 300:
                self.blink = pygame.time.get_ticks()
                if self.blink_count % 2 == 0:
                    self.image = pygame.transform.scale(world.img_, (0, 0))
                else:
                    self.image = self.animation_list[self.level -
                                                     1][self.action][0]
            self.blink_count += 1

    def update_animation(self):
        if self.health >= 0 and self.timer == False:
            # update animation
            ANIMATION_COOLDOWN = 100 #время перезарядки 
            # update image depending on current frame
            self.image = self.animation_list[self.level -1][self.action][self.frame_index]
            # check if enough time has passed since the last update
            if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN and (self.moving_up or self.moving_down or self.moving_left or self.moving_right or self.speed != self.speed_o):
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            # if the animation has run out the reset back to the start
            if self.frame_index >= len(self.animation_list[self.level - 1][self.action]):
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action and self.timer == False:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    # tank spawn animation
    def tank_born(self):
        # update animation
        ANIMATION_COOLDOWN = 180
        # update image depending on current frame
        self.image_spawn = self.tank_spawn[self.frame_spawn_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.spawn_time > ANIMATION_COOLDOWN:
            self.spawn_time = pygame.time.get_ticks()
            if self.frame_spawn_index >= 0:
                self.frame_spawn_index += 1
            else:
                self.frame_spawn_index -= 1
        # if the animation has run out the reset back to the start
        if self.frame_spawn_index >= len(self.tank_spawn):
            self.born += 1
            self.frame_spawn_index = -2
        elif self.frame_spawn_index < -4:
            self.born += 1
            self.frame_spawn_index = 1
        if self.born >= 2:
            self.born_ = False

    def check_alive(self):
        if self.shiled_active == False:
            self.shiled_time_end = pygame.time.get_ticks()

        if self.timer == False:
            self.cooldown_timer = pygame.time.get_ticks()
            self.blink = pygame.time.get_ticks()

        if self.health <= 0:
            self.speed = 0
            self.frame_index = 0
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

            if self.blast >= 3:
                if self.lifes > 0:
                    self.lifes -= 1

                if self.lifes < 1:
                    self.alive = False
                    self.frame_index_blast = 0
                    self.kill()

                else:
                    self.born_ = True
                    self.born = 0
                    self.rect.x = self.spawn_x
                    self.rect.y = self.spawn_y
                    self.health = 5
                    self.level = 1
                    self.fire_power = 1
                    self.blast = 0
                    self.direction = 2
                    self.action = 0

            # blast animation
            ANIMATION_COOLDOWN = 150
            # update image depending on current frame
            self.image_blast = self.tank_blast[self.frame_index_blast]
            # check if enough time has passed since the last update
            if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
                self.blast += 1
                self.update_time = pygame.time.get_ticks()
                self.frame_index_blast += 1
            # if the animation has run out the reset back to the start
            if self.frame_index_blast >= len(self.tank_blast):
                self.frame_index_blast = 0

    def draw(self):
        if self.born_:
            self.tank_born()
            screen.blit(self.image_spawn, self.rect)
        else:
            screen.blit(self.image, self.rect)
        if self.shiled_active:
            self.shiled_animation()
            screen.blit(self.image_shiled, self.rect)
        if self.timer:
            self.timer_cooldown()
        # pygame.draw.rect(screen, (255,255,255), self.rect, 1)

    def draw_blast(self):
        if self.health <= 0:
            screen.blit(self.image_blast, self.rect)
