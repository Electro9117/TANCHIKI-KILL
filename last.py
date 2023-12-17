def world_create():
    world_data = [
        [0,    0, rl(), rl(), rl(), rl(), rl(), rl(),    0,    0, rl(),
         rl(), rl(), rl(), rl(),    0,    0, 1, 1, 1],
        [0,    0,    0, rl(), rl(), rl(), rl(),    0,    0, rl(), rl(),
         rl(), rl(), rl(),    0,    0,    0, 1, 1, 1],
        [rl(), rl(),    0, rl(), rl(), rl(), rl(),    0, rl(), rl(),
            rl(), rl(),    0,    0,    0, rl(), rl(), 1, 1, 1],
        [rl(), rl(),    0, rl(), rl(),    0,    0,    0,    0, rl(),
            rl(), rl(),    0, rl(), rl(), rl(), rl(), 1, 1, 1],
        [0,    0,    0, rl(), rl(),    0, rl(), rl(),    0, rl(), rl(),
         rl(),    0, rl(), rl(), rl(), rl(), 1, 1, 1],
        [rl(), rl(),    0, rl(), rl(), rl(), rl(), rl(),    0,
            0,    0, rl(),    0, rl(), rl(), rl(), rl(), 1, 1, 1],
        [rl(), rl(), rl(), rl(), rl(),    0, rl(), rl(), rl(),
            rl(),    0,    0, rl(), rl(), rl(), rl(), rl(), 1, 1, 1],
        [rl(), rl(),    0, rl(), rl(), rl(),    0,    0, rl(), rl(),
            rl(), rl(),    0,    0,    0, rl(), rl(), 1, 1, 1],
        [rl(), rl(), rl(),    0, rl(), rl(), rl(), rl(), rl(),
            rl(),    0,    0,    0, rl(),    0, rl(), rl(), 1, 1, 1],
        [rl(), rl(), rl(), rl(),  rl(),    0,    0,    0, rl(),
            rl(),    0, rl(), rl(), rl(), rl(), rl(), rl(), 1, 1, 1],
        [rl(), rl(), rl(),    0,    0, rl(), rl(), rl(), rl(),
            rl(),    0, rl(), rl(), rl(),    0, rl(), rl(), 1, 1, 1],
        [rl(), rl(), rl(), rl(), rl(),    0, rl(), rl(), rl(), rl(),
            rl(), rl(), rl(), rl(),    0, rl(), rl(), 1, 1, 1],
        [rl(), rl(), rl(), rl(), rl(),    0, rl(),    8,    8,
            8,    0, rl(),    0,    0, rl(), rl(), rl(), 1, 1, 1],
        [rl(), rl(), rl(), rl(),    0,    0,    0,    8,    7,
            8,    0,    0,    0, rl(), rl(), rl(), rl(), 1, 1, 1]
    ]                                                   #
    # centre

    return world_data


data = world_create()
world = World(data)
detials = Detials()
ga_ov = Game_over()

# create screen fades
fade1 = ScreenFade(1, BLACK, 4, 0)

# create sprite groups
rocket_group = pygame.sprite.Group()
powerUP_group = pygame.sprite.Group()
rocket_blast_group = pygame.sprite.Group()
wall_blast_group = pygame.sprite.Group()

# creating enemys
enemy_group_list = ["enemy1", "enemy2", "enemy3", "enemy4", "enemy5", "enemy6", "enemy7", "enemy8",
                    "enemy9", "enemy10", "enemy11", "enemy12", "enemy13", "enemy14", "enemy15",
                    "enemy16", "enemy17", "enemy18", "enemy19", "enemy20"]

# creating players
player_group_list = ["player1", "player2"]

# key assign
key_list = [(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_0),
            (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE)]


next_enemy = 1
enemy_index = 0
run = True
level_no = 1
speed_limit = 1
enemy_counter = 0
frame_index = 0
select_tank_pos = 0
select_tank_pos1 = 0
player_spawn_counter = 1
option_select = None
next_level = False
control = False


