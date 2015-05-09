import pygame,os, game_constants

from brick import brick
from ball import ball
from pad import pad
from shared import direction



game_running = True

game_over = False

game_started = False

screen = pygame.display.set_mode([game_constants.game_size.width, game_constants.game_size.height])

reloj = pygame.time.Clock()

pygame.key.set_repeat(1, 20)

brick_list = pygame.sprite.Group()

ball_list = pygame.sprite.Group()

pad_list = pygame.sprite.Group()

pads  = None

balls = None


x_position = 0

y_position = 0

def init_levels(level):
    global x_position, brick_list, y_position
    
    for x in open(os.path.join("Levels", "Level"+str(level))):
        brick_cursor = None
        for y in x:
            if y == '1':
                brick_cursor = brick(pygame, game_constants.brick_image)
                
                brick_cursor.rect.x = x_position
    
                brick_cursor.rect.y = y_position
            
                brick_list.add(brick_cursor)
                
            
            x_position += game_constants.brick_size.width + 2
            if x_position + game_constants.brick_size.width >= game_constants.game_size.width:
                    x_position= 0
                    y_position += game_constants.brick_size.height + 2                    
    
def init_balls():
    ball_game = ball(pygame, game_constants.ball_image)
    
    ball_game.rect.x = game_constants.game_size.width / 2
    
    
    ball_game.rect.y = game_constants.game_size.height - game_constants.pad_size.height \
                       - game_constants.ball_size.height / 2 
    
    ball_list.add(ball_game)
    
    return ball_game


def init_pads():
    pad_game = pad(pygame, game_constants.pad_image)
    
    pad_game.rect.x = game_constants.game_size.width / 2 - game_constants.pad_size.width/2
    
    pad_game.rect.y = (game_constants.game_size.height - game_constants.pad_size.height)
    
    pad_list.add(pad_game)
    
    return pad_game


def handle_events(events):
    global game_running, game_started
    
    for event in events:
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pads.x += 12 if pads.x + 12 <=  game_constants.game_size.width - game_constants.pad_size.width else 0
            if event.key == pygame.K_LEFT:
                pads.x -= 12 if pads.x-12 >= 0 else 0
            if event.key == pygame.K_SPACE:
                game_started = True

def handle_game_objects(balls, pads, brick_list):
    
    for rects in pygame.sprite.spritecollide(balls, brick_list, False):
        rects.reduce_lives()
        if rects.rect.collidepoint(balls.rect.midbottom) or rects.rect.collidepoint(balls.rect.midtop):
            
            balls.direction.y *= -1
        
        if rects.rect.collidepoint(balls.rect.midleft) or rects.rect.collidepoint(balls.rect.midright):
            
            balls.direction.x *= -1
    
    if balls.rect.colliderect(pads.rect):
        balls.direction.y *= -1

    
    balls.move_x()
    
    balls.move_y()    

def start_game():
    
    global game_running, game_started, game_over, balls, pads, reloj, screen
    
    
    init_levels(0)
    
    balls = init_balls()
   
    pads  = init_pads()
            
    while game_running:
        
        handle_events(pygame.event.get())
        
        
        screen.fill((0, 0, 0))
        
        reloj.tick(40)        
        
        if not balls.alive:
            game_over = True
        
        if not game_over:
            brick_list.draw(screen)
    
            ball_list.draw(screen)
    
            pad_list.draw(screen)
            
            if not game_started:
                balls.x = pads.x + pads.width / 2
                balls.y = pads.y - (balls.height + 2) 
            else:
                handle_game_objects(balls, pads, brick_list)
        else:
            print "Game Over"
        
            
        
        
        pygame.display.update()
        


start_game()
        
            
            
    