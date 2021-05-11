import pygame, math, os, sys
from pygame import gfxdraw
from Board import Board

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 720
SCREEN_NAME = "Connect Four"


def draw_text(screen, text, size, location):
    font = pygame.font.SysFont("Comic Sans MS", size)
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, text.get_rect(center = location))


def turn(pos, circle, color, rgb, board, screen):
    for i, circ in enumerate(circle):
        for j, cir in enumerate(circle[i]):
            if math.sqrt((pos[0] - circle[i][j][0])**2 + (pos[1] - circle[i][j][1])**2) < 50:
                if board.available_plot(i):
                    y = board.get_available_plot(i)
                    pygame.gfxdraw.filled_circle(screen, circle[i][y][0], circle[i][y][1], 50, rgb)
                    pygame.gfxdraw.aacircle(screen, circle[i][y][0], circle[i][y][1], 50, rgb)
                    board.set_plot([i, y], color)
                    return True
    return False


def GameLoop():
    board = Board()

    player1 = ("Yellow", [255, 255, 0])
    player2 = ("Red", [255, 0, 0])

    player_turn = player1

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_NAME)

    if getattr(sys, 'frozen', False):
        icon = pygame.image.load(os.path.dirname(sys.executable) + "\\Images\\Red-Circle-Icon.ico")
    else:
        icon = pygame.image.load(os.path.dirname(__file__) + "\\Images\\Red-Circle-Icon.ico")

    pygame.display.set_icon(icon)

    screen.fill((0, 0, 255))

    circle = [[[] for y in range(6)] for x in range(7)]

    for i in range(6):
        for j in range(7):
            circle[j][i] = [60 + j * 120, SCREEN_HEIGHT - 60 - i * 120]
            pygame.gfxdraw.aacircle(screen, circle[j][i][0], circle[j][i][1], 50, (255, 255, 255))
            pygame.gfxdraw.filled_circle(screen, circle[j][i][0], circle[j][i][1], 50, (255, 255, 255))

    crash = False
    won = False
    draw = False
    text = False

    while not crash:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True
                pygame.quit()
                break

            elif event.type == pygame.MOUSEBUTTONUP and not won:
                turn_made = turn(pygame.mouse.get_pos(), circle, player_turn[0], player_turn[1], board, screen)
                won = board.won

                if not won:
                    draw = board.draw()

                if player_turn == player1 and turn_made and not (won or draw):
                    player_turn = player2
                elif turn_made and not (won or draw):
                    player_turn = player1

            elif event.type == pygame.KEYDOWN and (won or draw):
                if event.key == pygame.K_RETURN:
                    GameLoop()
                    crash = True
                    break

        if not text and (won or draw):
            text = True
            screen.fill((255, 255, 255))
            if won:
                draw_text(screen, player_turn[0] + " Wins!", 100, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50))
            else: 
                draw_text(screen, "Draw", 100, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50))
            draw_text(screen, "Press Enter To Play Again", 50, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50))


if __name__ == "__main__":
    GameLoop()