import pygame

pygame.init()
screen_width = 800
screen_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
paddle_width = 20
paddle_height = 100
ball_size = 20
ball_x = int(screen_width / 2)
ball_y = int(screen_height / 2)
ball_velocity_x = .5
ball_velocity_y = .5
paddle1_x = 20
paddle1_y = int(screen_height / 2)
paddle2_x = screen_width - 20 - paddle_width
paddle2_y = int(screen_height / 2)
score1 = 0
score2 = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill(black)



    dotted_line_width = 1
    dotted_line_height = 7
    dotted_line_spacing = 20
    for i in range(0, screen_height, dotted_line_height + dotted_line_spacing):
        pygame.draw.rect(screen, white, [screen_width // 2 - dotted_line_width // 2, i, dotted_line_width, dotted_line_height])

    ball_x += ball_velocity_x
    ball_y += ball_velocity_y
    if ball_y > screen_height - ball_size or ball_y < 0:
        ball_velocity_y *= -1
    if ball_x > screen_width - ball_size:
        score1 += 1
        ball_velocity_x *= -1
    if ball_x < 0:
        score2 += 1
        ball_velocity_x *= -1

    if ball_x <= paddle1_x + paddle_width and ball_y + ball_size >= paddle1_y and ball_y <= paddle1_y + paddle_height:
        ball_velocity_x *= -1
    if ball_x + ball_size >= paddle2_x and ball_y + ball_size >= paddle2_y and ball_y <= paddle2_y + paddle_height:
        ball_velocity_x *= -1
    paddle1_y = pygame.mouse.get_pos()[1]
    paddle2_y = pygame.mouse.get_pos()[1]
    if paddle1_y > screen_height - paddle_height:
        paddle1_y = screen_height - paddle_height
    if paddle1_y < 0:
        paddle1_y = 0
    if paddle2_y > screen_height - paddle_height:
        paddle2_y = screen_height - paddle_height
    if paddle2_y < 0:
        paddle2_y = 0
    pygame.draw.rect(screen, white, [paddle1_x, paddle1_y, paddle_width, paddle_height])
    pygame.draw.rect(screen, white, [paddle2_x, paddle2_y, paddle_width, paddle_height])
    pygame.draw.rect(screen, white, [ball_x, ball_y, ball_size, ball_size])
    paddle_padding = 50
    paddle1_x = paddle_padding
    paddle2_x = screen_width - paddle_width - paddle_padding
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(score1), 1, white)
    text2 = font.render(str(score2), 1, white)
    screen.blit(text1, (int(screen_width / 4), 20))
    screen.blit(text2, (int(3 * screen_width / 4), 20))

    pygame.display.update()






