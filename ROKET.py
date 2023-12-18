class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, char, fire_power):
        pygame.sprite.Sprite.__init__(self)
        self.blast = 0
        self.rocket_collusion = False
        self.char_type = char
        self.direction = direction
        self.fire_power = fire_power
        self.angle = 0
        self.blastx = 0
        self.blasty = 0
        self.tile_remove = []
        if self.direction == 1:
            self.angle = 270
        elif self.direction == -1:
            self.angle = 90
        elif self.direction == -2:
            self.angle = 180

        self.image = pygame.transform.rotate(rocket_img, self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if self.direction == 2 or self.direction == -2:
            self.rect.x = x+19
            if self.direction == -2:
                self.rect.y = y+55  # 50
            if self.direction == 2:  # r
                self.rect.y = y-25  # 16
        elif self.direction == 1 or self.direction == -1:
            self.rect.y = y+19
            if self.direction == 1:
                self.rect.x = x+55  # 50
            if self.direction == -1:
                self.rect.x = x-25  # 16
        self.update_time = pygame.time.get_ticks()

    def update(self):
        dx = 0
        dy = 0

        if self.direction == 1:
            dx += 4
        elif self.direction == -1:
            dx -= 4
        elif self.direction == 2:
            dy -= 4
        elif self.direction == -2:
            dy += 4

        # update rocket coordinates
        self.rect.x += dx
        self.rect.y += dy

        # check if rocket has gone off screen
        if self.rect.bottom > screen_height:
            self.kill()
        if self.rect.top < 0:
            self.kill()
        if self.rect.left < -1:
            self.kill()

        # check for wall collision
        for tile in world.tile_list:

            if tile[1].colliderect(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()) and (tile[2] == 's' or tile[2] == 'e' or tile[2] == 'default' or tile[2] == 'b'):
                if self.direction == 1:
                    self.blastx = tile[1].left-22
                    self.blasty = self.rect.y-20
                elif self.direction == -1:
                    self.blastx = tile[1].left+50
                    self.blasty = self.rect.y-20
                elif self.direction == 2:
                    self.blasty = tile[1].top+50
                    self.blastx = self.rect.x-20
                elif self.direction == -2:
                    self.blasty = tile[1].top-22
                    self.blastx = self.rect.x-20

                if tile[2] == 'b':
                    brick.play()

                if tile[2] == 's':
                    steel.play()

                if tile[2] == 'default':
                    self.kill()

                elif tile[2] != 'default':
                    if tile[3]//5 > 1:
                        if tile[2] == 's' and self.fire_power >= 2:
                            tile[0] = world.stell_wall[5 - (tile[3]//5)]
                        elif tile[2] == 'b':
                            tile[0] = world.brick_wall[5 - (tile[3]//5)]
                        elif tile[2] == 'e':
                            tile[0] = world.eagle[1]
                            if tile[3] != 1:
                                world.eagle_blast = True
                            tile[3] = 1

                    if tile[2] == 's' and self.fire_power >= 2:
                        tile[3] -= 5
                    elif tile[2] == 'b':
                        if self.fire_power == 1:
                            tile[3] -= 5
                        else:
                            tile[3] -= 10

                    if tile[3] <= 0:
                        self.tile_remove.append(tile)

                    wall_bst = Wall_blast(
                        self.blastx, self.blasty, self.direction, self.tile_remove)
                    wall_blast_group.add(wall_bst)
                    self.kill()

        # check collision with char
        if self.char_type == "player1" or self.char_type == "player2" or self.char_type == "player3" or self.char_type == "player4":
            self.check_list = enemy_list_detial
        else:
            self.check_list = player_list_detial
        for i in self.check_list:
            if i.born_ == False:
                if i.rect.colliderect(self.rect.x, self.rect.y + dy, self.image.get_width(), self.image.get_height()):
                    if i.alive:
                        steel.play()
                        if self.fire_power == 1:
                            i.health -= 5
                        elif self.fire_power >= 2:
                            i.health -= 10
                        if i.health <= 0:
                            tank_blast.play()
                            if self.char_type == "player1":
                                p1_point.append(i.level)
                            elif self.char_type == "player2":
                                p2_point.append(i.level)
                            # elif self.char_type == "player3":
                            #     p3_point.append(i.level)
                            # elif self.char_type == "player4":
                            #     p4_point.append(i.level)

                        self.kill()

        # check for rocket and rocket collision
        for i in rocket_group:
            if i.rect.colliderect(self.rect.x, self.rect.y + dy, self.image.get_width(), self.image.get_height()) and i.char_type != self.char_type:
                rblast.play(0, 500)
                rblast.set_volume(0.7)
                self.kill()
                i.kill()
                rocket_bst = Rocket_blast(
                    self.rect.x+self.image.get_width()//2, self.rect.y+self.image.get_height()//2)
                rocket_blast_group.add(rocket_bst)
