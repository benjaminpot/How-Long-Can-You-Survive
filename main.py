import random
import pygame
import Robot, Enemy, CameraGroup, Bullet, Player

FPS = 60 #frames per second
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 800, 600

#initialize the pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True

#initialize the robot
all_sprites = pygame.sprite.Group()
player = Player.Player(WIDTH/2, HEIGHT/2)
all_sprites.add(player)

# Create a group for the enemies
enemies = pygame.sprite.Group()
enemy_number = 5
# Create 10 enemies
for i in range(enemy_number):
    # Create an enemy at a random position
    enemy = Enemy.Enemy(random.randint(0, 800), random.randint(0, 600))
    enemies.add(enemy)
    all_sprites.add(enemy)

#initialize the camera
camera_group = CameraGroup.CameraGroup()
camera_group.add(all_sprites)

#game loop 
while running:
    clock.tick(FPS) #FPS frames per second
    screen.fill(WHITE)
    #get all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #shoot a bullet
            if event.button == 1:
                bullet = player.shoot()
                if bullet:
                    all_sprites.add(bullet)
                    camera_group.add(bullet)
    
    #update the game
    all_sprites.update()
    
    for enemy in enemies:
        # Update player position for all enemies
        enemy.update_player_position(player.rect.x, player.rect.y)
        #check if the enemy is dead
        if enemy.health <= 0:
            enemy.kill()
            enemy_number -= 1
    
    #enemy 死掉的时候，重新生成一个enemy
    if enemy_number < 5:
        enemy = Enemy.Enemy(random.randint(0, 800), random.randint(0, 600))
        enemies.add(enemy)
        all_sprites.add(enemy)
        enemy_number += 1
    #draw the screen
    #screen.fill(WHITE)
    camera_group.custom_draw(player)
    pygame.display.update()

pygame.quit()