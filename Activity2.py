import pygame 
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ADDing image and background image")
background_image = pygame.transform.scale(pygame.image.load("image1.jpeg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
image1 = pygame.transform.scale(pygame.image.load("image2.jpg").convert_alpha(),(200,200))
image_rect = image1.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
text = pygame.font.Font(None, 36).render("Hello, pygame!", True, (0, 0, 0))
text_rect = text.get_rect(center= (SCREEN_WIDTH//2, SCREEN_HEIGHT//4))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        surface.blit(background_image, (0, 0))
        surface.blit(image1, image_rect)
        surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    game_loop()