def control_menu():
    global pl_image, re_img, frame_index, update_time, control_img

    control_img = pygame.transform.scale(control_img, (1000, 700))
    screen.blit(control_img, (0, 0))

    re_img = pygame.transform.scale(re_img, (200, 80))
    screen.blit(re_img, ((screen_width-re_img.get_width())//2,
                ((screen_height-re_img.get_height())//2)+275))

    # update image depending on current frame
    pl_image = pl_img[frame_index]
    # check if enough time has passed since the last update
    if pygame.time.get_ticks() - update_time > 130:
        update_time = pygame.time.get_ticks()
        frame_index += 1
    # if the animation has run out the reset back to the start
    if frame_index >= len(pl_img):
        frame_index = 0

    pl_image = pygame.transform.scale(pl_image, (50, 50))
    screen.blit(pl_image, (((screen_width-pl_image.get_width())//2) -
                140, ((screen_height-pl_image.get_height())//2)+274))


while run:

    clockobject.tick(fps)
    screen.blit(bg_img, (0, 0))

    if start_game:
        detials.count = 0
        bc_img = pygame.transform.scale(bc_img, (700, 200))
        screen.blit(bc_img, ((screen_width-bc_img.get_width())//2,
                    ((screen_height-bc_img.get_height())//2)-200))

        ps_img = pygame.transform.scale(ps_img, (257, 320))
        screen.blit(ps_img, ((screen_width-ps_img.get_width())//2,
                    ((screen_height-ps_img.get_height())//2)+137))

        # update image depending on current frame
        pl_image = pl_img[frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - update_time > 130:
            update_time = pygame.time.get_ticks()
            frame_index += 1
        # if the animation has run out the reset back to the start
        if frame_index >= len(pl_img):
            frame_index = 0

        pl_image = pygame.transform.scale(pl_image, (40, 40))
        screen.blit(pl_image, (((screen_width-pl_image.get_width())//2) -
                    160, ((screen_height-pl_image.get_height())//2)+select_tank_pos))

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    steel.play()
                    if select_tank_pos > 0:
                        select_tank_pos -= 69
                if event.key == pygame.K_DOWN:
                    steel.play()
                    if select_tank_pos < 276:
                        select_tank_pos += 69
                if event.key == pygame.K_RETURN:
                    steel.play()
                    pl_sl = [0, 69, 138, 207, 276]
                    player_spawn_counter = pl_sl.index(select_tank_pos)+1
                    if player_spawn_counter == 5:
                        control = True
                        start_game = False
                    else:
                        for i in player_group_list[0:player_spawn_counter]:
                            char_list.append(i)
                            player_list.append(i)
                            if i == "player1":
                                i = Tank(i, 200, 800, 2, 1, 5, 1)
                            elif i == "player2":
                                i = Tank(i, 300, 800, 2, 1, 5, 1)

                            player_list_detial.append(i)
                            char_list_detial.append(i)
                        start_game = False
                        ga_ov.fade_counter = 0
                        gamestart.play()
                        game_start_time = pygame.time.get_ticks()

    elif control:
        control_menu()
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    steel.play()
                    if pass_game != True:
                        start_game = True
                    control = False

    elif pass_game:
        tank_move.set_volume(0.0)
        pause_img = pygame.transform.scale(pause_img, (300, 100))
        screen.blit(pause_img, ((screen_width-pause_img.get_width()) //
                    2, ((screen_height-pause_img.get_height())//2)-200))

        re_img = pygame.transform.scale(re_img, (200, 80))
        screen.blit(re_img, ((screen_width-re_img.get_width()) //
                    2, ((screen_height-re_img.get_height())//2)))

        co_img = pygame.transform.scale(co_img, (247, 80))
        screen.blit(co_img, (((screen_width-co_img.get_width())//2) +
                    20, ((screen_height-co_img.get_height())//2)+100))

        qg_img = pygame.transform.scale(qg_img, (200, 80))
        screen.blit(qg_img, ((screen_width-qg_img.get_width())//2,
                    ((screen_height-qg_img.get_height())//2)+200))

        # update image depending on current frame
        pl_image = pl_img[frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - update_time > 130:
            update_time = pygame.time.get_ticks()
            frame_index += 1
        # if the animation has run out the reset back to the start
        if frame_index >= len(pl_img):
            frame_index = 0

        pl_image = pygame.transform.scale(pl_image, (50, 50))
        screen.blit(pl_image, (((screen_width-pl_image.get_width())//2) -
                    140, ((screen_height-pl_image.get_height())//2)+select_tank_pos1))

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    tank_move.set_volume(0.6)
                    pass_game = False
                if event.key == pygame.K_UP:
                    steel.play()
                    if select_tank_pos1 > 0:
                        select_tank_pos1 -= 100
                if event.key == pygame.K_DOWN:
                    steel.play()
                    if select_tank_pos1 < 200:
                        select_tank_pos1 += 100
                if event.key == pygame.K_RETURN:
                    steel.play()
                    pl_sl = [0, 100, 200]
                    option_select = pl_sl.index(select_tank_pos1)+1
                    if option_select == 1:
                        tank_move.set_volume(0.6)
                        pass_game = False
                    elif option_select == 2:
                        control = True
                    elif option_select == 3:
                        run = False

    elif next_level:
        pygame.draw.rect(screen, BLACK, (0, 0, 1000, 700))
        score_img = pygame.transform.scale(score_img, (900, 500))
        screen.blit(score_img, (50, 100))

        score_time_add = (2000*player_spawn_counter)+4000
        if player_spawn_counter >= 1:
            if pygame.time.get_ticks() - score_time > 2000:
                if pygame.time.get_ticks() - score_time > 2000 and pygame.time.get_ticks() - score_time < 2020:
                    score.play()
                detials.p1_score(p1_point)
                player_list_detial[0].rect.x = 200
                player_list_detial[0].rect.y = 800
        if player_spawn_counter >= 2:
            if pygame.time.get_ticks() - score_time > 4000:
                if pygame.time.get_ticks() - score_time > 4000 and pygame.time.get_ticks() - score_time < 4020:
                    score.play()
                detials.p2_score(p2_point)
                player_list_detial[1].rect.x = 300
                player_list_detial[1].rect.y = 800

        if player_spawn_counter == 1:
            pygame.draw.rect(screen, BLACK, (0, 200, 1000, 700))
        elif player_spawn_counter == 2:
            pygame.draw.rect(screen, BLACK, (0, 300, 1000, 700))
        elif player_spawn_counter == 3:
            pygame.draw.rect(screen, BLACK, (0, 500, 1000, 700))

        if pygame.time.get_ticks() - score_time > score_time_add:
            # claer previous level score
            p1_point.clear()
            p2_point.clear()

            enemy_pastaway.clear()

            detials.total1_count = 0
            detials.total2_count = 0
            detials.total3_count = 0
            detials.total4_count = 0

            for i in player_list_detial:
                i.shoot = False
                i.update_action(0)
                i.born_ = True
                i.born = 0
                i.moving_left = False
                i.moving_right = False
                i.moving_up = False
                i.moving_down = False

            score_time = pygame.time.get_ticks()
            current_level += 1
            next_level = False

            gamestart.play()
            game_start_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pass_game = True
                if event.key == pygame.K_ESCAPE:
                    pass_game = True

    else:
        if len(enemy_pastaway) == 20:
            tank_move.set_volume(0.0)
            if fade1.fade():
                next_enemy = 1
                enemy_index = 0
                speed_limit = 1
                enemy_counter = 0
                level_no = 1

                # clear all list
                for i in enemy_list:
                    char_list.remove(i)
                enemy_list.clear()

                for i in enemy_list_detial:
                    char_list_detial.remove(i)
                enemy_list_detial.clear()

                tank_pastaway.clear()

                powerUP_count.clear()
                enemy_count.clear()
                enemy_levelUP.clear()
                for i in [5, 10, 15]:
                    powerUP_count.append(i)
                for i in range(-5, 16):
                    enemy_count.append(i)
                enemy_levelUP = [6, 11, 16]

                # empty all groups
                rocket_group.empty()
                powerUP_group.empty()
                rocket_blast_group.empty()
                wall_blast_group.empty()

                data = world_create()
                world = World(data)

                fade1.fade_counter = 0
                score_time = pygame.time.get_ticks()
                next_level = True

        elif ga_ov.finish:
            tank_move.set_volume(0.0)
            if detials.high_score():
                ga_ov.reset_all()

            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    run = False

        else:
            if pygame.time.get_ticks() - game_start_time > 2000:
                tank_move.set_volume(0.6)

            world.draw()
            if world.eagle_wall_change:
                world.restore_ewall()

            screen.blit(detial_img, (850, 0))
            if player_spawn_counter == 1:
                pygame.draw.rect(screen, (98, 99, 98),
                                 pygame.Rect(850, 210, 150, 310))
            elif player_spawn_counter == 2:
                pygame.draw.rect(screen, (98, 99, 98),
                                 pygame.Rect(850, 310, 150, 210))
            elif player_spawn_counter == 3:
                pygame.draw.rect(screen, (98, 99, 98),
                                 pygame.Rect(850, 410, 150, 110))

            detials.enemy_count()
            if player_spawn_counter >= 1:
                detials.player1_lives()
            if player_spawn_counter >= 2:
                detials.player2_lives()
            if player_spawn_counter >= 3:
                detials.player3_lives()
            if player_spawn_counter >= 4:
                detials.player4_lives()
            detials.current_level()

            for i in enemy_count:
                if pygame.time.get_ticks() - counter > 2000:
                    counter = pygame.time.get_ticks()
                    if len(enemy_pastaway) > i and enemy_index <= 19:
                        enemy_counter += 1
                        for j in enemy_levelUP:
                            if enemy_counter >= j:
                                level_no += 1
                                if level_no == 3:
                                    speed_limit = 2
                                elif level_no == 4:
                                    speed_limit = 1
                                enemy_levelUP.remove(j)

                        update_index = enemy_group_list[enemy_index]
                        char_list.append(update_index)
                        enemy_list.append(update_index)
                        if next_enemy == 1:
                            update_index = Tank(
                                update_index, 0, 0, -2, level_no, level_no*3, speed_limit)
                        elif next_enemy == 2:
                            update_index = Tank(
                                update_index, 400, 0, -2, level_no, level_no*3, speed_limit)
                        elif next_enemy == 3:
                            update_index = Tank(
                                update_index, 800, 0, -2, level_no, level_no*3, speed_limit)
                        next_enemy += 1
                        if next_enemy > 3:
                            next_enemy = 1
                        enemy_index += 1
                        enemy_list_detial.append(update_index)
                        char_list_detial.append(update_index)
                        enemy_count.remove(i)

            # draw power_up
            for i in powerUP_count:
                if len(enemy_pastaway) >= i:
                    power_up = Power_up(data)
                    powerUP_group.add(power_up)
                    powerUP_count.remove(i)

            # update and draw groups
            powerUP_group.update()
            for i in powerUP_group:
                i.blink()
                i.remove_power_up()
            powerUP_group.draw(screen)

            # draw_grid()

            # update player actions
            for i in player_list_detial:
                index = char_list_detial.index(i)
                if i.alive:
                    i.update()
                    i.draw()
                    i.move()
                    i.shoot_rocket()
                    # i.AI()
                elif i.alive == False and index not in player_pastaway:
                    player_pastaway.append(index)

            # update enemy actions
            for i in enemy_list_detial:
                index = char_list_detial.index(i)
                if i.alive:
                    i.update()
                    i.draw()
                    i.move()
                    i.shoot_rocket()
                    i.AI()
                elif i.alive == False and char_list[index] not in enemy_pastaway:
                    enemy_pastaway.append(char_list[index])

            rocket_group.update()
            rocket_group.draw(screen)

            world.draw_grass()

            for i in char_list_detial:
                if i.blast < 3:
                    i.draw_blast()

            rocket_blast_group.update()
            rocket_blast_group.draw(screen)

            wall_blast_group.update()
            wall_blast_group.draw(screen)

            if len(player_pastaway) == player_spawn_counter and world.eagle_blast != True:
                ga_ov.display()

            if world.eagle_blast:
                world.eagle_blast_effect()
                if len(player_pastaway) != player_spawn_counter:
                    ga_ov.display()

            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    run = False

                for i in player_list_detial[0:player_spawn_counter]:
                    if i == player_list_detial[0]:
                        player_index = 0
                    elif i == player_list_detial[1]:
                        player_index = 1
                    elif i == player_list_detial[2]:
                        player_index = 2
                    elif i == player_list_detial[3]:
                        player_index = 3

                    # keyboard presses
                    if event.type == pygame.KEYDOWN and i.alive:
                        if event.key == key_list[player_index][0]:
                            i.update_action(3)
                            i.moving_left = True
                            i.moving_right = i.moving_up = i.moving_down = False
                        elif event.key == key_list[player_index][1]:
                            i.update_action(2)
                            i.moving_right = True
                            i.moving_left = i.moving_up = i.moving_down = False
                        elif event.key == key_list[player_index][2]:
                            i.update_action(0)
                            i.moving_up = True
                            i.moving_left = i.moving_right = i.moving_down = False
                        elif event.key == key_list[player_index][3]:
                            i.update_action(1)
                            i.moving_down = True
                            i.moving_left = i.moving_right = i.moving_up = False
                        if event.key == key_list[player_index][4]:
                            i.shoot = True
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                            pass_game = True

                    # keyboard button released
                    if event.type == pygame.KEYUP:
                        if event.key == key_list[player_index][0]:
                            i.moving_left = False
                        if event.key == key_list[player_index][1]:
                            i.moving_right = False
                        if event.key == key_list[player_index][2]:
                            i.moving_up = False
                        if event.key == key_list[player_index][3]:
                            i.moving_down = False
                        if event.key == key_list[player_index][4]:
                            i.shoot = False

    pygame.display.update()

pygame.quit()
