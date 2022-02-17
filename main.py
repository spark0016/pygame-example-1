import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

display = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))

going_left = False
going_right = True

RED = (255, 0, 0)
CYAN = (204, 255, 204)

playerVelocity = pygame.Vector2(SCREEN_WIDTH // 2, (2 / 3) *  SCREEN_HEIGHT)

speed = 5

velocity = 0
acceleration = .1

previous_time = pygame.time.get_ticks()

bullets = []

pygame.display.set_caption("Flapiinio")

def update():
    global going_right, going_left, velocity, acceleration, previous_time
    

    playerRect = pygame.Rect(playerVelocity.x, playerVelocity.y, 50, 50)
    if going_right == True:
        playerVelocity.x += speed
    if going_left == True:
        playerVelocity.x -= speed
    
    if playerVelocity.x == 550:
        going_right = False
        going_left = True
    if playerVelocity.x == 0:
        going_right = True
        going_left = False
    
    if playerVelocity.y >= 550:
        velocity = -3
    
    if playerVelocity.y <= 0:
        velocity = 3

    
    key = pygame.key.get_pressed()
    if key[pygame.K_x]:
        velocity = -3
    
    if key[pygame.K_c]:
        current_time = pygame.time.get_ticks()
        if current_time - previous_time > 250:
            previous_time = current_time
            bullets.append([playerVelocity.x, playerVelocity.y])
    
    
    playerVelocity.y += velocity
    velocity += acceleration

    display.fill(CYAN)
    pygame.draw.rect(display, RED, playerRect)

    for bullet in bullets:
        bullet[1] -= 20
        pygame.draw.rect(display, (RED), (bullet[0] + 15, bullet[1], 20, 20))

    pygame.display.update()
    
    pygame.time.delay(20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    update()
    
