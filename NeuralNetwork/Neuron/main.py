import pygame

class App:

    def __init__(self):
        self.size = self.width, self.height = WIDTH, HEIGHT
        self.running = False
        self.display_surf = None

    def on_init(self):
        self.running = True
        self.display_surf = pygame.display.set_mode(self.size)

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        pass

    def on_loop(self):
        pass

    def on_execute(self):
        self.on_init()

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.display_surf.fill((0,0,0))
            self.on_loop()
            self.on_render()
            pygame.display.flip()

        self.on_cleanup()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

if __name__ == '__main__':
    pass