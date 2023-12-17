######################################################## SCREEN FADE ######################################################


class ScreenFade():
    def __init__(self, direction, colour, speed, width):
        self.direction = direction
        self.colour = colour
        self.speed = speed
        self.fade_counter = 0
        self.width = width

    def fade(self):
        global run
        fade_complete = False
        self.fade_counter += self.speed
        if self.direction == 1:  # whole screen fade
            pygame.draw.circle(screen, BLACK, [
                               screen_width // 2, screen_height // 2], self.fade_counter, self.width)
        if self.direction == 2:  # vertical screen fade down
            pygame.draw.rect(screen, self.colour,
                             (0, 0, screen_width, 0 + self.fade_counter))
        if self.fade_counter >= screen_width:
            fade_complete = True

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        return fade_complete
