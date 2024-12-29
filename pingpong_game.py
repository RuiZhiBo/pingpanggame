import pygame
import random
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("pingpong_game")
font = pygame.font.SysFont("微软雅黑", 40)
pygame.mixer.init()
pop = pygame.mixer.Sound("./mixer/snd_bubu_meme.wav")
win = pygame.mixer.Sound("./mixer/snd_player_win_flash.wav")
die = pygame.mixer.Sound("./mixer/snd_rockdoor_open.wav")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
board_x = 200
board_y = 550
board_weight = 200
board_hight = 25
posx = 50
posy = 50
xvel = 5
yvel = 5
keep_going = True
##keydown = False
##keypress_a = False
##keypress_d = False
score = 0
lifes = 5
clock = pygame.time.Clock()
#游戏主循环
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                posx = 50
                posy = 50
                xvel = 5
                yvel = 5
                score = 0
                lifes = 5

     #屏幕清空           
    screen.fill(BLACK)
    #挡板显示
    board_x = pygame.mouse.get_pos()[0] - board_weight/2
    pygame.draw.rect(screen, WHITE, (board_x, board_y, board_weight, board_hight))
    #弹球显示
    posx += xvel
    posy += yvel
    if posx <= 50 or posx >= 750:
        xvel = -xvel * 1.1
    if posy <= 50:
        yvel = -yvel + 1
    if posy >= 550:
        lifes += -1
        yvel = -5
        xvel = 5
        posy = 550
        die.play()
    if posy + 25 >= board_y and posy + 25 <= board_y + board_hight and yvel > 0:
        if posx >= board_x and posx <= board_x + board_weight:
            score += 1
            yvel = -yvel
            win.play()
    pygame.draw.circle(screen, RED, (posx, posy), 50)
    #玩家数值显示
    print_text = f"Lifes: {lifes} -- Scores: {score}"
    if lifes < 1:
        xvel = yvel = 0
        print_text = f"Game Over. Your score was: {score}. Press F1 to play again"
        
    text = font.render(print_text, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)
    #游戏界面更新
    pygame.display.update()
    clock.tick(60)
pygame.quit()
