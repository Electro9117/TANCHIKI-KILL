#################################################### DETIALS TO DISPLAY ###################################################


class Detials():
    def __init__(self):
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        self.maroon = (128, 0, 0)
        self.navy = (0, 0, 128)
        self.silver = (192, 192, 192)
        self.yellow = (255, 255, 0)
        self.red = (255, 0, 0)
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.score_font = pygame.font.Font('freesansbold.ttf', 65)
        self.scoreT_font = pygame.font.Font('freesansbold.ttf', 45)
        self.update_time = pygame.time.get_ticks()
        self.update_time1 = pygame.time.get_ticks()
        self.count = 0

        self.high_sc = []
        self.high_sc_index = 0
        for i in range(1, len(os.listdir("C:/Users/ASUS/Desktop/python/tanki/resources/images/intro/hs"))+1):
            img = pygame.image.load(
                f"C:/Users/ASUS/Desktop/python/tanki/resources/images/intro/hs/{i}.png")
            self.high_sc.append(img)

        self.high_no = []
        self.high_no_index = 0
        for i in range(0, len(os.listdir("C:/Users/ASUS/Desktop/python/tanki/resources/images/intro/no"))):
            img = pygame.image.load(
                f"C:/Users/ASUS/Desktop/python/tanki/resources/images/intro/no/{i}.png")
            self.high_no.append(img)

        self.high_no1 = []
        self.high_no_index1 = 0
        for i in range(0, len(os.listdir("C:/Users/ASUS/Desktop/python/tanki/resources/images/intro/no1"))):
            img1 = pygame.image.load(
                f"C:/Users/ASUS/Desktop/python/tanki/resources/images/intro/no1/{i}.png")
            self.high_no1.append(img1)

        self.no_image = self.high_no[0]
        self.no_lst = self.high_no[:]

        self.pl_image_lst = []
        self.pl_image_index = 0
        for i in range(1, 5):
            self.temp_lst = []
            for j in range(1, 3):
                self.pl_img = pygame.image.load(
                    f"C:/Users/ASUS/Desktop/python/tanki/resources/images/player{i}/lv1/up/{j}.png")
                self.temp_lst.append(self.pl_img)
            self.pl_image_lst.append(self.temp_lst)
        self.pl_image = self.pl_image_lst[0][0]

        self.score_img = pygame.image.load(
            'C:/Users/ASUS/Desktop/python/tanki/resources/images/intro/score.png')
        self.score_txt_img = pygame.image.load(
            'C:/Users/ASUS/Desktop/python/tanki/resources/images/intro/sc.png')
        self.score_time = pygame.time.get_ticks()
        self.score_time_add = 0

        self.total1 = 0
        self.total2 = 0
        self.total3 = 0
        self.total4 = 0

        self.total1_count = 0
        self.total2_count = 0
        self.total3_count = 0
        self.total4_count = 0

        self.width_add = 0
        self.width_add1 = 0
        self.height_addT = 0

    def enemy_count(self):
        text = self.font.render(f'{20-enemy_counter}', True, self.silver)
        textRect = text.get_rect()
        textRect.center = (screen_width-50, 75)
        screen.blit(text, textRect)

    def player1_lives(self):
        text = self.font.render(
            f'{player_list_detial[0].lifes}', True, self.yellow)
        textRect = text.get_rect()
        textRect.center = (screen_width-50, 183)
        screen.blit(text, textRect)

    def player2_lives(self):
        text = self.font.render(
            f'{player_list_detial[1].lifes}', True, self.green)
        textRect = text.get_rect()
        textRect.center = (screen_width-50, 285)
        screen.blit(text, textRect)

    def player3_lives(self):
        text = self.font.render(
            f'{player_list_detial[2].lifes}', True, self.red)
        textRect = text.get_rect()
        textRect.center = (screen_width-50, 387)
        screen.blit(text, textRect)

    def player4_lives(self):
        text = self.font.render(
            f'{player_list_detial[3].lifes}', True, self.blue)
        textRect = text.get_rect()
        textRect.center = (screen_width-50, 488)
        screen.blit(text, textRect)

    def current_level(self):
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render(f'{current_level}', True, self.maroon)
        textRect = text.get_rect()
        textRect.center = (screen_width-95, 600)
        screen.blit(text, textRect)

    def p1_score(self, score):
        score1 = score.count(1)
        text = self.score_font.render(f'{score1}', True, self.yellow)
        textRect = text.get_rect()
        textRect.center = (170, 140)
        screen.blit(text, textRect)

        score2 = score.count(2)
        text = self.score_font.render(f'{score2}', True, self.yellow)
        textRect = text.get_rect()
        textRect.center = (358, 140)
        screen.blit(text, textRect)

        score3 = score.count(3)
        text = self.score_font.render(f'{score3}', True, self.yellow)
        textRect = text.get_rect()
        textRect.center = (543, 140)
        screen.blit(text, textRect)

        score4 = score.count(4)
        text = self.score_font.render(f'{score4}', True, self.yellow)
        textRect = text.get_rect()
        textRect.center = (725, 140)
        screen.blit(text, textRect)

        self.total1 = score1*100 + score2*200 + score3*300 + score4*400
        self.total1_count += 1
        if self.total1_count == 1:
            p1_TP.append(self.total1)
        self.total1 = str(self.total1)
        if self.total1[-3:] == "000":
            self.total1 = self.total1[:-3] + 'k'
        text = self.scoreT_font.render(f'{self.total1}', True, self.yellow)
        textRect = text.get_rect()
        textRect.center = (845, 140)
        screen.blit(text, textRect)

    def p2_score(self, score):
        score1 = score.count(1)
        text = self.score_font.render(f'{score1}', True, self.green)
        textRect = text.get_rect()
        textRect.center = (170, 275)
        screen.blit(text, textRect)

        score2 = score.count(2)
        text = self.score_font.render(f'{score2}', True, self.green)
        textRect = text.get_rect()
        textRect.center = (358, 275)
        screen.blit(text, textRect)

        score3 = score.count(3)
        text = self.score_font.render(f'{score3}', True, self.green)
        textRect = text.get_rect()
        textRect.center = (543, 275)
        screen.blit(text, textRect)

        score4 = score.count(4)
        text = self.score_font.render(f'{score4}', True, self.green)
        textRect = text.get_rect()
        textRect.center = (725, 275)
        screen.blit(text, textRect)

        self.total2 = score1*100 + score2*200 + score3*300 + score4*400
        self.total2_count += 1
        if self.total2_count == 1:
            p2_TP.append(self.total2)
        self.total2 = str(self.total2)
        if self.total2[-3:] == "000":
            self.total2 = self.total2[:-3] + 'k'
        text = self.scoreT_font.render(f'{self.total2}', True, self.green)
        textRect = text.get_rect()
        textRect.center = (845, 275)
        screen.blit(text, textRect)

    def high_score(self):
        pygame.draw.rect(screen, BLACK, (0, 0, 1000, 700))
        self.score_img = pygame.transform.scale(self.score_img, (900, 500))
        screen.blit(self.score_img, (50, 100))

        self.score_time_add = (2000*player_spawn_counter)+4000
        if player_spawn_counter >= 1:
            if pygame.time.get_ticks() - self.score_time > 2000:
                if pygame.time.get_ticks() - self.score_time > 2000 and pygame.time.get_ticks() - self.score_time < 2020:
                    score.play()
                detials.p1_score(p1_point)
        if player_spawn_counter >= 2:
            if pygame.time.get_ticks() - self.score_time > 4000:
                if pygame.time.get_ticks() - self.score_time > 2000 and pygame.time.get_ticks() - self.score_time < 4020:
                    score.play()
                detials.p2_score(p2_point)

        if player_spawn_counter == 1:
            pygame.draw.rect(screen, BLACK, (0, 200, 1000, 700))
        elif player_spawn_counter == 2:
            pygame.draw.rect(screen, BLACK, (0, 300, 1000, 700))
        elif player_spawn_counter == 3:
            pygame.draw.rect(screen, BLACK, (0, 500, 1000, 700))

        if pygame.time.get_ticks() - self.score_time > self.score_time_add:
            if pygame.time.get_ticks() - self.score_time < self.score_time_add + 20:
                hg.play()
            screen.blit(bg_img, (0, 0))

            p1_FS = sum(p1_TP)
            p2_FS = sum(p2_TP)
            # p3_FS = sum(p3_TP)
            # p4_FS = sum(p4_TP)

            score_lst = [p1_FS, p2_FS][0:player_spawn_counter]
            res = dict(zip([0, 1, 2, 3][0:player_spawn_counter], score_lst))
            sortdict = dict(
                sorted(res.items(), key=lambda x: x[1], reverse=True))

            max_score = max(score_lst)

            max_score_pl = score_lst.index(max_score)

            max_score_pl_str = str(max_score)
            for i in max_score_pl_str:
                self.no_image = pygame.transform.scale(
                    self.no_lst[int(i)], (70, 84))
                screen.blit(self.no_image, (55 + self.width_add, 120))
                self.width_add += 48
                if self.width_add >= len(max_score_pl_str)*48:
                    self.width_add = 0

            if player_spawn_counter > 1:
                screen.blit(pygame.transform.scale(
                    self.score_txt_img, (350, 90)), (30, 270))

            for i in sortdict.items():
                if i[0] != max_score_pl:

                    for j in str(i[1]):
                        self.no_image1 = pygame.transform.scale(
                            self.high_no[int(j)], (55, 70))
                        screen.blit(
                            self.no_image1, (160 + self.width_add1, 385 + self.height_addT))
                        self.width_add1 += 35
                        if self.width_add1 >= len(str(i[1]))*35:
                            self.width_add1 = 0

                    self.pl_image1 = pygame.transform.scale(
                        self.pl_image_lst[i[0]][self.pl_image_index], (70, 70))
                    screen.blit(self.pl_image1, (70, 380 + self.height_addT))
                    self.height_addT += 100
                    if self.height_addT >= (player_spawn_counter-1)*100:
                        self.height_addT = 0

            # update image depending on current frame
            self.hs_image = self.high_sc[self.high_sc_index]
            self.pl_image = pygame.transform.scale(
                self.pl_image_lst[max_score_pl][self.pl_image_index], (80, 80))
            # check if enough time has passed since the last update
            if pygame.time.get_ticks() - self.update_time > 500:
                self.no_lst = self.high_no1[:]
                self.update_time = pygame.time.get_ticks()
                self.high_sc_index += 1
                self.pl_image_index += 1
            # if the animation has run out the reset back to the start
            if self.high_sc_index >= len(self.high_sc):
                self.no_lst = self.high_no[:]
                self.high_sc_index = 0
                self.pl_image_index = 0

            screen.blit(self.pl_image, (50, 33))
            screen.blit(self.hs_image, (150, 38))

            self.count += 1
            if self.count == 1:
                self.update_time1 = pygame.time.get_ticks()

            if pygame.time.get_ticks() - self.update_time1 > 4500:
                return True
            else:
                return False
