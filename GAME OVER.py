######################################################## GAME OVER #######################################################


class Game_over():
    def __init__(self):
        self.go_img = pygame.image.load(
            'C:/Users/ASUS/Desktop/python/tanki/resources/images/intro/go.png')
        self.speed = 1
        self.fade_counter = 0
        self.update_time = pygame.time.get_ticks()
        self.finish = False

    def display(self):
        if self.fade_counter == 2:
            gameover.play()

        if self.fade_counter <= 240:
            self.go_img = pygame.transform.scale(self.go_img, (300, 150))
            # ((screen_height-self.go_img.get_height())//2)+(screen_height//2-self.fade_counter))
            screen.blit(self.go_img, ((
                (screen_width-150-self.go_img.get_width())//2), (500-self.fade_counter)))

            if pygame.time.get_ticks() - self.update_time > 15:
                self.update_time = pygame.time.get_ticks()
                self.fade_counter += 2
            detials.score_time = pygame.time.get_ticks()

        elif self.fade_counter > 240:
            self.go_img = pygame.transform.scale(self.go_img, (300, 150))
            screen.blit(self.go_img, (((screen_width-150-self.go_img.get_width())//2),
                        ((screen_height-self.go_img.get_height())//2)+(screen_height//2-self.fade_counter)))
            self.finish = True

    def reset_all(self):
        # reset variables
        global next_enemy, enemy_index, speed_limit, enemy_counter, player_spawn_counter, start_game, world, level_no, current_level, next_level, data

        next_enemy = 1
        enemy_index = 0
        speed_limit = 1
        enemy_counter = 0
        player_spawn_counter = 1
        start_game = True
        level_no = 1
        current_level = 1
        next_level = False
        self.finish = False

        detials.total1_count = 0
        detials.total2_count = 0
        detials.total3_count = 0
        detials.total4_count = 0

        # clear all list
        p1_point.clear()
        p2_point.clear()
        # p3_point.clear()
        # p4_point.clear()

        p1_TP.clear()
        p2_TP.clear()
        # p3_TP.clear()
        # p4_TP.clear()

        player_list.clear()
        enemy_list.clear()
        char_list.clear()

        player_list_detial.clear()
        enemy_list_detial.clear()
        char_list_detial.clear()

        enemy_pastaway.clear()
        tank_pastaway.clear()
        player_pastaway.clear()

        powerUP_count.clear()
        enemy_count.clear()
        enemy_levelUP.clear()
        for i in [5, 10, 15]:
            powerUP_count.append(i)
        for i in range(-5, 16):
            enemy_count.append(i)
        for i in [6, 11, 16]:
            enemy_levelUP.append(i)

        # empty all groups
        rocket_group.empty()
        powerUP_group.empty()
        rocket_blast_group.empty()
        wall_blast_group.empty()

        data = world_create()
        world = World(data)

        fade1.fade_counter = 0
